from pydantic import BaseModel
from typing import List, Union

class OperatorUsageForecastRequest(BaseModel):
    operator_id: int
    last_n_days_dataset_input: List[Union[int, float, str]]
