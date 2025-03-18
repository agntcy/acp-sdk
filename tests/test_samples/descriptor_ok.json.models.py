# Generated from ACP Descriptor org.agntcy.sample-agent-1 using datamodel_code_generator.

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, RootModel


class ConfigSchema(BaseModel):
    test: Optional[bool] = None


class InputSchema(RootModel[int]):
    root: int


class OutputSchema(BaseModel):
    name: Optional[str] = None
