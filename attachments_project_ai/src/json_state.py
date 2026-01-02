from enum import Enum, auto


class JSONState(Enum):
    START = auto()
    OPEN_BRACE = auto()
    KEY_PROMPT = auto()
    COLON = auto()
    STRING_VALUE = auto()
    CLOSE_BRACE = auto()
    END = auto()
