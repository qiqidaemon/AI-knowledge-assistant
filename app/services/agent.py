import json

from app.services.memory import get_history
from app.router.llm_router import llm_route
from app.rag.retriever import search_knowledge
from app.rag.context import build_rag_context

from app.tools.executor import execute_tools
from app.services.llm  import call_llm

from app.core.prompts import SYSTEM_PROMPT

from app.core.logger import logger

def run_agent(
        question:str,
        conversation_id:str
):
    history=get_history(conversation_id)
    router_result=llm_route(question)
    router_result=json.loads(router_result)
    intent=router_result["intent"]
    logger.info(f"Intent:  {intent}")
    context=""
    source=[]
    tool_result=None

    if intent=="rag":
        knowledge=search_knowledge(question)
        logger.info(f"Rag result :{knowledge}")
        context,source=build_rag_context(knowledge)
    elif intent=="tool":
        tool_result=execute_tools("get_current_time")

    messages=[
        {
            "role":"system",
            "content":SYSTEM_PROMPT
     }
    ]

    if context:
        messages.append(
{
"role":"system",
"content":f"""
知识库信息：
{context}
请根据知识库回答。
"""


}
        )
    if tool_result:
        messages.append({
            "role":"system",
            "content":f"""
工具返回：
{tool_result}
请根据结果回答。
"""
        }
        )

    messages.extend(
        history
    )
    answer=call_llm(messages)

    if source :
        answer+="\n\n参考来源:\n"
        for s in source:
            answer+=(
                f"-{s['source']}\n"
            )
    return answer