import json
from pathlib import Path


def load_json_file(path: Path):
    """
    JSONファイルを読む。
    壊れてたら None を返す。
    """
    if not path.exists():
        print(f"[ERROR] ファイルが存在しません: {path}")
        return None

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSONの形式が壊れています: {path}")
        print(f"        {e}")
        return None
    except Exception as e:
        print(f"[ERROR] ファイル読み込み失敗: {path}")
        print(f"        {e}")
        return None
