from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from app.model.dto.user_dto import UserDto
from app.service.user_service import UserService
from app.controller.validator.user_validator import UserValidator
from app.persistence.database import get_db
from typing import List

router = APIRouter()

@router.get("/", response_model=List[UserDto])
def get_users(db: Session = Depends(get_db)):
    return UserService.get_all_users(db)

@router.get("/{user_id}", response_model=UserDto)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_user(db, user_id)

@router.post("/", response_model=UserDto)
def create_user(user_dto: UserDto, db: Session = Depends(get_db)):
    try:
        user_data = user_dto.model_dump(exclude={"id"})
        user_validated = UserValidator.validate(user_data)
        new_user = UserService.create_user(db, user_validated)
        return new_user
    except HTTPException as e: raise e
    except ValueError as e: raise HTTPException(status_code=400, detail=str(e))

@router.put("/{user_id}", response_model=UserDto)
def update_user(user_id: int, user_dto: UserDto, db: Session = Depends(get_db)):
    try:
        user_data = user_dto.model_dump(exclude={"id"})
        user_validated = UserValidator.validate(user_data)
        updated_user = UserService.update_user(db, user_id, user_validated)
        return updated_user
    except ValueError as e: raise HTTPException(status_code=404, detail=str(e))
    except HTTPException as e: raise e

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        UserService.delete_user(db, user_id)
        return {"message": "Usuario eliminado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
