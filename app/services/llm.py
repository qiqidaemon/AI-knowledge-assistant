import json
import time
from openai import OpenAI
from app.core.config import settings
from app.core.prompts import SYSTEM_PROMPT
from app.core.logger import logger
from app.services.memory import get_history
from app.services.memory import add_message
client=OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url= "https://api.deepseek.com"

)
def ask_llm_stream(question: str,conversation_id:str):
    

    start_time = time.time()
    history=get_history(conversation_id)
    full_answer=""
    
    messages=[
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        }
    ]
    messages.extend(history)
    messages.append({
        "role":"user",
        "content":question
    })
    add_message(
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
            stream=True,
            messages=messages
        )


        logger.info(
            f"Using model:{settings.MODEL_NAME}"
        )


        for chunk in response:

            content = chunk.choices[0].delta.content

            if content:
                full_answer+=content

                data = {
                    "content": content,
                    "finish": False
                }

                yield f"data:{json.dumps(data,ensure_ascii=False)}\n\n"
        add_message(
            conversation_id,
            "assistant",
            full_answer
        )


    except Exception as e:

        logger.error(
            f"LLM request failed: {str(e)}"
        )

        error_data = {
            "content": "AI服务暂时不可用,请稍后重试",
            "finish": True,
            "error": True
        }

        yield f"data:{json.dumps(error_data,ensure_ascii=False)}\n\n"


    finally:

        latency = time.time() - start_time

        logger.info(
            f"Request finished | latency={latency:.2f}s"
        )