# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0

# Use this to regenerate the reference oas for tests.
# You can also copy and paste the output in  test_manifest_validator.py file
regenerate_tests:
	for m in manifest_ok*.json; do\
		poetry run python3 -m acp_sdk generate-agent-oapi $${m} > "$${m}.oas.yml" ;\
		echo "(\"$${m}\", \"$${m}.oas.yml\"),";\
	done