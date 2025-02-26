# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import json

from pydantic import ValidationError

from acp_sdk.models.models import AgentManifest
from .generator import generate_agent_oapi
from .exceptions import ManifestValidationException


def validate_manifest_file(manifest_file_path: str, raise_exception: bool = False) -> AgentManifest:
    # Load the manifest and validate it
    json_manifest = load_manifest(manifest_file_path)
    return validate_manifest(json_manifest, raise_exception)


def validate_manifest(json_manifest: dict, raise_exception: bool = False) -> AgentManifest | None:
    try:
        # pydandic validation
        manifest = AgentManifest.model_validate(json_manifest)
        # advanced validation
        generate_agent_oapi(manifest)
    except (ValidationError, ManifestValidationException) as e:
        print(f"Validation Error: {e}")
        if raise_exception: raise e
        return None

    print("Manifest is valid")

    return manifest


def load_manifest(manifest_file_path: str) -> dict:
    with open(manifest_file_path, "r") as f:
        manifest = json.load(f)
    return manifest
