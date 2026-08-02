from sentence_transformers import SentenceTransformer

model=SentenceTransformer(
    "BAAI/bge-small-zh-v1.5"
)

def embedding_text(text:str):
    vector=model.encode(
        text
    )
    return vector.tolist()