from pydantic import BaseModel
from typing import Literal

class IntentResult(BaseModel):
    intent:Literal[
                "rag",
                "tool,"
                "chat"
                ]
    reson: str