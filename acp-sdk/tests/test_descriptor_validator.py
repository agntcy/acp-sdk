# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import os
import pytest
from acp_sdk.descriptor.validator import validate_agent_descriptor_file
from acp_sdk.descriptor.generator import generate_agent_oapi
from openapi_spec_validator.readers import read_from_filename
from deepdiff import diff


@pytest.mark.parametrize(
    "test_filename, test_success, error_message",
    [
        ("descriptor_ok.json", True, ""),
        ("descriptor_ko.json", False, ""),
        ("descriptor_ko_value_streaming.json", False, "custom_streaming_update defined with `spec.capabilities.streaming.custom=false`"),
        ("descriptor_ko_thread_support.json", False,
         "Cannot define `specs.thread_state` if `specs.capabilities.threads` is `false`"),
        ("descriptor_ko_no_interrupts.json", False, "Interrupts defined with `spec.capabilities.interrupts=false`")
    ],
)
def test_descriptor_validator(test_filename, test_success, error_message):
    curpwd = os.path.dirname(os.path.realpath(__file__))
    fullpath = os.path.join(curpwd, "sample_descriptors", test_filename)
    try:
        descriptor = validate_agent_descriptor_file(fullpath, raise_exception=True)
        assert (descriptor is not None)
    except Exception as e:
        assert (not test_success)
        assert (error_message in str(e))


@pytest.mark.parametrize(
    "test_filename, oas_ref_filename",
    [
        ("descriptor_ok.json", "descriptor_ok.json.oas.yml"),
        ("descriptor_ok_no_callbacks.json", "descriptor_ok_no_callbacks.json.oas.yml"),
        ("descriptor_ok_no_interrupts.json", "descriptor_ok_no_interrupts.json.oas.yml"),
        ("descriptor_ok_no_streaming.json", "descriptor_ok_no_streaming.json.oas.yml"),
        ("descriptor_ok_no_threads.json", "descriptor_ok_no_threads.json.oas.yml"),
    ],
)
def test_oas_generator(test_filename, oas_ref_filename):
    curpwd = os.path.dirname(os.path.realpath(__file__))
    ref_spec, base_uri = read_from_filename(os.path.join(curpwd, "sample_descriptors", oas_ref_filename))

    descriptor = validate_agent_descriptor_file(os.path.join(curpwd, "sample_descriptors", test_filename))
    gen_spec = generate_agent_oapi(descriptor)
    mapdiff = diff.DeepDiff(gen_spec, ref_spec)
    assert len(mapdiff.affected_paths) == 0
