from pathlib import Path
from src.parser import load_function_calling_tests, load_function_definitions


def main():
    base_dir = Path("data/exercise_input")

    tests = load_function_calling_tests(base_dir)
    functions = load_function_definitions(base_dir)

    if tests is None or functions is None:
        print("[FATAL] 入力ファイルの読み込みに失敗しました")
        return

    print("[OK] 入力ファイルを読み込みました")
    print(f"tests type: {type(tests)}")
    print(f"functions type: {type(functions)}")


if __name__ == "__main__":
    main()
