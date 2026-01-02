from src.pipeline import run_step11


def main():
    prompt = "add 2 and 5"
    result = run_step11(prompt)

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
