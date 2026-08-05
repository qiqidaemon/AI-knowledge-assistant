from app.rag.embedding import embedding_text
from app.rag.vector_store import collection
from app.core.logger import logger
distance_threshold=0.8
def search_knowledge(
        query:str,
        top_k:int=1
):

    query_embedding=embedding_text(
        query
    )
    results=collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k,

        


    )
    logger.info(
        f"Rag query :{query}"
    )
    logger.info(
        f"Rag result :{results}"
    )
   
    documents=results["documents"][0]
    metadatas=results["metadatas"][0]
    distance=results["distances"][0]
    
    knowledge=[]
    for doc,meta,dis in zip(
        documents,metadatas,distance
    ):  
        if dis>distance_threshold:
            pass
        else:
            knowledge.append(
            {
            "content":doc,
            "source":meta.get("source"),
            "chunk":meta.get("chunk"),
            "distance":dis
            

        }
        )
    return knowledge