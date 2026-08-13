import json
import time

from app.core.logger import logger
from app.core.prompts import SYSTEM_PROMPT

from app.services.llm import call_llm
from app.services.memory import get_history
from app.services.db_service import save_message

from app.tools.schemas import tools
from app.tools.executor import execute_tools
from app.core.config import settings

MAX_AGENT_STEPS=settings.MAX_AGENT_STEPS


def run_agent(
    question: str,
    conversation_id: str
):

    start_time = time.time()

    try:

        
        history = get_history(conversation_id)

        
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages.extend(history)

        messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        logger.info(
            f"User question: {question}"
        )

       
        for step in range(MAX_AGENT_STEPS):

            logger.info(
                f"Agent step: {step + 1}"
            )

            response = call_llm(
                messages=messages,
                tools=tools
            )

            message = response.choices[0].message

           
            if not message.tool_calls:

                answer = message.content

                logger.info(
                    "Agent finished without tool call"
                )

                break

           
            messages.append(
                message.model_dump()
            )

           
            for tool_call in message.tool_calls:

                tool_name = tool_call.function.name
                arguments = tool_call.function.arguments

                logger.info(
                    f"Tool call: {tool_name} | args={arguments}"
                )

                result = execute_tools(
                    tool_name,
                    arguments
                )

                
                if isinstance(result, str):
                    tool_content = result
                else:
                    tool_content = json.dumps(
                        result,
                        ensure_ascii=False
                    )

                
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_content
                    }
                )

        else:

           
            raise RuntimeError(
                "Agent exceeded maximum steps"
            )

        # 8. 保存完整消息
        save_message(
            conversation_id,
            "user",
            question
        )

        save_message(
            conversation_id,
            "assistant",
            answer
        )

        return answer


    except Exception as e:

        logger.error(
            f"Agent failed: {str(e)}",
            exc_info=True
        )

        raise


    finally:

        latency = time.time() - start_time

        logger.info(
            f"Agent finished | latency={latency:.2f}s"
        )