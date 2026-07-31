from app.core.database import SessionLocal
from app.models.message import Message

def save_message(
        conversation_id:str,
        role:str,
        content:str
):
    db=SessionLocal()
    try:
        message=Message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )
        db.add(message)
        db.commit()
    finally:
        db.close()