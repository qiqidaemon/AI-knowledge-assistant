from app.rag.loader import load_documents
from app.rag.embedding import embedding_text
from app.rag.vector_store import add_document
from app.rag.splitter import split_text
import uuid

documents=load_documents()

for index,doc in enumerate(documents):
    chunks=split_text(doc["text"])
    for index,chunk in enumerate(chunks):
        vector=embedding_text(chunk)
        source=doc["source"]
        add_document(
           
            doc_id=f"{source}_{index}",
            text=chunk,
            embedding=vector,
            metadata={
                "source":source,
                "chunk":index
            }
        )