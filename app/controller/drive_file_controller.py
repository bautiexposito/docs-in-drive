from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.persistence.database import get_db
from app.service.drive_file_service import DriveFileService
from app.controller.validator.drive_file_validator import ModifyVisibilityRequest

router = APIRouter()

@router.post("/login", status_code=200)
async def login_drive():
    try:
        drive_instance = DriveFileService.login_drive()
        return {"message": "Autenticacion exitosa", "drive_instance": str(drive_instance)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al autenticar con Google Drive: {str(e)}")
    
@router.get("/files", status_code=200)
async def get_files():
    try:
        return DriveFileService.get_files()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener archivos de Google Drive: {str(e)}")
    
@router.get("/folders", status_code=200)
async def get_folders():
    try:
        return DriveFileService.get_folders()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener carpetas de Google Drive: {str(e)}")
    
@router.get("/files/public/history", status_code=200)
async def get_public_files_history(db: Session = Depends(get_db)):
    try:
        return DriveFileService.get_public_files_history(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/file/modify_visibility", status_code=200)
def modify_file_visibility(request: ModifyVisibilityRequest, db: Session = Depends(get_db)):
    try:
        return DriveFileService.modify_file_visibility(request.file_id, request.visibility, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al modificar la visibilidad del archivo: {str(e)}")
    
@router.post("/files/save", status_code=200)
async def save_files(db: Session = Depends(get_db)):
    try:
        result = DriveFileService.save_files_in_database(db)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
