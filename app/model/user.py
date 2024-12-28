from sqlalchemy import Column, Integer, String, Enum
from app.persistence.database import Base
from enum import Enum as PyEnum

class Gender(PyEnum):
    male = "male"
    female = "female"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    address = Column(String(500), nullable=True)
    gender = Column(Enum(Gender), nullable=False)
