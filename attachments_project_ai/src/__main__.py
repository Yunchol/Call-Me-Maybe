from src.constrained import apply_constraints


def main():
    # 仮の logits（トークン5個の世界）
    logits = [2.0, 5.0, 1.0, 4.0, 3.0]

    # 出していいトークンID
    allowed = {0, 2}

    masked = apply_constraints(logits, allowed)

    print("original logits :", logits)
    print("masked logits   :", masked)

    # 実際に選ばれるトークン（最大値）
    chosen_token = max(range(len(masked)), key=lambda i: masked[i])
    print("chosen token id:", chosen_token)


if __name__ == "__main__":
    main()
