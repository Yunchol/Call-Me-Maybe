from llm_sdk import Small_LLM_Model
import json


# モデルは1回だけ作る（超重要）
_model = Small_LLM_Model()


def get_logits(input_ids):
    """
    input_ids に対する次トークンの logits を返す
    """
    return _model.get_logits_from_input_ids(input_ids)


def load_vocab():
    """
    token_id -> token文字列 の辞書を読む
    """
    vocab_path = _model.get_path_to_vocabulary_json()
    with open(vocab_path, "r", encoding="utf-8") as f:
        return json.load(f)
