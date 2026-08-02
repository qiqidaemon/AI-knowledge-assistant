from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEEPSEEK_API_KEY:str
    MODEL_NAME:str="deepseek-chat"
    REDIS_HOST:str="redis"
    REDIS_PORT:int=6379
    DATABASE_URL:str="postgresql://alan:123456@localhost:5432/ai_assistant"

    class Config:
        env_file=".env"

settings=Settings()

