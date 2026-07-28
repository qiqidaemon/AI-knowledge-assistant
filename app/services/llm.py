from openai import OpenAI
from app.core.config import settings
from app.core.prompts import SYSTEM_PROMPT

client=OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url= "https://api.deepseek.com"

)

def ask_llm_stream(question:str)->str:
    response=client.chat.completions.create(
        model=settings.MODEL_NAME,
        stream=True,
        messages=[
           { "role":"system",
            "content":SYSTEM_PROMPT
           },
           {
               "role":"user",
                "content":question
           }
        ]
    )

    for chunk in response:
        content=chunk.choices[0].delta.content
        if content:
            yield content
   