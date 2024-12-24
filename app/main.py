# uvicorn app.main:app --reload
from fastapi import FastAPI
from app.controller.user_controller import router as user_router
from app.controller.drive_file_controller import router as driveFile_router

app = FastAPI()

# Registrar rutas
app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
app.include_router(driveFile_router, prefix="/api/v1/files", tags=["driveFiles"])

@app.get("/")
def root():
    return {"message": "Welcome"}
