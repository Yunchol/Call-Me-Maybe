from enum import Enum, auto


class JSONState(Enum):
    START = auto()
    OPEN_BRACE = auto()

    KEY_FN_NAME = auto()
    COLON = auto()
    FN_NAME_VALUE = auto()

    KEY_ARGS = auto()
    ARGS_OBJECT_START = auto()
    ARGS_KEY = auto()
    ARGS_COLON = auto()
    ARGS_VALUE = auto()
    ARGS_OBJECT_END = auto()

    CLOSE_BRACE = auto()
    END = auto()
