# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import io
from typing import Generator, List

from pydantic import BaseModel, RootModel
from urllib3 import HTTPResponse

import agntcy_acp
from agntcy_acp import ACPClient, ApiClient, ApiClientConfiguration
from agntcy_acp.models import (
    RunCreateStateful,
    RunCreateStateless,
    RunOutput,
    RunOutputStream,
    RunResult,
    RunSearchRequest,
    RunStateful,
    RunStateless,
    RunWaitResponseStateful,
    RunWaitResponseStateless,
    StreamEventPayload,
    ValueRunErrorUpdate,
    ValueRunInterruptUpdate,
)

ListRunStateless = RootModel[List[RunStateless]]
ListRunStateful = RootModel[List[RunStateful]]


def mock_response_api_client(
    api_client: ApiClient,
    response: BaseModel,
    default_api_key,
    monkeypatch,
):
    class RESTResponse(io.IOBase):
        def __init__(self, status, body: str) -> None:
            body_bytes = body.encode()
            self.response = HTTPResponse(body=body_bytes)
            self.status = status
            self.reason = None
            self.data = body_bytes

            def mock_stream(
                amt: int | None = 2**16,
                decode_content: bool | None = None,
                body=body,
            ) -> Generator[bytes, None, None]:
                sse_list = (
                    [
                        ":this is a test feed\nid: 1\n".encode(),
                        "event: agent_event\n".encode(),
                    ]
                    + [f"data: {line}\n".encode() for line in body.splitlines()]
                    + ["\n".encode()]
                )
                for chunk in sse_list:
                    yield chunk

            monkeypatch.setattr(self.response, "stream", mock_stream)

        def read(self):
            return self.data

        def getheaders(self):
            return {}

        def getheader(self, name, default=None):
            """Returns a given response header."""
            headers = {"content-type": "application/json"}
            return headers.get(name, "bogus")

    # Make sure apis return data
    def mock_call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,
        response=response,
    ):
        assert header_params is not None
        assert header_params["x-api-key"] == default_api_key
        if hasattr(response, "actual_instance"):
            response = response.actual_instance
        if hasattr(response, "to_json"):
            body = response.to_json()
        else:
            body = response.model_dump_json(by_alias=True, exclude_unset=True)

        return RESTResponse(status=200, body=body)

    monkeypatch.setattr(agntcy_acp.ApiClient, "call_api", mock_call_api)


def test_acp_client_stateless_runs_api(
    default_api_key, default_agent_id, default_run_stateless_response, monkeypatch
):
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": default_api_key})
    run_response = default_run_stateless_response
    run_output = RunOutput(
        RunResult(
            type="result",
            values={
                "key": "value",
            },
        )
    )

    with ACPClient(configuration=config) as client:
        mock_response_api_client(
            client.api_client, run_response, default_api_key, monkeypatch
        )

        response = client.create_stateless_run(
            run_create_stateless=RunCreateStateless(agent_id=default_agent_id)
        )
        assert response is not None
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status

        run_id = response.run_id
        response = client.get_stateless_run(run_id)
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status
        assert response is not None

        mock_response_api_client(
            client.api_client,
            RunWaitResponseStateless(run=run_response, output=run_output),
            default_api_key,
            monkeypatch,
        )
        response = client.wait_for_stateless_run_output(run_id)
        assert response is not None
        assert response.run is not None
        assert response.output is not None
        assert response.run.agent_id == run_response.agent_id
        assert response.run.run_id == run_response.run_id
        assert response.run.status == run_response.status
        assert response.output.actual_instance.type == run_output.actual_instance.type

        mock_response_api_client(
            client.api_client, run_response, default_api_key, monkeypatch
        )
        response = client.resume_stateless_run(run_id, {})
        assert response is not None
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status

        list_response = ListRunStateless.model_validate([run_response])
        mock_response_api_client(
            client.api_client, list_response, default_api_key, monkeypatch
        )
        response = client.search_stateless_runs(
            RunSearchRequest(agent_id=default_agent_id)
        )
        assert response is not None
        assert len(response) == 1

        mock_response_api_client(
            client.api_client, run_response, default_api_key, monkeypatch
        )
        response = client.delete_stateless_run(run_id)
        assert response is None


def test_acp_client_stream_stateless_runs_api(
    default_api_key, default_agent_id, default_run_output_stream, monkeypatch
):
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": default_api_key})

    with ACPClient(configuration=config) as client:
        mock_response_api_client(
            client.api_client,
            default_run_output_stream.data,
            default_api_key,
            monkeypatch,
        )
        stream = client.create_and_stream_stateless_run_output(
            run_create_stateless=RunCreateStateless(agent_id=default_agent_id)
        )
        for response in stream:
            assert response is not None
            assert (
                response.data.actual_instance.run_id
                == default_run_output_stream.data.actual_instance.run_id
            )


def test_acp_client_thread_run_api(
    default_api_key, default_run_stateful_response, default_agent_id, monkeypatch
):
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": default_api_key})
    thread_id = "d379d156-560b-4c97-ba04-0e88c26fe697"
    run_response = default_run_stateful_response
    run_output = RunOutput(
        RunResult(
            type="result",
            values={
                "key": "value",
            },
        )
    )

    with ACPClient(configuration=config) as client:
        mock_response_api_client(
            client.api_client, run_response, default_api_key, monkeypatch
        )
        response = client.create_thread_run(
            thread_id=thread_id,
            run_create_stateful=RunCreateStateful(agent_id=default_agent_id),
        )
        assert response is not None
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status

        run_id = response.run_id
        response = client.get_thread_run(thread_id=thread_id, run_id=run_id)
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status
        assert response is not None

        mock_response_api_client(
            client.api_client,
            RunWaitResponseStateful(run=run_response, output=run_output),
            default_api_key,
            monkeypatch,
        )
        response = client.wait_for_thread_run_output(thread_id=thread_id, run_id=run_id)
        assert response is not None
        assert response.run is not None
        assert response.output is not None
        assert response.run.agent_id == run_response.agent_id
        assert response.run.run_id == run_response.run_id
        assert response.run.status == run_response.status
        assert response.output.actual_instance.type == run_output.actual_instance.type

        mock_response_api_client(
            client.api_client, run_response, default_api_key, monkeypatch
        )
        response = client.resume_thread_run(thread_id=thread_id, run_id=run_id, body={})
        assert response is not None
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status

        list_response = ListRunStateful.model_validate([run_response])
        mock_response_api_client(
            client.api_client, list_response, default_api_key, monkeypatch
        )
        response = client.list_thread_runs(thread_id=thread_id)
        assert response is not None
        assert len(response) == 1

        response = client.delete_thread_run(thread_id=thread_id, run_id=run_id)
        assert response is None


def test_acp_client_stream_thread_run_api(
    default_api_key,
    default_agent_id,
    default_run_output_stream,
    default_thread_id,
    monkeypatch,
):
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": default_api_key})

    with ACPClient(configuration=config) as client:
        mock_response_api_client(
            client.api_client,
            default_run_output_stream.data,
            default_api_key,
            monkeypatch,
        )
        stream = client.create_and_stream_thread_run_output(
            thread_id=default_thread_id,
            run_create_stateful=RunCreateStateful(agent_id=default_agent_id),
        )
        for response in stream:
            assert response is not None
            assert (
                response.data.actual_instance.run_id
                == default_run_output_stream.data.actual_instance.run_id
            )

        interrupt_stream = RunOutputStream(
            id="1",
            event="agent_event",
            data=StreamEventPayload(
                ValueRunInterruptUpdate(
                    type="interrupt",
                    run_id=default_run_output_stream.data.actual_instance.run_id,
                    status="pending",
                    interrupt={
                        "key": "value",
                    },
                )
            ),
        )
        mock_response_api_client(
            client.api_client,
            interrupt_stream.data,
            default_api_key,
            monkeypatch,
        )
        stream = client.create_and_stream_thread_run_output(
            thread_id=default_thread_id,
            run_create_stateful=RunCreateStateful(agent_id=default_agent_id),
        )
        for response in stream:
            assert response is not None
            assert (
                response.data.actual_instance.run_id
                == interrupt_stream.data.actual_instance.run_id
            )

        error_stream = RunOutputStream(
            id="1",
            event="agent_event",
            data=StreamEventPayload(
                ValueRunErrorUpdate(
                    type="error",
                    run_id=default_run_output_stream.data.actual_instance.run_id,
                    status="pending",
                    description="I'm sorry, Dave.",
                    errcode=0,
                )
            ),
        )
        mock_response_api_client(
            client.api_client,
            error_stream.data,
            default_api_key,
            monkeypatch,
        )
        stream = client.create_and_stream_thread_run_output(
            thread_id=default_thread_id,
            run_create_stateful=RunCreateStateful(agent_id=default_agent_id),
        )
        for response in stream:
            assert response is not None
            assert (
                response.data.actual_instance.run_id
                == error_stream.data.actual_instance.run_id
            )
