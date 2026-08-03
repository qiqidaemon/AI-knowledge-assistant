from app.rag.retriever import search_knowledge


result = search_knowledge(
    "介绍一下alan的信息"
)

for item in result:
    print("__________")
    print(item)