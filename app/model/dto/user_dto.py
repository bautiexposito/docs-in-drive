from pydantic import BaseModel
from enum import Enum

class GenderEnum(str, Enum): 
    male = "male"
    female = "female"

class UserDto(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    address: str | None
    gender: GenderEnum

    class Config:
        orm_mode = True
