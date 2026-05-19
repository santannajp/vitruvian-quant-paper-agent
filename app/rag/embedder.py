# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer

model =SentenceTransformer(
    'BAAI/bge-small-en'
    )

def embed(texts:str):
    return model.encode(texts).tolist()