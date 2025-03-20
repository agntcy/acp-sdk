
from typing_extensions import TypedDict
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

class Type(Enum):
    human = 'human'
    assistant = 'assistant'
    ai = 'ai'


class Message(BaseModel):
    type: Type = Field(
        ...,
        description='indicates the originator of the message, a human or an assistant',
    )
    content: str = Field(..., description='the content of the message')



class ConfigSchema(BaseModel):
    test: bool



class AgentState(TypedDict, total=False):
    messages: list[Message]
    is_completed: bool

class OutputState(AgentState):
    final_email: str
