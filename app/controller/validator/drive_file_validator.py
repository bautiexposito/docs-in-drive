from pydantic import BaseModel
from app.model.local_file import Visibility

class ModifyVisibilityRequest(BaseModel):
    file_id: str
    visibility: Visibility
