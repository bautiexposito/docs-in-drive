from fastapi import APIRouter, HTTPException
from app.model.user import User, Gender
from app.service.UserService import UserService

router = APIRouter()

@router.get("/users", response_model=list[User])
def get_users():
    return UserService.get_all_users()

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    return UserService.get_user(user_id)

@router.post("/users", response_model=User)
def create_user(user: User):
    return UserService.create_user(user)

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_data: User):
    try:
        return UserService.update_user(user_id, user_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        UserService.delete_user(user_id)
        return {"message": "Usuario eliminado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))