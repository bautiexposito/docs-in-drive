# uvicorn app.main:app --reload
import sys
import os
from fastapi import FastAPI
from app.controller.user_controller import router as user_router
from app.controller.local_file_controller import router as localFile_router
from app.controller.drive_file_controller import router as driveFile_router

app = FastAPI()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
app.include_router(localFile_router, prefix="/api/v1/local_files", tags=["localFiles"])
app.include_router(driveFile_router, prefix="/api/v1/drive", tags=["driveFiles"])

@app.get("/")
def root():
    return {"message": "Welcome"}
