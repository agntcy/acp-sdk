# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import os
import pytest
from agntcy_acp.descriptor.validator import validate_agent_descriptor_file
from agntcy_acp.descriptor.generator import generate_agent_oapi
from openapi_spec_validator.readers import read_from_filename
from deepdiff import diff


@pytest.mark.parametrize(
    "test_filename, oas_ref_filename",
    [
        ("descriptor_ok.json", "descriptor_ok.json.oas.yml"),
        ("descriptor_ok_no_callbacks.json", "descriptor_ok_no_callbacks.json.oas.yml"),
        ("descriptor_ok_no_interrupts.json", "descriptor_ok_no_interrupts.json.oas.yml"),
        ("descriptor_ok_no_streaming.json", "descriptor_ok_no_streaming.json.oas.yml"),
        ("descriptor_ok_no_threads.json", "descriptor_ok_no_threads.json.oas.yml"),
        ("manifest_ok_mailcomposer.json", "manifest_ok_mailcomposer.json.oas.yml"),
        ("manifest_ok_marketing-campaign.json", "manifest_ok_marketing-campaign.json.oas.yml"),

    ],
)
def test_oas_generator(test_filename, oas_ref_filename):
    curpwd = os.path.dirname(os.path.realpath(__file__))
    ref_spec, base_uri = read_from_filename(os.path.join(curpwd, "test_samples", oas_ref_filename))

    descriptor = validate_agent_descriptor_file(os.path.join(curpwd, "test_samples", test_filename))
    gen_spec = generate_agent_oapi(descriptor)
    mapdiff = diff.DeepDiff(gen_spec, ref_spec)
    assert len(mapdiff.affected_paths) == 0
