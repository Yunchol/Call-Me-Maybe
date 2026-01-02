# 全体ロードマップ（Step 0〜12）

## Step 0: ゴールの再確認

**目的**：prompt（自然文）→ `fn_name` と `args` のJSONに変換して保存
**学ぶこと**：要件整理、入出力仕様の読み取り

**完了条件**

* 出力JSONのキーが `prompt / fn_name / args` の3つだけだと理解して説明できる

---

## Step 1: プロジェクト骨格を作る

**やること**

* `src/`, `data/input/`, `data/output/` を作る
* `uv` で環境作成（numpy, pydantic）
* `.gitignore`, Makefile の雛形

**学ぶこと**

* 42系の提出物の整え方
* uv / pyproject / 実行入口（`python -m src`）

**完了条件**

* `uv run python -m src` が動く（まだ何もしなくてOK）

---

## Step 2: “正しい出力形式”を pydantic で固定する（最重要の土台）

**やること**

* `FunctionCallResult(prompt, fn_name, args)` を BaseModel で定義
* JSON書き出しをこのModel経由にする

**学ぶこと**

* schema（型・必須キー）でバグを潰す発想
* 「壊れない出力」を先に固める設計

**完了条件**

* ダミーでもいいから、指定schemaの配列JSONを出せる

---

## Step 3: 入力ファイル読み込み（壊れてても落ちない）

**やること**

* `function_calling_tests.json` と `function_definitions.json` を読む
* ファイル無い/JSON壊れてる/型違う時のエラー文を整える

**学ぶこと**

* 例外設計（落ちない、分かるエラー）
* “入力は信用しない”基本

**完了条件**

* 入力が壊れててもクラッシュせずに終了できる

---

## Step 4: function_definitions を pydantic でモデル化

**やること**

* FunctionDefinition（name, description, parameters, returns）をモデル化
* parameter型（number/string/boolean…）を内部表現にする

**学ぶこと**

* “LLMの前に”データ構造を整える
* 型の扱い（number→float など）

**完了条件**

* 定義ファイルを読み込んで、Pythonのオブジェクトとして扱える

---

## Step 5: まずは「関数選択」だけ作る（LLMなしの仮実装）

**やること**

* とりあえず常に先頭の関数を返す、などの仮実装
* 出力の形だけ正しくする

**学ぶこと**

* 複雑な部分を後回しにして“流れ”を完成させる

**完了条件**

* 全promptに対して、必ず何かしらの `fn_name` を出力できる

---

## Step 6: まずは「引数抽出」だけ作る（LLMなしの仮実装）

**やること**

* args を空で出す／固定値を入れる（仮）
* pydanticで型を強制

**学ぶこと**

* 引数の必須/任意の違い
* “型が合う”の意味

**完了条件**

* schema通りの args object を常に出せる（中身は仮でOK）

---

# ここまでで「入出力が完成」。ここからLLMに入る

## Step 7: llm_sdk を触って「1トークンのlogits」を取る

**やること**

* `get_logits_from_input_ids` を呼んでlogitsが返ることを確認
* `get_path_to_vocabulary_json` を読み込んで token_id→文字列を見れるようにする

**学ぶこと**

* LLMの生成が「1トークンずつ」な理由
* logits / vocab の意味

**完了条件**

* 任意の input_ids に対して logits が取れる
* vocabで token_id を文字に変換できる

---

## Step 8: constrained decoding の最小実装（JSONじゃなくてOK）

**やること**

* “許可トークン集合”だけで生成する練習
* 例： `"hello"` を許可トークンだけで出せるようにする

**学ぶこと**

* 「出力を制御する」ってどういうことか
* マスク（logitsを -∞）の作り方

**完了条件**

* 許可したトークン以外が絶対に出ない生成ができる

---

## Step 9: JSONの構造制約（JSONとして壊れない）

**やること**

* `{` → `"` → `prompt` → `"` → `:` → …みたいに
* “今どんな文字が許されるか”を状態（state）で管理

**学ぶこと**

* JSONを状態機械として扱う考え方
* 文字列/数値/区切りの制御

**完了条件**

* “必ずパースできるJSON”を生成できる（内容は仮でも）

---

## Step 10: schema制約（fn_nameとargsが定義に一致）

**やること**

* `fn_name` は function_definitions の name からしか選べない
* args のキーも型も definitions と一致させる

**学ぶこと**

* 「JSONが正しい」≠「仕様が正しい」
* 候補集合からの選択を強制する

**完了条件**

* 出力が常に “schema準拠” になる

---

## Step 11: “正確さ”を上げる（関数選択・引数抽出の品質）

**やること**

* 関数選択用のプロンプト設計（ただし最終出力は制約生成）
* args抽出の戦略：一発生成 or 段階生成（例：先にfn_name確定→次にargs）

**学ぶこと**

* 小さいモデルで精度を上げる分解の仕方
* 失敗時のリカバリ（別案の生成、再トライ方針）

**完了条件**

* ざっくり95%程度を目指す手応えが出る

---

## Step 12: 仕上げ（性能・テスト・README）

**やること**

* エッジケース（空文字、引用符、数字、特殊文字）
* 速度（prompt数多い時に遅すぎない）
* README（アルゴリズム説明、設計、テスト、課題、学び）

**学ぶこと**

* “動く”から“評価で通る”への仕上げ方
* 説明責任（なぜそうしたか）

**完了条件**

* `uv run python -m src` 一発で通る
* READMEで質問に答えられる

---

# 進捗チェック（今どこ？が分かるチェックリスト）

* [ ] Step2：ダミーでも正しい形の出力JSONが出る
* [ ] Step3：入力壊れてても落ちない
* [ ] Step7：logitsとvocabが読める
* [ ] Step9：壊れないJSONを制約生成できる
* [ ] Step10：schema準拠100%
* [ ] Step12：READMEとテスト



attachments_project_ai/
├── pyproject.toml        # uv / 依存関係
├── uv.lock               # 依存の確定版（自動生成）
├── .venv/                # 仮想環境（gitignore）
│
├── llm_sdk/              # 42提供（触らない）
│   └── __init__.py
│
├── data/
│   └── exercise_input/
│       ├── function_calling_tests.json
│       └── functions_definition.json
│
├── src/                  # ★あなたが書く本体
│   ├── __main__.py       # 実行入口
│   ├── io_utils.py       # 入出力処理
│   ├── models.py         # pydantic models
│   ├── parser.py         # input解析
│   ├── generator.py     # JSON生成（後でconstrained decoding）
│   └── llm_wrapper.py   # llm_sdkを使う層
│
├── README.md
└── .gitignore

