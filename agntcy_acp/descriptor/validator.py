# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import copy
import json

from pydantic import ValidationError

from agntcy_acp.models import AgentACPDescriptor, AgentManifest
from agntcy_acp.exceptions import ACPDescriptorValidationException


def validate_agent_manifest_file(manifest_file_path: str, raise_exception: bool = False) -> AgentManifest:
    # Load the descriptor and validate it
    manifest_json = load_json_file(manifest_file_path)
    return validate_agent_manifest(manifest_json, raise_exception)

def validate_agent_descriptor_file(descriptor_file_path: str, raise_exception: bool = False) -> AgentACPDescriptor:
    # Load the descriptor and validate it
    descriptor_json = load_json_file(descriptor_file_path)
    return validate_agent_descriptor(descriptor_json, raise_exception)

def _descriptor_from_manifest(manifest_json: dict)->dict:
    # ACP Descriptor is an Agent Manifest without the deployment part
    descriptor_json = copy.deepcopy(manifest_json)
    del descriptor_json["deployment"]
    return descriptor_json

def validate_agent_manifest(manifest_json: dict, raise_exception: bool = False) -> AgentManifest | None:
    try:
        manifest = AgentManifest.model_validate(manifest_json)
        descriptor_json = _descriptor_from_manifest(manifest_json)
        validate_agent_descriptor(descriptor_json)
        # TODO: add additional manifest checks
    except (ValidationError, ACPDescriptorValidationException) as e:
        print(f"Validation Error: {e}")
        if raise_exception: raise e
        return None

    return manifest

def validate_agent_descriptor(descriptor_json: dict, raise_exception: bool = False) -> AgentACPDescriptor | None:
    try:
        # pydandic validation
        descriptor = AgentACPDescriptor.model_validate(descriptor_json)
        # advanced validation
        # generate_agent_oapi(descriptor)
    except (ValidationError, ACPDescriptorValidationException) as e:
        print(f"Validation Error: {e}")
        if raise_exception: raise e
        return None

    return descriptor


def load_json_file(json_file_path: str) -> dict:
    with open(json_file_path, "r") as f:
        descriptor = json.load(f)
    return descriptor
