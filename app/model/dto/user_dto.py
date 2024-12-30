from pydantic import BaseModel
from enum import Enum
from typing import Optional

class GenderEnum(str, Enum): 
    male = "male"
    female = "female"

class UserDto(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    address: str | None
    gender: GenderEnum

    class Config:
        orm_mode = True
