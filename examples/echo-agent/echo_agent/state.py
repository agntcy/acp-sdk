# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
from enum import Enum
from typing import Optional, TypedDict, List

from pydantic import BaseModel, Field, RootModel


class MsgType(Enum):
    human = "human"
    assistant = "assistant"


class Message(BaseModel):
    type: MsgType = Field(
        ...,
        description="indicates the originator of the message, a human or an assistant",
    )
    content: str = Field(..., description="the content of the message")


class ConfigSchema(TypedDict):
    to_upper: bool
    to_lower: bool

MessageList = RootModel[List[Message]]

class AgentState(BaseModel):
    messages: Optional[List[Message]] = None
