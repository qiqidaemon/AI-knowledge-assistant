from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,String,Integer,Text,DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass

class Message(Base):
    __tablename__="messages"

    id=Column(
        Integer,
        primary_key=True
    )
    conversation_id=Column(
        String,
        index=True
    )
    role=Column(
        String
    )
    content=Column(
        Text
    )
    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )