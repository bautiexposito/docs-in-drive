from app.utils.google_auth import GoogleDriveAuth
from app.model.local_file import Visibility
from googleapiclient.errors import HttpError

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
    
    # Cambia la visibilidad del archivo de público a privado
    # Envia un correo electrónico al Propietario del archivo, avisando que la visibilidad ha sido cambiada
    @staticmethod
    def modify_file_visibility(file_id: str, visibility: Visibility):
        drive = auth_instance.drive
        if not drive:
            raise Exception("Debe autenticarse con Google Drive.")
        
        try:
                file = drive.CreateFile({'id': file_id})
                file.FetchMetadata()
                
                if visibility == Visibility.private:
                    permissions = file.GetPermissions()
                    for permission in permissions:
                        if permission.get('type') == 'anyone':
                            file.DeletePermission(permission['id'])
                    message = "La visibilidad del archivo ha sido cambiada a privado."
                elif visibility == Visibility.public:
                    file.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'
                    })
                    message = "La visibilidad del archivo ha sido cambiada a público."
                else:
                    raise Exception("La visibilidad debe ser 'public' o 'private'.")
                
                return message

        except HttpError as error:
            raise Exception(f"Error al modificar la visibilidad del archivo: {error}")
    
    # Sincroniza los archivos de Google Drive con la base de datos
    # (si un archivo de Drive no existe en la base de datos, se crea un registro)
    @staticmethod
    def save_files_in_database():
        drive = auth_instance.drive
        if not drive:
            raise Exception("Debe autenticarse con Google Drive.")
        return ""
    
    # Listado histórico de todos los archivos que fueron en algún momento públicos
    @staticmethod
    def get_public_file_history():
        drive = auth_instance.drive
        if not drive:
            raise Exception("Debe autenticarse con Google Drive.")
        return ""
    
    @staticmethod
    def send_email():
        return ""
