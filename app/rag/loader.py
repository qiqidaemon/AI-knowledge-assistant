import os


def load_documents(path="knowledge"):
    documents=[]
    for filename in os.listdir(path):
        filepath=os.path.join(
            path,
            filename
        )
        if filename.endswith(".txt"):
            with open(filepath,"r",encoding="utf-8") as f:
                content=f.read()
                documents.append(
                    {
                        "text":content,
                        "source":filename
                    }
                )
    return documents