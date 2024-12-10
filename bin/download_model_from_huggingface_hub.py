from config import Config
from models import EmbeddingModelManager

def main():
    config: dict = Config.load_config()
    EmbeddingModelManager.download_embedding_model(config)
    pass

if __name__ == "__main__":
    main()