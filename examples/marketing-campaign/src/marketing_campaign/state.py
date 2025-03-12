from pydantic import BaseModel, Field
from typing import List, Dict
from acp_sdk.langgraph import BaseModelACPState
from src.marketing_campaign.sdk import ACPState


class InputState(BaseModel):
    description:str = Field("", description="Description of the marketing campaign")

class OutputState(BaseModel):
    operation_logs:List[str] = Field([], description="List of operations performed by the agent")

class State(InputState, OutputState, BaseModelACPState): pass
