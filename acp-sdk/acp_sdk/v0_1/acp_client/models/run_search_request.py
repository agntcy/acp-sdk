# coding: utf-8

"""
    Agent Connect Protocol

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from .run_status import RunStatus
from typing import Optional, Set
from typing_extensions import Self

class RunSearchRequest(BaseModel):
    """
    Payload for listing runs.
    """ # noqa: E501
    agent_id: Optional[StrictStr] = Field(default=None, description="Matches all the Runs associated with the specified Agent ID.")
    status: Optional[RunStatus] = Field(default=None, description="Matches all the Runs associated with the specified status. One of 'pending', 'error', 'success', 'timeout', 'interrupted'.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Matches all threads for which metadata has  keys and values equal to those specified in this object.")
    limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(default=10, description="Maximum number to return.")
    offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=0, description="Offset to start from.")
    __properties: ClassVar[List[str]] = ["agent_id", "status", "metadata", "limit", "offset"]

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
        """Create an instance of RunSearchRequest from a JSON string"""
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
        """Create an instance of RunSearchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agent_id": obj.get("agent_id"),
            "status": obj.get("status"),
            "metadata": obj.get("metadata"),
            "limit": obj.get("limit") if obj.get("limit") is not None else 10,
            "offset": obj.get("offset") if obj.get("offset") is not None else 0
        })
        return _obj


