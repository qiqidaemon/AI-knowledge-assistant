from app.tools import available_tools

def execute_tools(
        tool_name:str,
        arguments=None
):
    tool=available_tools.get(
        tool_name
    )
    if not tool:
        raise ValueError(
            f"Tool {tool_name} not found"
            )
    return tool()