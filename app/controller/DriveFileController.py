from fastapi import APIRouter, HTTPException
from app.model.DriveFile import DriveFile
from app.service.DriveFileService import DriveFileService

router = APIRouter()

@router.get("/", response_model=list[DriveFile])
def get_files():
    return DriveFileService.get_all_files()

@router.get("/{file_id}", response_model=DriveFile)
def get_file(file_id: int):
    return DriveFileService.get_file(file_id)

@router.post("/", response_model=DriveFile)
def create_file(file: DriveFile):
    return DriveFileService.create_file(file)

@router.put("/{file_id}", response_model=DriveFile)
def update_file(file_id: int, file_data: DriveFile):
    try:
        return DriveFileService.update_file(file_id, file_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{file_id}")
def delete_file(file_id: int):
    try:
        DriveFileService.delete_file(file_id)
        return {"message": "File deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
