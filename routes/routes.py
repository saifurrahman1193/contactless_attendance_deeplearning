from fastapi import APIRouter, FastAPI, Request
from routes import datascience

router = APIRouter()

@router.get("/")
async def root(request: Request):
    return {"message": "Successfully Run!"}

def register_routes(app: FastAPI):
    app.include_router(router, prefix="") 
    app.include_router(datascience.router, prefix="/api/ds")


# [{"operator_id": 1, "last_n_days_dataset_input": [0, 0, 0, 0, 0, "2", 0]}]