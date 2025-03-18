# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
from acp_sdk import ApiClientConfiguration

def test_client_config(monkeypatch):
    host = "test.host.com"
    username = "testuser"
    password = "testpass"

    monkeypatch.setenv("TEST_HOST", host)
    config = ApiClientConfiguration.fromEnvPrefix("TEST_", username=username, password=password)
    assert config is not None
    assert config.host == host
    assert config.password == password
    assert config.username == username
    assert config.retries is None