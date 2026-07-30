from app.core.database import engine
from app.models.message import Base

Base.metadata.create_all(
    bind=engine
)