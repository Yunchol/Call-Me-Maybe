from pathlib import Path
from src.parser import load_function_definitions


def main():
    base_dir = Path("data/exercise_input")
    functions = load_function_definitions(base_dir)

    if functions is None:
        print("[FATAL] 読み込み失敗")
        return

    f = functions[0]
    print("fn_name:", f.fn_name)
    print("args_names:", f.args_names)
    print("args_types:", f.args_types)
    print("return_type:", f.return_type)


if __name__ == "__main__":
    main()
