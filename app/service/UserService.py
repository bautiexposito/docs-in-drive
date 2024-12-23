from app.model.user import User
from app.persistence.UserDao import get_all_users, get_user, add_user, update_user, delete_user

class UserService:
    @staticmethod
    def get_all_users():
        return get_all_users()
    
    @staticmethod
    def get_user(user_id: int):
        return get_user(user_id)

    @staticmethod
    def create_user(user: User):
        add_user(user)
        return user

    @staticmethod
    def update_user(user_id: int, user_data: User):
        if update_user(user_id, user_data):
            return user_data
        raise ValueError("Usuario not found")

    @staticmethod
    def delete_user(user_id: int):
        if not delete_user(user_id):
            raise ValueError("Usuario not found")
