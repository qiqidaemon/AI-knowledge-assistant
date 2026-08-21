import streamlit as sl
import requests

API_Base="http://api:8000"

sl.set_page_config(
    page_title="main page",
    page_icon="🤖",
    layout="wide"
)

sl.title("AI knowledge Assistant version 0.7")



def creat_conversation():
    response=requests.post(
        f"{API_Base}/conversation"
    )
    response.raise_for_status()
    return response.json()

def get_conversation():
    response=requests.get(
        f"{API_Base}/conversations"
    )
    response.raise_for_status()
    return response.json()

def get_message(conversation_id):
    response=requests.get(
        f"{API_Base}/conversation/{conversation_id}/messages"
    )
    response.raise_for_status()
    return response.json()

def delete_conversation(conversation_id):
    response=requests.delete(
        f"{API_Base}/conversation/{conversation_id}"
    )
    response.raise_for_status()
    return response.json()

def send_message(question,conversation_id):
    response=requests.post(
        f"{API_Base}/chat",
        json={
            "question":question,
            "conversation_id":conversation_id
        }
    )

    response.raise_for_status()
    return response.json()

if "conversation_id" not in sl.session_state:
    sl.session_state.conversation_id=None

with sl.sidebar:
    sl.header("会话")

    if sl.button(
        "+ 新建会话",
        use_container_width=True
    ):
        conversation=creat_conversation()

        sl.session_state.conversation_id=(
            conversation["conversation_id"]
        )

        sl.rerun()

    try:
        conversations=get_conversation()

    except Exception as e:
        sl.error(
            f"获取会话列表失败：{e}"
        )

        conversations=[]

    for conversation in conversations:
        conversation_id=conversation["id"]

        title=conversation.get(
            "title",
            "新对话"
        )

        col1,col2=sl.columns(
            [4,1]

        )

        with col1:
            if sl.button(
                title,
                key=f"open_{conversation_id}",
                use_container_width=True
            ):
                sl.session_state.conversation_id=(
                    conversation_id
                )

                sl.rerun()
        with col2:
            if sl.button(
                "🗑",
                key=f"delete_{conversation_id}"
            ):
                delete_conversation(conversation_id)
                if(sl.session_state.conversation_id==conversation_id):
                    sl.session_state.conversation_id=None
                sl.rerun()

if not sl.session_state.conversation_id:
    sl.info(
        "请点击左侧【新建对话】开始聊天"
    )

    sl.stop()

conversation_id=(
    sl.session_state.conversation_id
)

try:
    messages=get_message(
        conversation_id
    )
except Exception as e:
    sl.error(
        f"加载历史消失失败：{e}"
    )

    messages=[]


question=sl.chat_input(
    "please write your question"
)

if question:
    with sl.chat_message("user"):
        sl.markdown(question)

    try:

        result=send_message(
            question,
            conversation_id
        )
        answer=result["answer"]

    except Exception as e:
        answer=(
            f"请求失败：{e}"
        )

    with sl.chat_message("assistant"):
        sl.markdown(answer)

    sl.rerun()