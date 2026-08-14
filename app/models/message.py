from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,String,Integer,Text,DateTime
from datetime import datetime,timezone


class Base(DeclarativeBase):
    pass

class Conversation(Base):
    __tablename__="conversations"
    id = Column(
        String,
        primary_key=True
    )
    title=Column(
        String,
        default="新对话"
    )
    created_at=Column(
        DateTime,
        default=lambda :datetime.now(timezone.utc),
        nullable=False
    )
    updated_at=Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda :datetime.now(timezone.utc),
        nullable=False
    )

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
        default=lambda :datetime.now(timezone.utc)
    )