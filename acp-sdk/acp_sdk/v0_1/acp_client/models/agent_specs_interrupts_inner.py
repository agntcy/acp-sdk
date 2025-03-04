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
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class AgentSpecsInterruptsInner(BaseModel):
    """
    AgentSpecsInterruptsInner
    """ # noqa: E501
    interrupt_type: StrictStr = Field(description="Name of this interrupt type. Needs to be unique in the list of interrupts.")
    interrupt_payload: Dict[str, Any] = Field(description="This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object")
    resume_payload: Dict[str, Any] = Field(description="This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object")
    __properties: ClassVar[List[str]] = ["interrupt_type", "interrupt_payload", "resume_payload"]

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
        """Create an instance of AgentSpecsInterruptsInner from a JSON string"""
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
        """Create an instance of AgentSpecsInterruptsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interrupt_type": obj.get("interrupt_type"),
            "interrupt_payload": obj.get("interrupt_payload"),
            "resume_payload": obj.get("resume_payload")
        })
        return _obj


