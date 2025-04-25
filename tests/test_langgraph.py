# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import datetime
from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel

import agntcy_acp
from agntcy_acp import ApiClientConfiguration, ApiResponse
from agntcy_acp.langgraph.acp_node import ACPNode
from agntcy_acp.models import (
    RunCreateStateless,
    RunOutput,
    RunStateless,
    RunStatus,
    RunWaitResponseStateless,
)


class InputSchema(BaseModel):
    content: str

class OutputSchema(BaseModel):
    content: str

class StateMeasures(TypedDict):
    input: InputSchema
    output: OutputSchema

def test_langgraph_acp_node(mock_sync_api_client, default_api_key, default_agent_id, monkeypatch):
    monkeypatch.setenv("TEST_ENDPOINT", "http://mailcomposer")
    monkeypatch.setenv("TEST_API_KEY", f'{{"x-api-key": "{default_api_key}"}}')
    agent_id = "bogus-agent-id"
    init_run_id = "bugus-run-id"
    input = "input_string_is_uninteresting"
    output = input

    # Make sure data is deserialized
    def mock_response_deserialize(
        self, 
        response_data, 
        response_types_map = None,
    ):
        output_state = OutputSchema(content=output)
        run = RunWaitResponseStateless(
            run=RunStateless(
                run_id=init_run_id, 
                agent_id=default_agent_id, 
                creation=RunCreateStateless(agent_id=default_agent_id),
                status=RunStatus.SUCCESS,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
            output=RunOutput.from_dict({"type":"result", "values": output_state.model_dump()})
        )
        return ApiResponse[RunWaitResponseStateless](status_code=200, data=run, raw_data=run.model_dump_json(exclude_unset=True).encode())
    monkeypatch.setattr(agntcy_acp.ApiClient, "response_deserialize", mock_response_deserialize)

    client_config = ApiClientConfiguration.fromEnvPrefix("TEST_")

    # Instantiate the local ACP node for the remote agent
    acp_node = ACPNode(
        name="copy-io",
        agent_id=agent_id,
        client_config=client_config,
        input_path="input",
        input_type=InputSchema,
        output_path="output",
        output_type=OutputSchema,
    )

    # Create the state graph
    sg = StateGraph(StateMeasures)

    # Add nodes
    sg.add_node(acp_node)

    # Add edges
    sg.add_edge(START, acp_node.get_name())
    sg.add_edge(acp_node.get_name(), END)

    graph = sg.compile()
    output_state = graph.invoke({"input": InputSchema(content=input), "output": OutputSchema(content="bad-output")})
    assert output_state is not None
    assert output_state["output"].content == input
