from typing import Optional, List
#from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    address: Optional[str] = None
    gender: Gender
