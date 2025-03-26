# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import datetime
import io

from agntcy_acp import ApiResponse, ApiClient, AsyncApiClient, ApiClientConfiguration
from agntcy_acp.models import RunStateless, RunCreateStateless, RunStatus


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

def mock_async_api_client(
    config: ApiClientConfiguration,
    default_agent_id, 
    default_api_key, 
    monkeypatch,
) -> AsyncApiClient:
    init_run_id = "bugus-run-id"
    api_client = AsyncApiClient(config)

    # Make sure apis return data
    async def mock_call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ):
        assert header_params is not None
        assert header_params["x-api-key"] == default_api_key
        return RESTResponse(status=200, body="""
    run_id: 1234-5678-90123
    """)
    monkeypatch.setattr(api_client, "call_api", mock_call_api)

    # Make sure data is deserialized
    def mock_response_deserialize(
        self,
        response_data, 
        response_types_map = None,
    ):
        run = RunStateless(
            run_id=init_run_id, 
            agent_id=default_agent_id, 
            creation=RunCreateStateless(agent_id=default_agent_id),
            status=RunStatus.SUCCESS,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        return ApiResponse[RunStateless](status_code=200, data=run, raw_data=run.model_dump_json(exclude_unset=True).encode())
    monkeypatch.setattr(api_client, "response_deserialize", mock_response_deserialize)

    return api_client

def mock_sync_api_client(
    config: ApiClientConfiguration, 
    default_agent_id,
    default_api_key,
    monkeypatch,
) -> ApiClient:
    init_run_id = "bugus-run-id"
    api_client = ApiClient(config)

    # Make sure apis return data
    def mock_call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,        
    ):
        assert header_params is not None
        assert header_params["x-api-key"] == default_api_key
        return RESTResponse(status=200, body="""
    run_id: 1234-5678-90123
    """)
    monkeypatch.setattr(api_client, "call_api", mock_call_api)

    # Make sure data is deserialized
    def mock_response_deserialize(
        self, 
        response_data, 
        response_types_map = None,
    ):
        run = RunStateless(
            run_id=init_run_id, 
            agent_id=default_agent_id, 
            creation=RunCreateStateless(agent_id=default_agent_id),
            status=RunStatus.SUCCESS,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        return ApiResponse[RunStateless](status_code=200, data=run, raw_data=run.model_dump_json(exclude_unset=True).encode())
    monkeypatch.setattr(api_client, "response_deserialize", mock_response_deserialize)

    return api_client
