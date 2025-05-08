# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import datetime
import io

import pytest

import agntcy_acp
from agntcy_acp import ApiResponse
from agntcy_acp.models import (
    RunCreateStateless,
    RunOutput,
    RunOutputStream,
    RunResult,
    RunStateless,
    RunStatus,
    StreamEventPayload,
    ValueRunResultUpdate,
)


@pytest.fixture
def default_agent_id():
    return "bogus-agent-id"

@pytest.fixture
def default_thread_id():
    return 'd379d156-560b-4c97-ba04-0e88c26fe697'

@pytest.fixture
def default_api_key():
    return "bogus-api-key"

@pytest.fixture
def default_run_stateless_response(default_agent_id) -> RunStateless:
    init_run_id = "bugus-run-id"
    return RunStateless(
        run_id=init_run_id, 
        agent_id=default_agent_id, 
        creation=RunCreateStateless(agent_id=default_agent_id),
        status=RunStatus.SUCCESS,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )

@pytest.fixture
def default_run_output() -> RunOutput:
    return RunOutput(RunResult(
        type="result",
        values={
            "key": "value",
        }
    ))

@pytest.fixture
def default_run_output_stream(default_run_stateless_response) -> RunOutputStream:
    return RunOutputStream(
        id="1",
        event="agent_event",
        data=StreamEventPayload(ValueRunResultUpdate(
            type="values",
            run_id = default_run_stateless_response.run_id,
            status="success",
            values = {
                "key": "value",
            }
        )),
    )

@pytest.fixture
def mock_async_api_client(
    default_agent_id, 
    default_api_key, 
    monkeypatch,
):
    init_run_id = "bugus-run-id"

    class RESTResponseAsync(io.IOBase):
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
        return RESTResponseAsync(status=200, body="""
    run_id: 1234-5678-90123
    """)
    monkeypatch.setattr(agntcy_acp.AsyncApiClient, "call_api", mock_call_api)

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
    monkeypatch.setattr(agntcy_acp.AsyncApiClient, "response_deserialize", mock_response_deserialize)

@pytest.fixture
def mock_sync_api_client(
    default_agent_id,
    default_api_key,
    monkeypatch,
):
    init_run_id = "bugus-run-id"

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
    monkeypatch.setattr(agntcy_acp.ApiClient, "call_api", mock_call_api)

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
    monkeypatch.setattr(agntcy_acp.ApiClient, "response_deserialize", mock_response_deserialize)
