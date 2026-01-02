from typing import List
from src.models import FunctionDefinition, FunctionCallResult


def generate_function_call(prompt: str, functions: List[FunctionDefinition]) -> FunctionCallResult:
    """
    仮実装：
    常に先頭の関数を選ぶ
    """
    selected_fn = functions[0]

    return FunctionCallResult(
        prompt=prompt,
        fn_name=selected_fn.fn_name,
        args={}  # Step6で埋める
    )
