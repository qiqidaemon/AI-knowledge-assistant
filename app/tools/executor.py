from app.tools import available_tools
import json

def execute_tools(
        tool_name:str,
        arguments:str
):
    tool=available_tools.get(
        tool_name
    )
    if not tool:
        raise ValueError(
            f"Tool {tool_name} not found"
            )
    args=json.loads(arguments)
    return tool(**args)