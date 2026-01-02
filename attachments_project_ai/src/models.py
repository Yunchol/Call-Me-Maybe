from pydantic import BaseModel
from typing import Dict, Any


class FunctionCallResult(BaseModel):
    prompt: str
    fn_name: str
    args: Dict[str, Any]
