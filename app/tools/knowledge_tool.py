from app.rag.retriever import search_knowledge
from app.rag.context import build_rag_context

def search_knowledge_tool(query:str):
    knowledge=search_knowledge(query)

    if not knowledge:
        return {
            "context": "知识库中没有找到相关信息",
            "sources":[]

        }

    context,sources=build_rag_context(knowledge)

    result={
        "context": context,
        "sources" : sources
    }

    return result