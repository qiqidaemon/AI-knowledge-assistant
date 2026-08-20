from fastapi import APIRouter,HTTPException
import uuid
from app.schemas.chat import MessageResponse
from app.services.db_service import (get_message,
                                     create_conversation_record,delete_conversation
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

@router.delete("/conversation/{conversation_id}")
def remove_conversation(
    conversation_id: str
):

    deleted_count = delete_conversation(
        conversation_id
    )

    if deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return {
        "message": "Conversation deleted successfully",
        "conversation_id": conversation_id
    }