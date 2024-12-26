from app.model.local_file import LocalFile
from app.persistence.local_file_dao import get_all_files, get_file, add_file, update_file, delete_file

class LocalFileService:
    @staticmethod
    def get_all_files():
        return get_all_files()
    
    @staticmethod
    def get_file(file_id: int):
        return get_file(file_id)
    
    @staticmethod
    def create_file(driveFile: LocalFile):
        add_file(driveFile)
        return driveFile
    
    @staticmethod
    def update_file(file_id: int, driveFile: LocalFile):
        if update_file(file_id, driveFile):
            return driveFile
        raise ValueError("File not found")
    
    @staticmethod
    def delete_file(file_id: int):
        if not delete_file(file_id):
            raise ValueError("File not found")
