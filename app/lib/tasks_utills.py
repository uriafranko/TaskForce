import importlib

from langchain.agents import Tool

from lib.models import ToolInitiator


def dynamic_import(attr_path: str):
    """
    Dynamically imports an attribute (e.g., a class or function)
    from a given path.

    Parameters:
    - attr_path (str): The full path to the attribute,
    formatted as 'module.submodule:AttributeName'.

    Returns:
    - The imported attribute.
    """
    if attr_path.startswith("from "):
        attr_path = attr_path.replace("from ", "")

    module_path, attr_name = attr_path.split(" import ")
    module = importlib.import_module(module_path)
    return getattr(module, attr_name)


def tool_initiator(tool_config: ToolInitiator):
    """
    Initializes a tool by dynamically importing the tool's
    class and calling
    its `init` method.
    """
    tool = dynamic_import(tool_config.path)
    return Tool(
        name=tool_config.name,
        func=tool.run,
        description=tool_config.description,
    )
