# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import json

from pydantic import ValidationError

from acp_sdk.models import AgentACPDescriptor
from acp_sdk.exceptions import ACPDescriptorValidationException


def validate_agent_descriptor_file(descriptor_file_path: str, raise_exception: bool = False) -> AgentACPDescriptor:
    # Load the descriptor and validate it
    json_descriptor = load_agent_descriptor(descriptor_file_path)
    return validate_agent_descriptor(json_descriptor, raise_exception)


def validate_agent_descriptor(json_descriptor: dict, raise_exception: bool = False) -> AgentACPDescriptor | None:
    try:
        # pydandic validation
        descriptor = AgentACPDescriptor.model_validate(json_descriptor)
        # advanced validation
        # generate_agent_oapi(descriptor)
    except (ValidationError, ACPDescriptorValidationException) as e:
        print(f"Validation Error: {e}")
        if raise_exception: raise e
        return None

    return descriptor


def load_agent_descriptor(descriptor_file_path: str) -> dict:
    with open(descriptor_file_path, "r") as f:
        descriptor = json.load(f)
    return descriptor
