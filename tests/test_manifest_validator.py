# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import os
import pytest
from agntcy_acp.descriptor.validator import validate_agent_manifest_file


@pytest.mark.parametrize(
    "test_filename, test_success, error_message",
    [
        ("manifest_ok_mailcomposer.json", True, ""),
        ("manifest_ok_marketing-campaign.json", True, ""),
    ],
)
def test_manifest_validator(test_filename, test_success, error_message):
    curpwd = os.path.dirname(os.path.realpath(__file__))
    fullpath = os.path.join(curpwd, "test_samples", test_filename)
    try:
        manifest = validate_agent_manifest_file(fullpath, raise_exception=True)
        assert (manifest is not None)
    except Exception as e:
        assert (not test_success)
        assert (error_message in str(e))
