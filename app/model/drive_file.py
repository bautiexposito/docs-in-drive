from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum
from typing import Optional

class Visibility(str, Enum):
    public = "public"
    private = "private"

class DriveFile(BaseModel):
    id: int
    id_drive: str
    name: str
    extension: str
    emailOwner: EmailStr
    visibility: Visibility
    lastModified: Optional[datetime] = None
