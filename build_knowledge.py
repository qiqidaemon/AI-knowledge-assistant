from app.rag.loader import load_documents
from app.rag.embedding import embedding_text
from app.rag.vector_store import add_document

documents=load_documents()

for index,doc in enumerate(documents):
    vector=embedding_text(
        doc["text"]
    )
    add_document(
        doc_id=doc["source"],
        text=doc["text"],
        embedding=vector,
        metadata={
            "source":doc["source"]
        }

    )
    print(f"Added {doc["source"]}")