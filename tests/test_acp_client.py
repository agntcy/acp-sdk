# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import datetime
import io
from acp_sdk import ACPClient, ApiResponse, Configuration, ApiClient
from acp_sdk.models import RunCreate, RunSearchRequest, Run, RunStatus

class RESTResponse(io.IOBase):
    def __init__(self, status, body) -> None:
        self.response = None
        self.status = status
        self.reason = None
        self.data = body

    def read(self):
        return self.data

    def getheaders(self):
        return {}

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return "bogus"

def test_acp_client_runs_api(monkeypatch):
    agent_id = "bogus-agent-id"
    init_run_id = "bugus-run-id"
    run_create = RunCreate(agent_id=agent_id)

    api_client = ApiClient(Configuration(retries=2, api_key="bogus"))
    # Make sure apis return data
    def mock_call_api(
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None            
    ):
        return RESTResponse(status=200, body="""
run_id: 1234-5678-90123
""")
    monkeypatch.setattr(api_client, "call_api", mock_call_api)

    # Make sure data is deserialized
    def mock_response_deserialize(response_data, response_types_map = None):
        run = Run(
            run_id=init_run_id, 
            agent_id=agent_id, 
            creation=run_create,
            status=RunStatus.SUCCESS,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        return ApiResponse[Run](status_code=200, data=run, raw_data=run.model_dump_json(exclude_unset=True).encode())
    monkeypatch.setattr(api_client, "response_deserialize", mock_response_deserialize)
    client = ACPClient(api_client)

    response = client.create_run(run_create=run_create)
    assert response is not None
    run_id = response.run_id

    response = client.get_run(run_id)
    assert response is not None

    response = client.get_run_output(run_id)
    assert response is not None

    response = client.get_run_stream(run_id)
    assert response is not None

    response = client.resume_run(run_id, {})
    assert response is not None

    response = client.search_runs(RunSearchRequest(agent_id=agent_id))
    assert response is not None

    response = client.delete_run(run_id)
    assert response is not None
