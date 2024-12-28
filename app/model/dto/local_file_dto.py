from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class Visibility(str, Enum):
    public = "public"
    private = "private"

class LocalFileDto(BaseModel):
    id: int
    id_drive: str
    name: str
    extension: str
    emailOwner: str
    visibility: Visibility
    lastModified: datetime

    class Config:
        orm_mode = True
