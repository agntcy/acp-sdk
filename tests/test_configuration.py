# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import json
from agntcy_acp import ApiClientConfiguration

def test_client_config(monkeypatch):
    host = "test.host.com"
    username = "testuser"
    password = "testpass"
    api_key = "bogus-api-key"

    monkeypatch.setenv("TEST_HOST", host)
    monkeypatch.setenv("TEST_API_KEY", json.dumps({"x-api-key": api_key}))
    
    config = ApiClientConfiguration.fromEnvPrefix("TEST_", username=username, password=password)
    assert config is not None
    assert config.host == host
    assert config.password == password
    assert config.username == username
    assert config.retries is None
    assert config.api_key["x-api-key"] == api_key