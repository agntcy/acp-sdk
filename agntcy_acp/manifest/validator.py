# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import json
import logging

from pydantic import ValidationError

from agntcy_acp.agws_v0 import OASF_EXTENSION_NAME_MANIFEST, AgentManifest
from agntcy_acp.exceptions import ACPDescriptorValidationException
from agntcy_acp.models import AgentACPDescriptor

logger = logging.getLogger(__name__)


def validate_agent_manifest_file(
    manifest_file_path: str, raise_exception: bool = False
) -> AgentManifest:
    # Load the descriptor and validate it
    manifest_json = load_json_file(manifest_file_path)
    return validate_agent_manifest(manifest_json, raise_exception)


def validate_agent_descriptor_file(
    descriptor_file_path: str, raise_exception: bool = False
) -> AgentACPDescriptor:
    # Load the descriptor and validate it
    descriptor_json = load_json_file(descriptor_file_path)
    return validate_agent_descriptor(descriptor_json, raise_exception)


def descriptor_from_manifest_obj(manifest: dict | AgentManifest) -> dict:
    # ACP Descriptor is in the extensions of an Agent Manifest
    if hasattr(manifest, "extensions"):
        for ext in manifest.extensions:
            if ext.name == OASF_EXTENSION_NAME_MANIFEST:
                descriptor_json = ext.data.acp
                return descriptor_json
    else:
        for ext in manifest.get("extensions", []):
            if ext.get("name", None) == OASF_EXTENSION_NAME_MANIFEST:
                ext_json = ext.get("data", {})
                descriptor_json = ext_json.get("acp", {})
                return descriptor_json
    return {}


def validate_agent_manifest(
    manifest_json: dict, raise_exception: bool = False
) -> AgentManifest | None:
    try:
        manifest = AgentManifest.model_validate(manifest_json)
        descriptor_json = descriptor_from_manifest_obj(manifest_json)
        validate_agent_descriptor(descriptor_json)
        # TODO: add additional manifest checks
    except (ValidationError, ACPDescriptorValidationException) as e:
        if raise_exception:
            raise e
        else:
            logger.debug(f"Validation Error: {e}")
        return None

    return manifest


def validate_agent_descriptor(
    descriptor_json: dict, raise_exception: bool = False
) -> AgentACPDescriptor | None:
    try:
        # pydandic validation
        descriptor = AgentACPDescriptor.model_validate(descriptor_json)
        # advanced validation
        # generate_agent_oapi(descriptor)
    except (ValidationError, ACPDescriptorValidationException) as e:
        if raise_exception:
            raise e
        else:
            logger.debug(f"Validation Error: {e}")
        return None

    return descriptor


def load_json_file(json_file_path: str) -> dict:
    with open(json_file_path, "r") as f:
        descriptor = json.load(f)
    return descriptor
