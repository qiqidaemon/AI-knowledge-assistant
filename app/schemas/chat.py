from pydantic import BaseModel


class MessageResponse(BaseModel):
    role:str
    content:str
    class Config:
        from_attributes=True
class ChatRequest(BaseModel):
    question:str
    conversation_id:str
    
class ChatResponse(BaseModel):
    conversation_id:str
    answer:str