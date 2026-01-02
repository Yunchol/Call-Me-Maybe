from pathlib import Path
from typing import List
from src.io_utils import load_json_file
from src.models import FunctionDefinition


def load_function_calling_tests(base_dir: Path):
    path = base_dir / "function_calling_tests.json"
    return load_json_file(path)


def load_function_definitions(base_dir: Path) -> List[FunctionDefinition]:
    path = base_dir / "functions_definition.json"
    raw = load_json_file(path)

    if raw is None:
        return None

    try:
        return [FunctionDefinition(**item) for item in raw]
    except Exception as e:
        print("[ERROR] function_definitions の構造が不正です")
        print(e)
        return None
