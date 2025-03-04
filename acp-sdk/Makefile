# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
default: test
.PHONY: setup_test test

setup_test:
	poetry sync --with test --without generate_server

test: setup_test
	@poetry run pytest --exitfirst -q tests/test_descriptor_validator.py::test_descriptor_validator
	@poetry run pytest --exitfirst -q tests/test_descriptor_validator.py::test_oas_generator
	poetry run pytest -vv tests/test_acp_client.py
