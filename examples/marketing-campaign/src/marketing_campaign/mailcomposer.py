from pydantic import BaseModel, Field

from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from typing_extensions import TypedDict, Union
from typing import Any
from pydantic import create_model


class Input(BaseModel):
    messages: list[HumanMessage|AIMessage]
    is_completed: bool

class Output(BaseModel):
    final_email: str

class State(BaseModel):
    input: Input|None = None
    output: Output|None = None




