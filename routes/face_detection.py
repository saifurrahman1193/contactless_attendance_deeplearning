from fastapi import APIRouter, HTTPException, Request, status
from typing import List
from controllers.face_detection_controller import handle_face_detection

router = APIRouter()

@router.get(
    "/operator-usage-forecasting", status_code=status.HTTP_200_OK
)
async def face_detection():
    try:
        return await handle_face_detection()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
