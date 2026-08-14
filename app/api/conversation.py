from fastapi import APIRouter
import uuid
from app.schemas.chat import MessageResponse
from app.services.db_service import (get_message,
                                     create_conversation_record
)
router=APIRouter()

@router.post("/conversation")

def create_conversation():
    conversation_id=str(uuid.uuid4())
    conversation=create_conversation_record(conversation_id)
    return {
        "conversation_id":conversation.id,
        "title":conversation.title,
        "created_at":conversation.created_at
    }

@router.get("/conversation{conversation_id}/messages",
            response_model=list[MessageResponse])

def conversation_messages(
    conversation_id:str
):
    messages=get_message(
        conversation_id
    )
    return messages