# Generated from ACP Descriptor org.agntcy.marketing-campaign using datamodel_code_generator.

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class ConfigSchema(BaseModel):
    recipient_email_address: Optional[str] = Field(
        None,
        description='Email address of the email recipient',
        title='Recipient Email Address',
    )
    sender_email_address: Optional[str] = Field(
        None,
        description='Email address of the email sender',
        title='Sender Email Address',
    )


class InputSchema(BaseModel):
    messages: Optional[List[Message]] = Field(
        [], description='Chat messages', title='Messages'
    )


class Message(BaseModel):
    type: Type = Field(
        ...,
        description='indicates the originator of the message, a human or an assistant',
    )
    content: str = Field(..., description='the content of the message', title='Content')


class OutputSchema(BaseModel):
    messages: Optional[List[Message]] = Field(
        [], description='Chat messages', title='Messages'
    )
    operation_logs: Optional[List[str]] = Field(
        [],
        description='An array containing all the operations performed and their result. Each operation is appended to this array with a timestamp.',
        examples=[
            [
                'Mar 15 18:10:39 Operation performed: email sent Result: OK',
                'Mar 19 18:13:39 Operation X failed',
            ]
        ],
        title='Operation Logs',
    )


class Type(Enum):
    human = 'human'
    assistant = 'assistant'
    ai = 'ai'
