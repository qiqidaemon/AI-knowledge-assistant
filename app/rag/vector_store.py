import chromadb

client=chromadb.PersistentClient(
    path="./chroma"
)

collection=client.get_or_create_collection(
    name="knowledge"
)

def add_document(
        doc_id:str,text:str,embedding:list,metadata:dict
):
    collection.upsert(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata]
    )