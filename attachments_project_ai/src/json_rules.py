from src.json_state import JSONState


def allowed_strings(state: JSONState):
    """
    今の状態で出していい「文字列」の集合
    """
    if state == JSONState.START:
        return ["{"]

    if state == JSONState.OPEN_BRACE:
        return ['"']

    if state == JSONState.KEY_PROMPT:
        return ["prompt"]

    if state == JSONState.COLON:
        return [":"]

    if state == JSONState.STRING_VALUE:
        return ["hi"]  # 今は固定でOK（仮）

    if state == JSONState.CLOSE_BRACE:
        return ["}"]

    return []
