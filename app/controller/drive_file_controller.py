from fastapi import APIRouter, HTTPException
from app.service.drive_file_service import DriveFileService

router = APIRouter()

@router.post("/login-drive", status_code=200)
async def login_drive():
    try:
        drive_instance = DriveFileService.login_drive()
        return {"message": "Autenticacion exitosa", "drive_instance": str(drive_instance)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al autenticar con Google Drive: {str(e)}")
    
@router.get("/", status_code=200)
async def get_files():
    try:
        return DriveFileService.get_files()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener archivos de Google Drive: {str(e)}")
    
@router.get("/", status_code=200)
async def get_folders():
    try:
        return DriveFileService.get_folders()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener carpetas de Google Drive: {str(e)}")
