from openai import OpenAI
from app.core.config import settings

client=OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

def llm_route(question:str):
    prompt=f"""
你是一个任务分类器。
判断用户问题属于哪一类：
rag:
需要查询知识库的问题

tool:
需要调用工具的问题

chat:
普通聊天

用户问题：
{question}

只返回JSON:
{{
"intent":"",
"reason":""
}}
"""
    response=client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]

    )
    return response.choices[0].message.content