from app.rag.embedding import embedding_text
from app.rag.vector_store import collection

def search_knowledge(
        query:str,
        top_k:int=3
):

    query_embedding=embedding_text(
        query
    )
    results=collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k

    )
    documents=results["documents"][0]
    return documents