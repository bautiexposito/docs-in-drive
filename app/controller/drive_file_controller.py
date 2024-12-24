from fastapi import APIRouter, HTTPException
from app.model.drive_file import DriveFile
from app.service.drive_file_service import DriveFileService

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

@router.post("/login-drive", status_code=200)
async def login_drive():
    try:
        drive_instance = DriveFileService.login_drive()
        return {"message": "Autenticacion exitosa", "drive_instance": str(drive_instance)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al autenticar con Google Drive: {str(e)}")

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
