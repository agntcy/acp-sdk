# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

"""
    Agent Connect Protocol

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from agntcy_acp.acp_v0.models.message import Message
from typing import Optional, Set
from typing_extensions import Self

class Thread(BaseModel):
    """
    Represents a collection of consecutive runs over a thread.  Thread is associated with a state. Runs for a thread can potentially happen across different agents, if the state format is compatible.
    """ # noqa: E501
    thread_id: StrictStr = Field(description="unique identifier of a thread")
    created_at: datetime = Field(description="The time the thread was created.")
    updated_at: datetime = Field(description="The last time the thread was updated.")
    metadata: Dict[str, Any] = Field(description="Free form metadata for this thread")
    status: StrictStr = Field(description="The status of the thread.")
    values: Optional[Dict[str, Any]] = Field(default=None, description="The thread state. The schema is described in agent ACP descriptor under 'spec.thread_state'.")
    messages: Optional[List[Message]] = Field(default=None, description="The current Messages of the thread. If messages are contained in Thread.values, implementations should remove them from values when returning messages. When this key isn't present it means the thread/agent doesn't support messages.")
    __properties: ClassVar[List[str]] = ["thread_id", "created_at", "updated_at", "metadata", "status", "values", "messages"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['idle', 'busy', 'interrupted', 'error']):
            raise ValueError("must be one of enum values ('idle', 'busy', 'interrupted', 'error')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Thread from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item_messages in self.messages:
                if _item_messages:
                    _items.append(_item_messages.to_dict())
            _dict['messages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Thread from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "thread_id": obj.get("thread_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "metadata": obj.get("metadata"),
            "status": obj.get("status"),
            "values": obj.get("values"),
            "messages": [Message.from_dict(_item) for _item in obj["messages"]] if obj.get("messages") is not None else None
        })
        return _obj


