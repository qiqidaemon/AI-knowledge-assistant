from app.router.intent import classify_intent
from app.rag.retriever import search_knowledge
from app.router.llm_router import llm_route

answer=llm_route("我想获得alan的身高")
print(answer)