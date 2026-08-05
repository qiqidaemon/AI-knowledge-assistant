
from openai import OpenAI
from app.core.config import settings

from app.services.db_service import save_message
client=OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url= "https://api.deepseek.com"

)

def call_llm(messages):
    response=client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=messages
    )
    return response.choices[0].message.content