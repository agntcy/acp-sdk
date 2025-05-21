# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import asyncio
import io
from typing import List

from aiohttp import ClientResponse, RequestInfo, StreamReader
from aiohttp.base_protocol import BaseProtocol
from pydantic import BaseModel, RootModel
from yarl import URL

from agntcy_acp import ApiClientConfiguration, AsyncACPClient, AsyncApiClient
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
    api_client: AsyncApiClient,
    response: BaseModel,
    default_api_key,
    monkeypatch,
):
    class RESTResponseAsync(io.IOBase):
        def __init__(self, status, body: str) -> None:
            cur_loop = asyncio.get_running_loop()
            req_info = RequestInfo(
                URL("http://bogus.org/path/to/bogus"),
                "GET",
                {},
            )
            sse_list = (
                [
                    ":this is a test feed\nid: 1\n".encode(),
                    "event: agent_event\n".encode(),
                ]
                + [f"data: {line}\n".encode() for line in body.splitlines()]
                + ["\n".encode()]
            )
            print(sse_list)

            self.response = ClientResponse(
                req_info.method,
                req_info.url,
                writer=None,
                continue100=None,
                timer=None,
                request_info=req_info,
                traces=[],
                loop=cur_loop,
                session=None,
            )
            stream = StreamReader(
                protocol=BaseProtocol(loop=cur_loop),
                limit=100,
                loop=cur_loop,
            )
            for chunk in sse_list:
                stream.feed_data(chunk)
            stream.feed_eof()

            self.response.content = stream
            self.status = status
            self.reason = None
            self.data = body.encode()

        async def read(self):
            return self.data

        def getheaders(self):
            return {}

        def getheader(self, name, default=None):
            """Returns a given response header."""
            headers = {"content-type": "application/json"}
            return headers.get(name, "bogus")

    # Make sure apis return data
    async def mock_call_api(
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

        return RESTResponseAsync(status=200, body=body)

    monkeypatch.setattr(api_client, "call_api", mock_call_api)


async def test_acp_client_stateless_runs_api(
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

    async with AsyncACPClient(configuration=config) as client:
        mock_response_api_client(
            client.api_client, run_response, default_api_key, monkeypatch
        )

        response = await client.create_stateless_run(
            run_create_stateless=RunCreateStateless(agent_id=default_agent_id)
        )
        assert response is not None
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status

        run_id = response.run_id
        response = await client.get_stateless_run(run_id)
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
        response = await client.wait_for_stateless_run_output(run_id)
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
        response = await client.resume_stateless_run(run_id, {})
        assert response is not None
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status

        list_response = ListRunStateless.model_validate([run_response])
        mock_response_api_client(
            client.api_client, list_response, default_api_key, monkeypatch
        )
        response = await client.search_stateless_runs(
            RunSearchRequest(agent_id=default_agent_id)
        )
        assert response is not None
        assert len(response) == 1

        mock_response_api_client(
            client.api_client, run_response, default_api_key, monkeypatch
        )
        response = await client.delete_stateless_run(run_id)
        assert response is None


async def test_acp_client_stream_stateless_runs_api(
    default_api_key, default_agent_id, default_run_output_stream, monkeypatch
):
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": default_api_key})

    async with AsyncACPClient(configuration=config) as client:
        mock_response_api_client(
            client.api_client,
            default_run_output_stream.data,
            default_api_key,
            monkeypatch,
        )
        stream = client.create_and_stream_stateless_run_output(
            run_create_stateless=RunCreateStateless(agent_id=default_agent_id)
        )
        async for response in stream:
            assert response is not None
            assert (
                response.data.actual_instance.run_id
                == default_run_output_stream.data.actual_instance.run_id
            )


async def test_acp_client_thread_run_api(
    default_api_key,
    default_run_stateful_response,
    default_agent_id,
    default_thread_id,
    monkeypatch,
):
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": default_api_key})
    thread_id = default_thread_id
    run_response = default_run_stateful_response
    run_output = RunOutput(
        RunResult(
            type="result",
            values={
                "key": "value",
            },
        )
    )

    async with AsyncACPClient(configuration=config) as client:
        mock_response_api_client(
            client.api_client, run_response, default_api_key, monkeypatch
        )
        response = await client.create_thread_run(
            thread_id=thread_id,
            run_create_stateful=RunCreateStateful(agent_id=default_agent_id),
        )
        assert response is not None
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status

        run_id = response.run_id
        response = await client.get_thread_run(thread_id=thread_id, run_id=run_id)
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
        response = await client.wait_for_thread_run_output(
            thread_id=thread_id, run_id=run_id
        )
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
        response = await client.resume_thread_run(
            thread_id=thread_id, run_id=run_id, body={}
        )
        assert response is not None
        assert response.agent_id == run_response.agent_id
        assert response.run_id == run_response.run_id
        assert response.status == run_response.status

        list_response = ListRunStateful.model_validate([run_response])
        mock_response_api_client(
            client.api_client, list_response, default_api_key, monkeypatch
        )
        response = await client.list_thread_runs(thread_id=thread_id)
        assert response is not None
        assert len(response) == 1

        response = await client.delete_thread_run(thread_id=thread_id, run_id=run_id)
        assert response is None


async def test_acp_client_stream_thread_run_api(
    default_api_key,
    default_agent_id,
    default_run_output_stream,
    default_thread_id,
    monkeypatch,
):
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": default_api_key})

    async with AsyncACPClient(configuration=config) as client:
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
        prev_id = -1
        async for response in stream:
            assert response is not None
            assert response.event == "agent_event"
            assert int(response.id) > prev_id
            prev_id = int(response.id)
            assert (
                response.data.actual_instance.run_id
                == default_run_output_stream.data.actual_instance.run_id
            )
            assert (
                response.data.actual_instance.status
                == default_run_output_stream.data.actual_instance.status
            )
            assert (
                response.data.actual_instance.values
                == default_run_output_stream.data.actual_instance.values
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
        prev_id = -1
        async for response in stream:
            assert response is not None
            assert (
                response.data.actual_instance.run_id
                == interrupt_stream.data.actual_instance.run_id
            )
            assert response.event == "agent_event"
            assert int(response.id) > prev_id
            prev_id = int(response.id)
            assert (
                response.data.actual_instance.run_id
                == interrupt_stream.data.actual_instance.run_id
            )
            assert (
                response.data.actual_instance.status
                == interrupt_stream.data.actual_instance.status
            )
            assert (
                response.data.actual_instance.interrupt
                == interrupt_stream.data.actual_instance.interrupt
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
        prev_id = -1
        async for response in stream:
            assert response is not None
            assert (
                response.data.actual_instance.run_id
                == error_stream.data.actual_instance.run_id
            )
            assert response.event == "agent_event"
            assert int(response.id) > prev_id
            prev_id = int(response.id)
            assert (
                response.data.actual_instance.run_id
                == error_stream.data.actual_instance.run_id
            )
            assert (
                response.data.actual_instance.status
                == error_stream.data.actual_instance.status
            )
            assert (
                response.data.actual_instance.description
                == error_stream.data.actual_instance.description
            )
