from pydantic import BaseModel


class ToolInitiator(BaseModel):
    path: str
    name: str
    description: str
