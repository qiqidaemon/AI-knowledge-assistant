import json
import time
from openai import OpenAI
from app.core.config import settings
from app.core.prompts import SYSTEM_PROMPT
from app.core.logger import logger
from app.services.memory import get_history
from app.tools import available_tools
from app.rag.retriever import search_knowledge


from app.services.db_service import save_message
client=OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url= "https://api.deepseek.com"

)

tools=[
    {
        "type":"function",
        "function":{
            "name":"get_current_time",
            "description":"获取当前时间",
            "parameters":{
                "type":"object",
                "properties":{}
            }
        }
    }
]
def ask_llm(question: str,conversation_id:str):
    

    start_time = time.time()
    history=get_history(conversation_id)
    knowledge=search_knowledge(
        question
    )
    full_answer=""
    context="\n".join(knowledge)
    messages=[
        {
            "role":"system",
            "content":
            SYSTEM_PROMPT
            +
            f"""
以下是知识库资料：
{context}
回答问题时请优先参考这些资料。
如果资料中没有答案,请明确说明。
"""
        }

    ]
    messages.extend(history)
    messages.append({
        "role":"user",
        "content":question
    })
    save_message(
            conversation_id,
            "user",
            question
        )

    logger.info(
        f"User question:{question}"
    )

    try:

        response = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=messages,
            tools=tools
        )


        logger.info(
            f"Using model:{settings.MODEL_NAME}"
        )

        message=response.choices[0].message
        print("MESSAGE:",message)
        print("TOOL CALLS:",message.tool_calls)
        if message.tool_calls:
            tool_call=message.tool_calls[0]
            function_name=tool_call.function.name
            function=available_tools[function_name]
            result=function()
            messages.append(
                message.model_dump()
            )
            messages.append(
                {
                    "role":"tool",
                    "tool_call_id":tool_call.id,
                    "content":result
                }
            )
            second_response=client.chat.completions.create(
                model=settings.MODEL_NAME,
                messages=messages
            )
            answer=second_response.choices[0].message.content
            print("Final answer",answer)

        else:
            answer=message.content
        full_answer+=answer

        
             
    
        save_message(
            conversation_id,
            "assistant",
            full_answer
        )
        
        return full_answer


    except Exception as e:

        logger.error(
            f"LLM request failed: {str(e)}"
        )

        error_data = {
            "content": "AI服务暂时不可用,请稍后重试",
            "finish": True,
            "error": True
        }

        


    finally:

        latency = time.time() - start_time

        logger.info(
            f"Request finished | latency={latency:.2f}s"
        )