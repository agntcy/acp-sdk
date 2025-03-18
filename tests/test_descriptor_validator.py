# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import os
import pytest
from agntcy_acp.descriptor.validator import validate_agent_descriptor_file


@pytest.mark.parametrize(
    "test_filename, test_success, error_message",
    [
        ("descriptor_ok.json", True, ""),
        ("descriptor_ko.json", False, ""),
        ("descriptor_ko_value_streaming.json", False,
         "custom_streaming_update defined with `spec.capabilities.streaming.custom=false`"),
        ("descriptor_ko_thread_support.json", False,
         "Cannot define `specs.thread_state` if `specs.capabilities.threads` is `false`"),
        ("descriptor_ko_no_interrupts.json", False, "Interrupts defined with `spec.capabilities.interrupts=false`")
    ],
)
def test_descriptor_validator(test_filename, test_success, error_message):
    curpwd = os.path.dirname(os.path.realpath(__file__))
    fullpath = os.path.join(curpwd, "test_samples", test_filename)
    try:
        descriptor = validate_agent_descriptor_file(fullpath, raise_exception=True)
        assert (descriptor is not None)
    except Exception as e:
        assert (not test_success)
        assert (error_message in str(e))
