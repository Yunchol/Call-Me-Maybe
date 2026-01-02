from pathlib import Path
from src.parser import load_function_calling_tests, load_function_definitions
from src.generator import generate_function_call


def main():
    base_dir = Path("data/exercise_input")

    tests = load_function_calling_tests(base_dir)
    functions = load_function_definitions(base_dir)

    if tests is None or functions is None:
        print("[FATAL] 入力ファイルの読み込みに失敗しました")
        return

    # テストの先頭だけ使う（今は十分）
    prompt = tests[0]["prompt"]

    result = generate_function_call(prompt, functions)

    print(result.model_dump())


if __name__ == "__main__":
    main()
