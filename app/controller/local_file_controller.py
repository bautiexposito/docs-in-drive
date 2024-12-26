from fastapi import APIRouter, HTTPException
from app.model.local_file import LocalFile
from app.service.local_file_service import LocalFileService

router = APIRouter()

@router.get("/", response_model=list[LocalFile])
def get_files():
    return LocalFileService.get_all_files()

@router.get("/{file_id}", response_model=LocalFile)
def get_file(file_id: int):
    return LocalFileService.get_file(file_id)

@router.post("/", response_model=LocalFile)
def create_file(file: LocalFile):
    return LocalFileService.create_file(file)

@router.put("/{file_id}", response_model=LocalFile)
def update_file(file_id: int, file_data: LocalFile):
    try:
        return LocalFileService.update_file(file_id, file_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{file_id}")
def delete_file(file_id: int):
    try:
        LocalFileService.delete_file(file_id)
        return {"message": "File deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
