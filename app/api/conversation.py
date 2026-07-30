from fastapi import APIRouter
import uuid

router=APIRouter()

@router.post("/conversation")

def create_conversation():
    conversation_id=str(uuid.uuid4())
    return {
        "conversation_id":conversation_id
    }