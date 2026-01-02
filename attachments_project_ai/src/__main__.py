from src.llm_wrapper import get_logits, load_vocab


def main():
    #「入力が [1, 2, 3] のとき、次に来そうなトークンは何だろう？」
    logits = get_logits([1, 2, 3])
    print("logits length:", len(logits))
    print("first 5 logits:", logits[:5])

    vocab = load_vocab()
    print("token 0:", vocab.get("hello"))
    print("token 1:", vocab.get("1"))


if __name__ == "__main__":
    main()
