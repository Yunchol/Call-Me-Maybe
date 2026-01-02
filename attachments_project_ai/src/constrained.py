from typing import List, Set


def apply_constraints(
    logits: List[float],
    allowed_token_ids: Set[int]
) -> List[float]:
    """
    allowed_token_ids に含まれないトークンは
    絶対に選ばれないようにする
    """
    masked_logits = []

    for token_id, score in enumerate(logits):
        if token_id in allowed_token_ids:
            masked_logits.append(score)
        else:
            masked_logits.append(-1e9)  # 実質 -∞

    return masked_logits
