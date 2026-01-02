from src.json_state import JSONState


def next_state(state: JSONState) -> JSONState:
    """
    トークンを1つ出した後、次の状態へ
    """
    if state == JSONState.START:
        return JSONState.OPEN_BRACE

    if state == JSONState.OPEN_BRACE:
        return JSONState.KEY_PROMPT

    if state == JSONState.KEY_PROMPT:
        return JSONState.COLON

    if state == JSONState.COLON:
        return JSONState.STRING_VALUE

    if state == JSONState.STRING_VALUE:
        return JSONState.CLOSE_BRACE

    if state == JSONState.CLOSE_BRACE:
        return JSONState.END

    return JSONState.END
