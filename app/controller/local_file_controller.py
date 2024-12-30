from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from app.model.dto.local_file_dto import LocalFileDto
from app.service.local_file_service import LocalFileService
from app.controller.validator.local_file_validator import LocalFileValidator
from app.persistence.database import get_db
from typing import List

router = APIRouter()

@router.get("/", response_model=List[LocalFileDto])
def get_files(db: Session = Depends(get_db)):
    return LocalFileService.get_all_files(db)

@router.get("/{file_id}", response_model=LocalFileDto)
def get_file(file_id: int, db: Session = Depends(get_db)):
    return LocalFileService.get_file(db, file_id)

@router.post("/", response_model=LocalFileDto)
def create_file(file_dto: LocalFileDto, db: Session = Depends(get_db)):
    try:
        file_data = file_dto.model_dump(exclude={"id"})
        file_validated = LocalFileValidator.validate(file_data)
        new_file = LocalFileService.create_file(db, file_validated)
        return new_file
    except HTTPException as e: raise e
    except ValueError as e: raise HTTPException(status_code=400, detail=str(e))

@router.put("/{file_id}", response_model=LocalFileDto)
def update_file(file_id: int, file_dto: LocalFileDto, db: Session = Depends(get_db)):
    try:
        file_data = file_dto.model_dump(exclude={"id"})
        file_validated = LocalFileValidator.validate(file_data)
        updated_file = LocalFileService.update_file(db, file_id, file_validated)
        return updated_file
    except HTTPException as e: raise e
    except ValueError as e: raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{file_id}")
def delete_file(file_id: int, db: Session = Depends(get_db)):
    try:
        LocalFileService.delete_file(db, file_id)
        return {"message": "Archivo eliminado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
