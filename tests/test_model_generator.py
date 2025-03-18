# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import os
import pytest
from agntcy_acp.descriptor.validator import validate_agent_descriptor_file
from agntcy_acp.descriptor.generator import generate_agent_models
import tempfile
import subprocess


@pytest.mark.parametrize(
    "test_filename, model_ref_filename",
    [
        ("descriptor_ok.json", "descriptor_ok.json.models.py"),
        ("descriptor_ok_no_callbacks.json", "descriptor_ok_no_callbacks.json.models.py"),
        ("descriptor_ok_no_interrupts.json", "descriptor_ok_no_interrupts.json.models.py"),
        ("descriptor_ok_no_streaming.json", "descriptor_ok_no_streaming.json.models.py"),
        ("descriptor_ok_no_threads.json", "descriptor_ok_no_threads.json.models.py"),
        ("manifest_ok_mailcomposer.json", "manifest_ok_mailcomposer.json.models.py"),
        ("manifest_ok_marketing-campaign.json", "manifest_ok_marketing-campaign.json.models.py"),

    ],
)
def test_oas_generator(test_filename, model_ref_filename):
    curpwd = os.path.dirname(os.path.realpath(__file__))

    ref_models = os.path.join(curpwd, "test_samples", model_ref_filename)

    descriptor = validate_agent_descriptor_file(os.path.join(curpwd, "test_samples", test_filename))
    tmp_dir = tempfile.TemporaryDirectory()
    generate_agent_models(descriptor, tmp_dir.name, "models.py")

    result = subprocess.run(args=["diff", os.path.join(tmp_dir.name, "models.py"), ref_models], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise AssertionError(
            f"Generated Models and ref '{ref_models}' are not identical. Differences:\n{result.stdout.decode()}")

