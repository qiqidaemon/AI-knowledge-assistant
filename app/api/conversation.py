from fastapi import APIRouter
import uuid
from app.schemas.chat import MessageResponse
from app.services.db_service import get_message

router=APIRouter()

@router.post("/conversation")

def create_conversation():
    conversation_id=str(uuid.uuid4())
    return {
        "conversation_id":conversation_id
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