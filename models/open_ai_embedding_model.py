import openai
from . import EmbeddingModel

class OpenAIEmbeddingModel(EmbeddingModel):
    def __init__(self, api_key: str, model_name: str = "text-embedding-ada-002"):
        openai.api_key = api_key
        self.model_name = model_name

    def generate_embedding(self, text: str) -> list:
        response = openai.Embedding.create(
            input=text,
            model=self.model_name
        )
        return response["data"][0]["embedding"]
