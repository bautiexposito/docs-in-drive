from app.model.DriveFile import DriveFile
from app.persistence.DriveFileDao import get_all_files, get_file, add_file, update_file, delete_file

class DriveFileService:
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
