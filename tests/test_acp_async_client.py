# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import datetime
import io
from agntcy_acp import AsyncACPClient, ApiResponse, ApiClientConfiguration, AsyncApiClient
from agntcy_acp.models import RunSearchRequest, RunStateless, RunStatus, RunCreateStateless

class RESTResponse(io.IOBase):
    def __init__(self, status, body) -> None:
        self.response = None
        self.status = status
        self.reason = None
        self.data = body

    async def read(self):
        return self.data

    def getheaders(self):
        return {}

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return "bogus"

async def test_acp_client_runs_api(monkeypatch):
    agent_id = "bogus-agent-id"
    init_run_id = "bugus-run-id"
    run_create = RunCreateStateless(agent_id=agent_id)
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": "bogus-api-key"})

    api_client = AsyncApiClient(config)
    # Make sure apis return data
    async def mock_call_api(
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None            
    ):
        assert header_params is not None
        assert header_params["x-api-key"] == "bogus-api-key"
        return RESTResponse(status=200, body="""
run_id: 1234-5678-90123
""")
    monkeypatch.setattr(api_client, "call_api", mock_call_api)

    # Make sure data is deserialized
    def mock_response_deserialize(response_data, response_types_map = None):
        run = RunStateless(
            run_id=init_run_id, 
            agent_id=agent_id, 
            creation=run_create,
            status=RunStatus.SUCCESS,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        return ApiResponse[RunStateless](status_code=200, data=run, raw_data=run.model_dump_json(exclude_unset=True).encode())
    monkeypatch.setattr(api_client, "response_deserialize", mock_response_deserialize)

    async with api_client:
        client = AsyncACPClient(api_client)

        response = await client.create_stateless_run(run_create_stateless=RunCreateStateless(agent_id=agent_id))
        assert response is not None
        run_id = response.run_id

        response = await client.get_stateless_run(run_id)
        assert response is not None

        response = await client.wait_for_stateless_run_output(run_id)
        assert response is not None

        response = await client.stream_stateless_run_output(run_id)
        assert response is not None

        response = await client.resume_stateless_run(run_id, {})
        assert response is not None

        response = await client.search_stateless_runs(RunSearchRequest(agent_id=agent_id))
        assert response is not None

        response = await client.delete_stateless_run(run_id)
        assert response is not None
