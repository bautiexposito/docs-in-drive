from typing import List
from app.model.user import User, Gender

db: List[User] = [
    User(
        id=0, 
        first_name="John",
        last_name="Travolta",
        email="jhontravolta@hotmail.com",
        gender=Gender.male,
    ),
    User(
        id=1, 
        first_name="Alexa",
        last_name="Ahmed",
        email="alexaahmed@yahoo.com",
        gender=Gender.female,
    )
]

def get_all_users():
    return db

def get_user(user_id: int):
    return db[user_id]

def add_user(user: User):
    db.append(user)

def update_user(user_id: int, user_data: User):
    for i, user in enumerate(db):
        if user.id == user_id:
            db[i] = user_data
            return True
    return False

def delete_user(user_id: int):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return True
    return False