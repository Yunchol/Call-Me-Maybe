from pathlib import Path
from src.parser import load_function_definitions
from src.schema_rules import allowed_fn_names, allowed_args_keys


def main():
    functions = load_function_definitions(Path("data/exercise_input"))

    print("allowed fn_name:", allowed_fn_names(functions))
    print("args for fn_add_numbers:",
          allowed_args_keys(functions, "fn_add_numbers"))


if __name__ == "__main__":
    main()
