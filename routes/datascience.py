from fastapi import APIRouter, HTTPException, Request, status
from typing import List
from schemas.datascience import OperatorUsageForecastRequest
from controllers.datascience_controller import handle_operator_usage_forecasting

router = APIRouter()

@router.post(
    "/operator-usage-forecasting", status_code=status.HTTP_200_OK
)
async def operator_usage_forecasting(requests: List[OperatorUsageForecastRequest]):
    try:
        return await handle_operator_usage_forecasting(requests)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
