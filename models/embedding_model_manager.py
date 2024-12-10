
from . import EmbeddingModel, SentenceTransformersEmbeddingModel, OpenAIEmbeddingModel
from huggingface_hub import snapshot_download

class EmbeddingModelManager:
    base_path = "models/local_models/"

    @classmethod
    def get_embedding_model(cls, config: dict) -> EmbeddingModel:
        model_type = config["embedding_model"]["type"]
        if model_type == "sentence-transformers":
            model_path = config["embedding_model"]["sentence_transformers"]["model_name"]
            return SentenceTransformersEmbeddingModel(
                model_path = cls.base_path + model_path
            )
        elif model_type == "openai":
            return OpenAIEmbeddingModel(
                api_key=config["embedding_model"]["openai"]["api_key"],
                model_name=config["embedding_model"]["openai"]["model_name"]
            )
        else:
            raise ValueError(f"Unknown model type: {model_type}")

    @classmethod
    def download_embedding_model(cls, config: dict):
        """
        エンべティングモデルをHuggingFace Hubからダウンロードする
        注意：必ずルートディレクトリから実行すること
        """
        model_name = config["embedding_model"]["sentence_transformers"]["model_name"]
        model_path = cls.base_path + model_name
        snapshot_download(model_name, local_dir=model_path)
