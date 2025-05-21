# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
from enum import Enum
from typing import List, Optional, TypedDict

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
    interrupt_count: int
    sleep_secs: int
    log_level: str


type MessageList = RootModel[List[Message]]


class EchoInterrupt(TypedDict):
    messages: Optional[List[Message]]


class EchoResume(TypedDict):
    messages: Optional[List[Message]]


# Graph input
class InputState(BaseModel):
    messages: Optional[List[Message]]


# Input + local config variables and defaults
class AgentState(InputState):
    to_upper: bool = Field(False)
    to_lower: bool = Field(False)
    sleep_secs: int = Field(1)
    interrupt_left: int = Field(
        0,
        description="Number of times to send an interrupt echo message instead of output.",
    )
