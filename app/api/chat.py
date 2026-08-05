from fastapi import APIRouter,HTTPException
from app.schemas.chat import ChatRequest,ChatResponse
from app.services.agent import run_agent
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
        question=request.question
        answer=run_agent(
            question,
            request.conversation_id
        )
        print(f"the question is {question} ")
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
