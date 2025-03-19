import os
from typing_extensions import Annotated, Union, TypedDict
from langchain_core.messages import AIMessage, HumanMessage


class AgentState(TypedDict, total=False):
    messages: list[Union[AIMessage, HumanMessage]]
    is_completed: bool

class OutputState(AgentState):
    final_email: str
