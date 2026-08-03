from fastapi import APIRouter,HTTPException
from app.schemas.chat import ChatRequest,ChatResponse
from app.services.llm import ask_llm
from fastapi.responses import StreamingResponse
from app.core.logger import logger
import uuid

router=APIRouter()

@router.post("/chat")
def chat(request:ChatRequest):
    
    logger.info(
        "Received chat request"
    )
    try:
        answer=ask_llm(
            request.question,
            request.conversation_id
        )
        print(f"we get the answer there {answer}")
        return {
            "answer":answer
        }
    except Exception as e:
        logger.error(f"Chat failed:{str(e)}",exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
