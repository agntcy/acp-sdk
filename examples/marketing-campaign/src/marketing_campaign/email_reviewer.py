# generated by datamodel-codegen:
#   filename:  /var/folders/x1/p1jlgprs7_g3l7tkwv4_ksx40000gn/T/tmp8pvrdh5n/openapi.yaml
#   timestamp: 2025-03-19T15:04:47+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field, RootModel


class TargetAudience(Enum):
    general = 'general'
    technical = 'technical'
    business = 'business'
    academic = 'academic'


class InputSchema(BaseModel):
    email: str = Field(
        ..., description='The email content to be reviewed and corrected'
    )
    target_audience: TargetAudience = Field(
        ...,
        description='The target audience for the email, affecting the style of review',
    )


class OutputSchema(BaseModel):
    correct: bool = Field(
        ...,
        description='Indicates whether the email is correct and requires no changes',
    )
    corrected_email: Optional[str] = Field(
        None,
        description='The corrected version of the email, if changes were necessary',
    )


class ConfigSchema(RootModel[Any]):
    root: Any
