# vector-search-util

## 概要

- ベクトル検索の類似度を検証するツール


## 環境構築

### windows

```cmd
python -m venv venv
source venv\Script\activate
make deps
```

### linux

```bash
python -m venv venv
source venv/bin/activate
make deps
```

## 使い方

### ローカルのエンべティングモデルを使う場合


- 事前準備として下記のような設定にする
  - ※`sentence_transformers_model`は[Hugging FaceのEmbeddings](https://huggingface.co/models?other=embeddings)からモデルを探して指定することも可能

```yaml
#config/config.yaml
embedding_model:
  type: "sentence-transformers"
  sentence_transformers_model: "intfloat/multilingual-e5-base"
```

```cmd
# モデルをローカルにダウンロードする
make get-model

# ツールを実行
make run
```

### OpenAIのエンべティングモデルを使う場合

※未実装


## エンべティングモデルの置き場

- sentence_transformerライブラリが用意しているオリジナルのモデル
  - [https://sbert.net/docs/sentence_transformer/pretrained_models.html#original-models]
- Hugging Face hub： AI開発・機械学習のためのプラットフォーム
  - [https://huggingface.co/models?other=embeddings]