from typing import Dict,List
import json
from app.core.redis import redis_client
Max_history=3

def get_history(
        conversation_id:str
):
    key=f"chat:{conversation_id}"
    history=redis_client.get(key)
    if history:
        history=json.loads(history)
        return history[-Max_history:]
    return []

def add_message(
        conversation_id:str,
        role:str,
        content:str
):
    key=f"chat:{conversation_id}"
    history=get_history(
        conversation_id
    )
    history.append(
        {
            "role":role,
            "content":content
        }
    )
    history=history[-Max_history:]
    redis_client.set(
        key,
        json.dumps(
            history,
            ensure_ascii=False
        ),
        ex=60*60*24*7
    )