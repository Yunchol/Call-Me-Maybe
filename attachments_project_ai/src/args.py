from typing import Dict
from src.models import FunctionDefinition
from src.llm_wrapper import get_logits
from llm_sdk import Small_LLM_Model

_model = Small_LLM_Model()
_tokenizer = _model._tokenizer


def generate_arg_value(
    prompt: str,
    fn_name: str,
    arg_name: str,
    arg_type: str,
) -> float:
    """
    1つの引数の値だけを LLM に決めさせる（簡易）
    """
    query = (
        f"Function: {fn_name}\n"
        f"Argument: {arg_name} ({arg_type})\n"
        f"User input: {prompt}\n"
        f"Value:"
    )

    input_ids = _tokenizer.encode(query, add_special_tokens=False)
    logits = get_logits(input_ids)

    # 数値トークンっぽいものを探す（超簡易）
    # Step11では精度より流れ重視
    for token_id in sorted(range(len(logits)), key=lambda i: logits[i], reverse=True):
        token = _tokenizer.decode([token_id])
        try:
            return float(token)
        except ValueError:
            continue

    return 0.0  # fallback


def fill_args(
    prompt: str,
    fn_def: FunctionDefinition
) -> Dict[str, float]:
    """
    fn_def に従って args を埋める
    """
    args = {}

    for name in fn_def.args_names:
        arg_type = fn_def.args_types[name]
        value = generate_arg_value(
            prompt,
            fn_def.fn_name,
            name,
            arg_type,
        )
        args[name] = value

    return args
