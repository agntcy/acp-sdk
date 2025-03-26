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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ThreadCreate(BaseModel):
    """
    Detail of an empty thread to be created.
    """ # noqa: E501
    thread_id: Optional[StrictStr] = Field(default=None, description="The ID of the thread. If not provided, a random UUID will be generated.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Free form metadata for this thread")
    if_exists: Optional[StrictStr] = Field(default='raise', description="How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing thread).")
    __properties: ClassVar[List[str]] = ["thread_id", "metadata", "if_exists"]

    @field_validator('if_exists')
    def if_exists_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['raise', 'do_nothing']):
            raise ValueError("must be one of enum values ('raise', 'do_nothing')")
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
        """Create an instance of ThreadCreate from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ThreadCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "thread_id": obj.get("thread_id"),
            "metadata": obj.get("metadata"),
            "if_exists": obj.get("if_exists") if obj.get("if_exists") is not None else 'raise'
        })
        return _obj


