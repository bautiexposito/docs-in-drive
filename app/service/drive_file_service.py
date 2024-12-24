from app.model.drive_file import DriveFile
from app.persistence.drive_file_dao import get_all_files, get_file, add_file, update_file, delete_file
from app.utils.google_auth import GoogleDriveAuth

class DriveFileService:
    @staticmethod
    def login_drive():
        auth_instance = GoogleDriveAuth()
        auth_instance.authenticate()
        return auth_instance.drive

    @staticmethod
    def get_all_files():
        return get_all_files()
    
    @staticmethod
    def get_file(file_id: int):
        return get_file(file_id)
    
    @staticmethod
    def create_file(driveFile: DriveFile):
        add_file(driveFile)
        return driveFile
    
    @staticmethod
    def update_file(file_id: int, driveFile: DriveFile):
        if update_file(file_id, driveFile):
            return driveFile
        raise ValueError("File not found")
    
    @staticmethod
    def delete_file(file_id: int):
        if not delete_file(file_id):
            raise ValueError("File not found")
