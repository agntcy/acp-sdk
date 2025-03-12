from pydantic import BaseModel, Field
from typing import List, Dict
from acp_sdk.langgraph import BaseModelACPState
from src.marketing_campaign.sdk import ACPState
from langchain_core.messages import  AIMessage, HumanMessage



class InputState(BaseModel):
    messages: List[HumanMessage|AIMessage]  = Field([], description="Chat messages")

class OutputState(InputState):
    operation_logs:List[str] = Field([], description="List of operations performed by the agent")


class OverallState(OutputState, BaseModelACPState):
    has_composer_completed: bool | None = None
    has_reviewer_completed: bool | None = None
    has_sender_completed: bool | None = None