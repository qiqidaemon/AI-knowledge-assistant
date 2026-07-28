from fastapi import APIRouter,HTTPException
from app.schemas.chat import ChatRequest,ChatResponse
from app.services.llm import ask_llm_stream
from fastapi.responses import StreamingResponse

router=APIRouter()

@router.post("/chat",response_model=ChatResponse)
def chat(request:ChatRequest):
    try:
        answer=ask_llm_stream(request.question)
        return StreamingResponse(
            ask_llm_stream(request.question),
            media_type="text/event-stream"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
