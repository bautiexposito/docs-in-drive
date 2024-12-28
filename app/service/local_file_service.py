from sqlalchemy.orm import Session
from app.model.local_file import LocalFile
from app.persistence.local_file_dao import get_all_files, get_file, add_file, update_file, delete_file

class LocalFileService:
    @staticmethod
    def get_all_files(db: Session):
        return get_all_files(db)
    
    @staticmethod
    def get_file(db: Session, file_id: int):
        file = get_file(db, file_id)
        if not file:
            raise ValueError("Archivo no encontrado")
        return file
    
    @staticmethod
    def create_file(db: Session, local_file: LocalFile):
        file = LocalFile(**local_file)
        return add_file(db, file)
    
    @staticmethod
    def update_file(db: Session, file_id: int, local_file_data: LocalFile):
        file = LocalFile(**local_file_data)
        return update_file(db, file_id, file)
    
    @staticmethod
    def delete_file(db: Session, file_id: int):
        if not delete_file(db, file_id):
            raise ValueError("Archivo no encontrado")
