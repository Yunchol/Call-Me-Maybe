from src.json_state import JSONState
from src.json_rules import allowed_strings
from src.json_fsm import next_state


def main():
    state = JSONState.START
    output = []

    print("=== Step9: JSON State Machine Test ===")

    while state != JSONState.END:
        allowed = allowed_strings(state)

        print(f"state: {state}")
        print(f"allowed: {allowed}")

        if not allowed:
            print("no allowed output, stop")
            break

        # 今は「必ず最初の候補を出す」だけ
        token = allowed[0]
        output.append(token)

        state = next_state(state)

    print("\nresult:")
    print("".join(output))


if __name__ == "__main__":
    main()
