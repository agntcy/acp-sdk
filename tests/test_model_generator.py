# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import difflib
import os
import tempfile

import pytest

from agntcy_acp.manifest.generator import generate_agent_models
from agntcy_acp.manifest.validator import validate_agent_descriptor_file


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
def test_models_generator(test_filename, model_ref_filename):
    curpwd = os.path.dirname(os.path.realpath(__file__))

    ref_models = os.path.join(curpwd, "test_samples", model_ref_filename)

    descriptor = validate_agent_descriptor_file(os.path.join(curpwd, "test_samples", test_filename))
    tmp_dir = tempfile.TemporaryDirectory()
    generate_agent_models(descriptor, tmp_dir.name, "models.py")

    diff = _diff_files(os.path.join(tmp_dir.name, "models.py"), ref_models)

    if diff:
        diff_str = '\n'.join(diff)
        raise AssertionError(
            f"Generated Models and ref '{ref_models}' are not identical. Differences:\n{diff_str}")


def _diff_files(test_file, ref_file):
    with open(test_file, 'r') as f:
        test_lines = f.readlines()

    with open(ref_file, 'r') as f:
        ref_lines = f.readlines()

    diff = difflib.unified_diff(
        test_lines,
        ref_lines,
        fromfile='generated',
        tofile='reference',
        lineterm=''
    )

    return list(diff)
