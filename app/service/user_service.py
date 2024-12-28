from sqlalchemy.orm import Session
from app.model.user import User
from app.persistence.user_dao import get_all_users, get_user, add_user, update_user, delete_user

class UserService:
    @staticmethod
    def get_all_users(db: Session):
        return get_all_users(db)
    
    @staticmethod
    def get_user(db: Session, user_id: int):
        user = get_user(db, user_id)
        if not user:
            raise ValueError("Usuario no encontrado")
        return user

    @staticmethod
    def create_user(db: Session, user_data: dict):
        user = User(**user_data)
        return add_user(db, user)

    @staticmethod
    def update_user(db: Session, user_id: int, user_data: dict):
        user = User(**user_data)
        return update_user(db, user_id, user)

    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = delete_user(db, user_id)
        if not user:
            raise ValueError("Usuario no encontrado")
        return user
