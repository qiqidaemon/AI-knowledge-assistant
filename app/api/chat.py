from fastapi import APIRouter,HTTPException
from app.schemas.chat import ChatRequest,ChatResponse
from app.services.llm import ask_llm_stream
from fastapi.responses import StreamingResponse
from app.core.logger import logger
import uuid

router=APIRouter()

@router.post("/chat")
def chat(request:ChatRequest):
    conversation_id=str(uuid.uuid4())
    logger.info(
        "Received chat request"
    )
    try:
        
        return StreamingResponse(
            ask_llm_stream(request.question,request.conversation_id),
            media_type="text/event-stream"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
