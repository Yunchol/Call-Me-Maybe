from pathlib import Path
from src.parser import load_function_definitions
from src.selector import choose_fn_name
from src.args import fill_args
from src.models import FunctionCallResult


def run_step11(prompt: str) -> FunctionCallResult:
    functions = load_function_definitions(
        Path("data/exercise_input")
    )

    # 1. fn_name を選ぶ
    fn_name = choose_fn_name(prompt, functions)

    # 2. 定義を取得
    fn_def = next(f for f in functions if f.fn_name == fn_name)

    # 3. args を埋める
    args = fill_args(prompt, fn_def)

    return FunctionCallResult(
        prompt=prompt,
        fn_name=fn_name,
        args=args,
    )
