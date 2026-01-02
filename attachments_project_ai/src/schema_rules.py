from typing import List, Set
from src.models import FunctionDefinition


def allowed_fn_names(functions: List[FunctionDefinition]) -> Set[str]:
    """
    定義ファイルにある fn_name だけを許可
    """
    return {f.fn_name for f in functions}

def allowed_args_keys(
    functions: List[FunctionDefinition],
    fn_name: str
) -> Set[str]:
    for f in functions:
        if f.fn_name == fn_name:
            return set(f.args_names)
    return set()
