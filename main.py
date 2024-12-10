from config import Config
from models import EmbeddingModel, EmbeddingModelManager

def main():
    config: dict = Config.load_config()
    embedding_model: EmbeddingModel = EmbeddingModelManager.get_embedding_model(config)
    pass

if __name__ == "__main__":
    print("f")
    # main()