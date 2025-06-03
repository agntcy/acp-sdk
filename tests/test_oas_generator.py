# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import os

import pytest
from deepdiff import diff
from openapi_spec_validator.readers import read_from_filename

from agntcy_acp.manifest.generator import generate_agent_oapi
from agntcy_acp.manifest.validator import (
    validate_agent_descriptor_file,
    validate_agent_manifest_file,
)


@pytest.mark.needs_acp_spec
@pytest.mark.parametrize(
    "test_filename, oas_ref_filename",
    [
        ("descriptor_ok.json", "descriptor_ok.json.oas.yml"),
        ("descriptor_ok_no_callbacks.json", "descriptor_ok_no_callbacks.json.oas.yml"),
        (
            "descriptor_ok_no_interrupts.json",
            "descriptor_ok_no_interrupts.json.oas.yml",
        ),
        ("descriptor_ok_no_streaming.json", "descriptor_ok_no_streaming.json.oas.yml"),
        ("descriptor_ok_no_threads.json", "descriptor_ok_no_threads.json.oas.yml"),
        ("manifest_ok_mailcomposer.json", "manifest_ok_mailcomposer.json.oas.yml"),
        (
            "manifest_ok_marketing-campaign.json",
            "manifest_ok_marketing-campaign.json.oas.yml",
        ),
    ],
)
def test_oas_generator(test_filename, oas_ref_filename, monkeypatch):
    curpwd = os.path.dirname(os.path.realpath(__file__))
    ref_spec, _ = read_from_filename(
        os.path.join(curpwd, "test_samples", oas_ref_filename)
    )

    agent_descriptor_path = os.path.join(curpwd, "test_samples", test_filename)
    descriptor = validate_agent_descriptor_file(agent_descriptor_path)
    if descriptor is None:
        descriptor = validate_agent_manifest_file(
            agent_descriptor_path, raise_exception=True
        )

    assert descriptor is not None
    gen_spec = generate_agent_oapi(descriptor, "acp-spec/openapi.json")
    mapdiff = diff.DeepDiff(gen_spec, ref_spec)
    assert len(mapdiff.affected_paths) == 0
