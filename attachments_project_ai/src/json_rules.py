from typing import List, Optional
from src.json_state import JSONState
from src.models import FunctionDefinition


def allowed_strings(
    state: JSONState,
    functions: List[FunctionDefinition],
    selected_fn: Optional[str] = None,
) -> List[str]:
    """
    今の JSONState において「出していい文字列」を返す
    """

    # { 
    if state == JSONState.START:
        return ["{"]

    # "fn_name"
    if state == JSONState.KEY_FN_NAME:
        return ['"fn_name"']

    # :
    if state in (
        JSONState.COLON,
        JSONState.ARGS_COLON,
    ):
        return [":"]

    # fn_name の値（定義ファイルからのみ）
    if state == JSONState.FN_NAME_VALUE:
        return [f'"{f.fn_name}"' for f in functions]

    # "args"
    if state == JSONState.KEY_ARGS:
        return ['"args"']

    # {
    if state == JSONState.ARGS_OBJECT_START:
        return ["{"]

    # args のキー（選ばれた fn_name に対応）
    if state == JSONState.ARGS_KEY:
        if selected_fn is None:
            return []

        for f in functions:
            if f.fn_name == selected_fn:
                return [f'"{name}"' for name in f.args_names]

        return []

    # args の値（Step10ではダミー）
    if state == JSONState.ARGS_VALUE:
        # 型はまだ見ない（Step11）
        return ["0"]

    # }
    if state in (
        JSONState.ARGS_OBJECT_END,
        JSONState.CLOSE_BRACE,
    ):
        return ["}"]

    return []
