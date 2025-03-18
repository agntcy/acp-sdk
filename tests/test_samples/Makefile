# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
default: regenerate_tests
.PHONY: regenerate_tests setup

setup:
	poetry sync --without generate_server

# Use this to regenerate the reference oas for tests.
# You can also copy and paste the output in test_descriptor_validator.py file
regenerate_tests: setup
	export ACP_SPEC_PATH="../../acp-spec/openapi.yaml" ; \
	for m in *_ok*.json ; do\
		poetry run python3 -m agntcy_acp generate-agent-oapi $${m} > "$${m}.oas.yml" ;\
		echo "(\"$${m}\", \"$${m}.oas.yml\")," ;\
	done; \
	for m in *_ok*.json ; do\
		poetry run python3 -m agntcy_acp generate-agent-models $${m} --output-dir . --model-file-name "$${m}.models.py" ;\
		echo "(\"$${m}\", \"$${m}.models.py\")," ;\
	done