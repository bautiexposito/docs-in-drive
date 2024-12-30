from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional

class Visibility(str, Enum):
    public = "public"
    private = "private"

class LocalFileDto(BaseModel):
    id: Optional[int] = None
    id_drive: str
    name: str
    extension: str
    emailOwner: str
    visibility: Visibility
    lastModified: datetime

    class Config:
        orm_mode = True
