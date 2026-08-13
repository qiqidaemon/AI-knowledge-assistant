from app.tools import available_tools
import json
from app.core.logger import logger

def execute_tools(
        tool_name:str,
        arguments:str
):
    tool=available_tools.get(
        tool_name
    )
    if not tool:
        return {
            "success":False,
            "error":f"Tool {tool_name} not found"
        }
    try:
        args=json.loads(arguments or "{}")
        result=tool(**args)

        return {
            "success":True,
            "data":result
        }
    except json.JSONDecodeError as e:
        logger.error(
            f"Tool arguments parse failed |"
            f"tool={tool_name} |"
            f"arguments={arguments}"
        )

        return {
            "success":False,
            "error":"工具参数格式错误"
        }
    except Exception as e:
        logger.error(
            f"Tool execution failed | "
            f"tool={tool_name} | "
            f"error={str(e)}",
            exc_info=True
        )
        return {
            "success":False,
            "error":str(e)
        }