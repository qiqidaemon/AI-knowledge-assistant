from app.core.database import SessionLocal

from app.models.message import Message
from app.models.message import Conversation,Message


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

def get_message(conversation_id:str):
    db=SessionLocal()
    try:
        messages=(db.query(Message).
                  filter(Message.conversation_id==conversation_id).
                  order_by(Message.created_at).
                  all())
        return messages
    finally:
        db.close()

def create_conversation_record(conversation_id : str):
    db=SessionLocal()
    try:
        conversation=Conversation(id=conversation_id,
                                  title="新对话")
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        return conversation
    finally:
        db.close()




def delete_conversation(
        conversation_id:str
):
    db=SessionLocal()

    try:
        db.query(Message).filter(
            Message.conversation_id == conversation_id
        ).delete()

        deleted_count=(
            db.query(Conversation).filter(
                 Conversation.id == conversation_id
            ).delete()
        )

        db.commit()

        return deleted_count

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

def get_conversations():
    db=SessionLocal()

    try:
        conversations=(
            db.query(Conversation).order_by(Conversation.updated_at.desc()).all()
        )
        return conversations
    finally:
        db.close()