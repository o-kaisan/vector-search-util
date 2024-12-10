from sentence_transformers import SentenceTransformer
from . import EmbeddingModel

class SentenceTransformersEmbeddingModel(EmbeddingModel):
    def __init__(self, model_path: str):
        self.model = SentenceTransformer(model_path)

    def generate_embedding(self, text: str) -> list:
        return self.model.encode(text).tolist()