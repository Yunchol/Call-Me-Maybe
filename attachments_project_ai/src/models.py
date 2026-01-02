from pydantic import BaseModel
from typing import Dict, Any, List


class FunctionCallResult(BaseModel):
    prompt: str
    fn_name: str
    args: Dict[str, Any]


class ParameterDefinition(BaseModel):
    type: str
    description: str


class FunctionDefinition(BaseModel):
    fn_name: str
    args_names: List[str]
    args_types: Dict[str, str]
    return_type: str