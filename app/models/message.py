
from sqlalchemy import Column,String,Integer,Text,DateTime,ForeignKey
from datetime import datetime,timezone
from sqlalchemy.orm import DeclarativeBase,relationship


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
    messages=relationship(
        "Message",
        back_populates="conversation",
        cascade="all,delete-orphan",
        passive_deletes=True

    )

class Message(Base):
    __tablename__="messages"

    id=Column(
        Integer,
        primary_key=True
    )
    conversation_id=Column(
        String,
        ForeignKey("conversations.id",ondelete="CASCADE"),
        nullable=False,
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
    conversation=relationship(
        "Conversation",
        back_populates="messages"
    )