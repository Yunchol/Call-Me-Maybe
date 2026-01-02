from typing import List
from src.models import FunctionDefinition
from src.llm_wrapper import get_logits
from transformers import AutoTokenizer

# tokenizer は llm_sdk の中のものを流用してもOKだが
# Step11では「文字 → token_id」を使うため明示する
from llm_sdk import Small_LLM_Model

_model = Small_LLM_Model()
_tokenizer = _model._tokenizer


def score_candidate(prompt: str, candidate: str) -> float:
    """
    prompt の続きとして candidate 全体が
    どれくらい自然かをスコア化する
    """
    # prompt + 改行 + candidate を 1 本の入力にする
    text = prompt + "\n" + candidate
    input_ids = _tokenizer.encode(text, add_special_tokens=False)

    # 各位置の logits を取りたいので
    # candidate が始まる位置を覚える
    prompt_ids = _tokenizer.encode(prompt + "\n", add_special_tokens=False)
    start = len(prompt_ids)

    score = 0.0

    # candidate の各トークンについて
    for i in range(start, len(input_ids)):
        # i-1 までが入力、i が「次トークン」
        logits = get_logits(input_ids[:i])
        token_id = input_ids[i]

        score += logits[token_id]

    return score



def choose_fn_name(
    prompt: str,
    functions: List[FunctionDefinition]
) -> str:
    """
    functions の中から最も自然な fn_name を選ぶ
    """
    scores = {}

    for f in functions:
        score = score_candidate(prompt, f.fn_name)
        scores[f.fn_name] = score

    # 一番スコアが高いものを選ぶ
    return max(scores, key=scores.get)
