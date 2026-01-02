from pathlib import Path
from src.io_utils import load_json_file


def load_function_calling_tests(base_dir: Path):
    path = base_dir / "function_calling_tests.json"
    return load_json_file(path)


def load_function_definitions(base_dir: Path):
    path = base_dir / "functions_definition.json"
    return load_json_file(path)
