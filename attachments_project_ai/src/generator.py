
from typing import List, Any, Dict
from src.models import FunctionDefinition, FunctionCallResult


def generate_function_call(prompt: str, functions: List[FunctionDefinition]) -> FunctionCallResult:
    """
    仮実装：
    - 関数は先頭を選ぶ
    - args は引数名だけ揃えて None を入れる
    """
    selected_fn = functions[0]

    # 引数名だけを使って args を作る
    args: Dict[str, Any] = {}
    for name in selected_fn.args_names:
        args[name] = None

    return FunctionCallResult(
        prompt=prompt,
        fn_name=selected_fn.fn_name,
        args=args
    )
