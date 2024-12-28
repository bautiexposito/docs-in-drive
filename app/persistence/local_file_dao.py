from sqlalchemy.orm import Session
from app.model.local_file import LocalFile

def get_all_files(db: Session):
    return db.query(LocalFile).all()

def get_file(db: Session, file_id: int):
    return db.query(LocalFile).filter(LocalFile.id == file_id).first()

def add_file(db: Session, local_file: LocalFile):
    db.add(local_file)
    db.commit()
    db.refresh(local_file)
    return local_file

def update_file(db: Session, file_id: int, updated_data: dict):
    file = db.query(LocalFile).filter(LocalFile.id == file_id).first()
    if file:
        for key, value in updated_data.items():
            if value is not None:
                setattr(file, key, value)
        db.commit()
        db.refresh(file)
        return file
    return None

def delete_file(db: Session, file_id: int):
    file = db.query(LocalFile).filter(LocalFile.id == file_id).first()
    if file:
        db.delete(file)
        db.commit()
        return True
    return False
