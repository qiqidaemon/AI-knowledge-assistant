from app.rag.vector_store import collection


result = collection.get()


print(result["ids"])