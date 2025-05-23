# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

"""
Agent Connect Protocol

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.2.2
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Self

from agntcy_acp.acp_v0.models.run_output import RunOutput
from agntcy_acp.acp_v0.models.run_stateful import RunStateful


class RunWaitResponseStateful(BaseModel):
    """
    RunWaitResponseStateful
    """  # noqa: E501

    run: Optional[RunStateful] = Field(default=None, description="The run information.")
    output: Optional[RunOutput] = None
    __properties: ClassVar[List[str]] = ["run", "output"]

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
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RunWaitResponseStateful from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of run
        if self.run:
            _dict["run"] = self.run.to_dict()
        # override the default output from pydantic by calling `to_dict()` of output
        if self.output:
            _dict["output"] = self.output.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RunWaitResponseStateful from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "run": RunStateful.from_dict(obj["run"])
                if obj.get("run") is not None
                else None,
                "output": RunOutput.from_dict(obj["output"])
                if obj.get("output") is not None
                else None,
            }
        )
        return _obj
