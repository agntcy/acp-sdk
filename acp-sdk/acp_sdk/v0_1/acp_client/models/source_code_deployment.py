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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from .source_code_deployment_framework_config import SourceCodeDeploymentFrameworkConfig
from typing import Optional, Set
from typing_extensions import Self

class SourceCodeDeployment(BaseModel):
    """
    Describes the source code where the agent is available. It specifies also the type of deployer that it supports.
    """ # noqa: E501
    type: StrictStr
    name: Optional[StrictStr] = Field(default=None, description="Name this deployment option is referred to within this agent. This is needed to indicate which one is preferred when this manifest is referred. Can be omitted, in such case selection is not possible.")
    url: StrictStr = Field(description="Location of the source code. E.g. path to code root, github repo url etc.")
    framework_config: SourceCodeDeploymentFrameworkConfig
    __properties: ClassVar[List[str]] = ["type", "name", "url", "framework_config"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['source_code']):
            raise ValueError("must be one of enum values ('source_code')")
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
        """Create an instance of SourceCodeDeployment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of framework_config
        if self.framework_config:
            _dict['framework_config'] = self.framework_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceCodeDeployment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "url": obj.get("url"),
            "framework_config": SourceCodeDeploymentFrameworkConfig.from_dict(obj["framework_config"]) if obj.get("framework_config") is not None else None
        })
        return _obj


