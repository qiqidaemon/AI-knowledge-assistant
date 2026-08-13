from fastapi import FastAPI
from app.api import chat
from app.core.config import settings
from app.api import conversation
from app.models.message import Base
from app.core.database import engine
app=FastAPI()
Base.metadata.create_all(
    bind=engine
)

app.include_router(
    chat.router
    
)
app.include_router(
    conversation.router
)

@app.get("/")
def root():
    return {
        "message":"AI assistant is running on   "
        "version:0.1 2026.7.28"
    }

@app.get("/health")
def health_check():
    return {"status":"healthy"}

print(settings.MODEL_NAME)