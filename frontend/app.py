import streamlit as sl
import requests

API_Base="http://api:8000"

sl.set_page_config(
    page_title="main page",
    page_icon="😊"
)

sl.title("AI knowledge Assistant version 0.7")

if "conversation_id" not in sl.session_state:
    response=requests.post(
        f"{API_Base}/conversation"
    )
    data=response.json()

    sl.session_state.conversation_id=(
        data["conversation_id"]
    )

conversation_id=(
    sl.session_state.conversation_id
)

if "messages" not in sl.session_state:
    sl.session_state.messages=[]

for message in sl.session_state.messages:
    with sl.chat_message(
        message["role"]
    ):
        sl.markdown(
            message["content"]
        )

question=sl.chat_input(
    "please enter your problem"
)

if question:
    sl.session_state.messages.append(
        {"role":"user",
         "content":question
        }
    )
    with sl.chat_message("user"):
        sl.markdown(question)

    response=requests.post(
        f"{API_Base}/chat",
        json={
            "question":question,
            "conversation_id":conversation_id
        }
    )

    if  response.status_code==200:
        data=response.json()
        answer=data["answer"]
    else:
        answer="AI failed"

    with sl.chat_message("assistant"):
        sl.markdown(answer)

    sl.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )