# uvicorn app.main:app --reload
from fastapi import FastAPI
from app.controller.UserController import router as user_router

app = FastAPI()

# Registrar rutas
app.include_router(user_router, prefix="/api/v1", tags=["users"])

@app.get("/")
def root():
    return {"message": "Welcome"}