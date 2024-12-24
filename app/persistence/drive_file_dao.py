from typing import List
from app.model.drive_file import DriveFile, Visibility

db: List[DriveFile] = [
    DriveFile(
        id=0,
        id_drive="jsd8SDYFHAS9I",
        name="requerimientos",
        extension=".txt",
        emailOwner="bautistaaexpositooo@gmail.com",
        visibility=Visibility.private,
    ),
    DriveFile(
        id=1,
        id_drive="JSD8J8dsaf9A1",
        name="README",
        extension=".md",
        emailOwner="bautistaaexpositooo@gmail.com",
        visibility=Visibility.public,
    )
]

def get_all_files():
    return db

def get_file(file_id: int):
    return db[file_id]

def add_file(driveFile: DriveFile):
    db.append(driveFile)

def update_file(file_id: int, driveFile: DriveFile):
    for i, file in enumerate(db):
        if file.id == file_id:
            db[i] = driveFile
            return True
    return False

def delete_file(file_id: int):
    for file in db:
        if file.id == file_id:
            db.remove(file)
            return True
    return False
