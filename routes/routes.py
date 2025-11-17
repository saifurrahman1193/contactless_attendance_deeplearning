from fastapi import APIRouter, FastAPI, Request
from routes import face_detection

router = APIRouter()

@router.get("/")
async def root(request: Request):
    return {"message": "Successfully Run!"}

def register_routes(app: FastAPI):
    app.include_router(router, prefix="") 
    app.include_router(face_detection.router, prefix="/api/face-detection")