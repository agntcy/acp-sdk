# /// script
# requires-python = ">=3.12"
# dependencies = ["jsonschema", "pydantic"]
# ///

from enum import Enum
from typing import List, TypedDict

import jsonschema
from pydantic import BaseModel, Field

interrupt_schema = {
    "title": "Interrupt Payload",
    "description": "Input message echoed as interrupt payload.",
    "$defs": {
        "Message": {
            "properties": {
                "type": {
                    "$ref": "#/$defs/Type",
                    "description": "indicates the originator of the message, a human or an assistant",
                },
                "content": {
                    "description": "the content of the message",
                    "title": "Content",
                    "type": "string",
                },
            },
            "required": ["type", "content"],
            "title": "Message",
            "type": "object",
        },
        "Type": {
            "enum": ["human", "assistant", "ai"],
            "title": "Type",
            "type": "string",
        },
    },
    "properties": {
        "messages": {
            "anyOf": [
                {"items": {"$ref": "#/$defs/Message"}, "type": "array"},
                {"type": "null"},
            ],
            "default": None,
            "title": "Messages",
        }
    },
    "additionalProperties": False,
    "required": ["messages"],
    "type": "object",
}


class MsgType(Enum):
    human = "human"
    assistant = "assistant"


class Message(BaseModel):
    type: MsgType = Field(
        ...,
        description="indicates the originator of the message, a human or an assistant",
    )
    content: str = Field(..., description="the content of the message")


class EchoInterrupt(TypedDict):
    messages: List[Message]


test_instance = {"messages": [{"type": "assistant", "content": "yo!"}]}
jsonschema.validate(instance=test_instance, schema=interrupt_schema)

output_messages = [
    Message(type=MsgType.assistant, content="yo, dude").model_dump(mode="json")
]
interrupt_message = {"messages": output_messages}

jsonschema.validate(instance=interrupt_message, schema=interrupt_schema)
