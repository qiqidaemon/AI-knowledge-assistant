from typing import Literal

def classify_intent(
        question:str
)->Literal["rag","tool","chat"]:
    tool_keywords=[
        "几点",
        "时间",
        "现在时间"
    ]
    knwoledge_keywords=[
        "是什么",
        "介绍",
        "是谁",
        "什么是",
    ]
    for keyword in tool_keywords:
        if keyword in question:
            return "tool"
    for keyword in knwoledge_keywords:
        if keyword in question:
            return "rag"
    return "chat"