from sqlalchemy.orm import Session
from datetime import datetime
from dateutil.parser import isoparse
from app.service.email import send_email
from app.persistence.local_file_dao import get_all_files, add_file
from app.model.local_file import LocalFile
from app.utils.google_auth import GoogleDriveAuth
from app.model.local_file import Visibility
from googleapiclient.errors import HttpError
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

auth_instance = GoogleDriveAuth()

class DriveFileService:
    @staticmethod
    def login_drive():
        auth_instance.authenticate()
        return auth_instance.drive

    @staticmethod
    def get_files():
        drive = auth_instance.drive
        if not drive:
            raise Exception("Debe autenticarse con Google Drive.")

        file_list = drive.ListFile({'q': "mimeType != 'application/vnd.google-apps.folder' and trashed=false"}).GetList()
        return [{"title": file["title"], "id": file["id"]} for file in file_list]
    
    @staticmethod
    def get_folders():
        drive = auth_instance.drive
        if not drive:
            raise Exception("Debe autenticarse con Google Drive.")

        folder_list = drive.ListFile({'q': "mimeType = 'application/vnd.google-apps.folder' and trashed=false"}).GetList()
        return [{"title": folder["title"], "id": folder["id"]} for folder in folder_list]
    
    # Modifica la visibilidad del archivo en Google Drive y el registro en la base de datos
    # Envia un correo al Propietario del archivo, avisando que la visibilidad fue modificada
    @staticmethod
    def modify_file_visibility(file_id: str, visibility: Visibility, db: Session):
        drive = auth_instance.drive
        if not drive:
            raise Exception("Debe autenticarse con Google Drive.")
        
        try:
                file = drive.CreateFile({'id': file_id})
                file.FetchMetadata()

                file_name = file["title"]
                owner_email = file["owners"][0]["emailAddress"]
                
                # Modifica la visibilidad en Google Drive
                if visibility == Visibility.private:
                    permissions = file.GetPermissions()
                    for permission in permissions:
                        if permission.get('type') == 'anyone':
                            file.DeletePermission(permission['id'])
                    visibility_status = "privado"
                elif visibility == Visibility.public:
                    file.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'
                    })
                    visibility_status = "público"
                else:
                    raise Exception("La visibilidad debe ser 'public' o 'private'.")
                
                # Actualizar la visibilidad en la base de datos
                try:
                    query = db.query(LocalFile).filter_by(id_drive=file_id).first()
                    if not query:
                        raise Exception(f"El archivo con ID '{file_id}' no fue encontrado en la base de datos.")
                    query.visibility = visibility.value
                    db.commit()
                except SQLAlchemyError as db_error:
                    db.rollback()
                    raise Exception(f"Error al actualizar la base de datos: {db_error}")
                
                # Envia un correo al propietario del archivo
                send_email(owner_email, file_name, visibility_status)
                
                return f"La visibilidad del archivo '{file_name}' fue cambiada a {visibility_status}."
        except HttpError as error:
            raise Exception(f"Error al modificar la visibilidad del archivo: {error}")
    
    # Sincroniza los archivos de Google Drive con la base de datos
    # (si un archivo de Drive no existe en la base de datos, se crea un registro)
    @staticmethod
    def save_files_in_database(db: Session):
        drive = auth_instance.drive
        if not drive:
            raise Exception("Debe autenticarse con Google Drive.")
        
        try:
            drive_files = drive.ListFile({'q': "mimeType != 'application/vnd.google-apps.folder' and trashed=false"}).GetList()
            db_files = get_all_files(db)
            db_file_ids = {file.id_drive for file in db_files}

            for file in drive_files:
                if file["id"] not in db_file_ids:
                    file_extension = file["title"].split('.')[-1] if '.' in file["title"] else ''
                    file_owner_email = file["owners"][0]["emailAddress"] if "owners" in file else "bautistaaexpositooo@gmail.com"

                    file_visibility = Visibility.private
                    permissions = drive.CreateFile({'id': file["id"]}).GetPermissions()
                    for permission in permissions:
                        if permission.get('type') == 'anyone' and permission.get('role') in ['reader', 'writer']:
                            file_visibility = Visibility.public
                            break

                    last_modified_str = file.get("modifiedDate")
                    last_modified = isoparse(last_modified_str) if last_modified_str else datetime.now()

                    new_file = LocalFile(
                        id_drive=file["id"],
                        name=file["title"],
                        extension=file_extension,
                        emailOwner=file_owner_email,
                        visibility=file_visibility,
                        lastModified=last_modified,
                    )
                    add_file(db, new_file)

            return "Archivos sincronizados exitosamente."
        except HttpError as error:
            raise Exception(f"Error al sincronizar archivos de Google Drive: {error}")
    
    # Listado histórico de todos los archivos que fueron en algún momento públicos
    @staticmethod
    def get_public_files_history(db: Session):
        drive = auth_instance.drive
        if not drive:
            raise Exception("Debe autenticarse con Google Drive.")
        
        try:
            query = text("""
                SELECT * 
                FROM public_files_history
            """)
            result = db.execute(query).fetchall()
            return [dict(row._mapping) for row in result]
        except Exception as e:
            raise Exception(f"Error al obtener el historial de archivos públicos: {e}")
