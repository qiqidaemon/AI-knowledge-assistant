from fastapi import FastAPI
from app.api import chat
from app.core.config import settings
app=FastAPI()
app.include_router(
    chat.router
)

@app.get("/")
def root():
    return {
        "message":"AI assistant is running"
        "version:0.1 2026.7.28"
    }

@app.get("/health")
def health_check():
    return {"status":"healthy"}

print(settings.MODEL_NAME)