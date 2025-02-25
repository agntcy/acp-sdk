# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import json

from pydantic import ValidationError

from acp_sdk.models.models import AgentManifest


def validate_manifest_file(manifest_file_path: str) -> AgentManifest:
    # Load the manifest and validate it
    json_manifest = load_manifest(manifest_file_path)
    return validate_manifest(json_manifest)


def validate_manifest(json_manifest: dict) -> AgentManifest | None:
    # pydantic validation
    try:
        manifest = AgentManifest.model_validate(json_manifest)
    except ValidationError as e:
        print(e)
        return None

    print("Manifest is valid")

    return manifest


def load_manifest(manifest_file_path: str) -> dict:
    with open(manifest_file_path, "r") as f:
        manifest = json.load(f)
    return manifest
