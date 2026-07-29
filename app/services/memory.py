from typing import Dict,List

chat_history:Dict[str,List[dict]]={}

def get_history(
        conversation_id:str
):
    return chat_history.get(
        conversation_id,
        []
    )

def add_message(
        conversation_id:str,
        role:str,
        content:str
):
    if conversation_id not in chat_history:
        chat_history[conversation_id]=[]
    chat_history[conversation_id].append(
        {
            "role":role,
            "content":content
        }
    )