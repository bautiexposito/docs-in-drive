from app.utils.google_auth import GoogleDriveAuth

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
            raise Exception("Google Drive authentication is required. Call login_drive() first.")

        file_list = drive.ListFile({'q': "mimeType != 'application/vnd.google-apps.folder' and trashed=false"}).GetList()
        return [{"title": file["title"], "id": file["id"]} for file in file_list]
    
    @staticmethod
    def get_folders():
        drive = auth_instance.drive
        if not drive:
            raise Exception("Google Drive authentication is required. Call login_drive() first.")

        folder_list = drive.ListFile({'q': "mimeType = 'application/vnd.google-apps.folder' and trashed=false"}).GetList()
        return [{"title": folder["title"], "id": folder["id"]} for folder in folder_list]
    
    @staticmethod
    def create_file():
        return ""
        
    @staticmethod
    def create_folder():
        return ""

    @staticmethod
    def upload_file():
        return ""
    
    @staticmethod
    def download_file():
        return ""

    @staticmethod
    def search_file():
        return ""
    
    @staticmethod
    def delete_file():
        return ""
    
    @staticmethod
    def modify_file_visibility():
        # Cambia la visibilidad del archivo de público a privado
        # Envia un correo electrónico al Propietario del archivo, avisando que la visibilidad ha sido cambiada.
        return ""
    
    @staticmethod
    def insert_permissions():
        return ""
    
    @staticmethod
    def modify_permissions():
        return ""
