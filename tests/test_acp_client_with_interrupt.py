# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import datetime
from typing import List, Optional, TypedDict
from unittest.mock import Mock

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command
from pydantic import BaseModel

import agntcy_acp
from agntcy_acp import ApiClientConfiguration
from agntcy_acp.langgraph.acp_node import ACPNode
from agntcy_acp.models import (
    RunCreateStateless,
    RunInterrupt,
    RunOutput,
    RunStateless,
    RunStatus,
    RunWaitResponseStateless,
)


class InputSchema(BaseModel):
    content: Optional[str] = None


class OutputSchema(BaseModel):
    messages: List[dict]


class StateMeasures(TypedDict):
    user_feedback: Optional[str] = None
    input: Optional[InputSchema] = None
    output: Optional[OutputSchema] = None


def test_interrupt_acp_node(
    default_api_key,
    default_agent_id,
    monkeypatch,
):
    agent_id = "bogus-agent-id"
    init_run_id = "bugus-run-id"
    monkeypatch.setenv("PHILOSOPHER_AGENT_HOST", "http://phil_agent")
    monkeypatch.setenv(
        "PHILOSOPHER_AGENT_API_KEY", f'{{"x-api-key": "{default_api_key}"}}'
    )

    output_state = OutputSchema(messages=[{"role": "human", "content": "Yes"}])

    def mock_response_deserialize(
        self,
        response_data,
        response_types_map=None,
    ):
        run = RunWaitResponseStateless(
            run=RunStateless(
                run_id=init_run_id,
                agent_id=default_agent_id,
                creation=RunCreateStateless(
                    agent_id=default_agent_id, multitask_strategy="interrupt"
                ),
                status=RunStatus.INTERRUPTED,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
            output=RunOutput(
                RunInterrupt(
                    type="interrupt",
                    interrupt={
                        "value": "Please provide feedback",
                        "resumable": True,
                        "ns": ["step_3:62e598fa-8653-9d6d-2046-a70203020e37"],
                    },
                )
            ),
        )
        return run

    def mock_wait_for_stateless_run_output_1(self, run_id):
        mock_wait_for_stateless_run_output = RunWaitResponseStateless(
            run=RunStateless(
                run_id="1929838238",
                agent_id=default_agent_id,
                creation=RunCreateStateless(
                    agent_id=default_agent_id, multitask_strategy="interrupt"
                ),
                status=RunStatus.INTERRUPTED,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
            output=RunOutput(
                RunInterrupt(
                    type="interrupt",
                    interrupt={
                        "confirmation": "Please confirm your feedback",
                        "resumable": True,
                        "ns": ["step_3:62e598fa-8653-9d6d-2046-a70203020e37"],
                    },
                )
            ),
        )
        return mock_wait_for_stateless_run_output

    def mock_wait_for_stateless_run_output_2(self, run_id):
        mock_wait_for_stateless_run_output_final = RunWaitResponseStateless(
            run=RunStateless(
                run_id=init_run_id,
                agent_id=default_agent_id,
                creation=RunCreateStateless(agent_id=default_agent_id),
                status=RunStatus.SUCCESS,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
            output=RunOutput.from_dict(
                {"type": "result", "values": output_state.model_dump()}
            ),
        )

        return mock_wait_for_stateless_run_output_final

    monkeypatch.setattr(
        agntcy_acp.ACPClient,
        "create_and_wait_for_stateless_run_output",
        mock_response_deserialize,
    )
    mock_resume_stateless_run = Mock()
    monkeypatch.setattr(
        agntcy_acp.ACPClient, "resume_stateless_run", mock_resume_stateless_run
    )
    monkeypatch.setattr(
        agntcy_acp.ACPClient,
        "wait_for_stateless_run_output",
        mock_wait_for_stateless_run_output_1,
    )

    client_config = ApiClientConfiguration.fromEnvPrefix("PHILOSOPHER_AGENT_")
    #
    # Instantiate the local ACP node for the remote agent
    acp_node = ACPNode(
        name="philosopher_agent",
        agent_id=agent_id,
        client_config=client_config,
        input_path="input",
        input_type=InputSchema,
        output_path="output",
        output_type=OutputSchema,
    )

    # Create the state graph

    def do_nothing(_state):
        pass

    def end_graph(_state):
        return {"output": output_state}

    sg = StateGraph(StateMeasures)
    sg.add_node(acp_node)
    sg.add_node("end_graph", end_graph)

    sg.add_edge(START, acp_node.get_name())
    sg.add_edge(acp_node.get_name(), "end_graph")
    sg.add_edge("end_graph", END)

    thread = {"configurable": {"thread_id": "1"}}

    memory = MemorySaver()
    graph = sg.compile(checkpointer=memory)
    graph.invoke({}, thread)
    curr_state = graph.get_state(thread)
    print(f"first_state {curr_state}")
    # Graph should be interrupted
    assert len(curr_state.tasks) > 0
    assert curr_state.tasks[0].interrupts is not None

    # Resume execution of graph
    graph.invoke(Command(resume={"user_feedback": "Continue execution"}), thread)

    mock_resume_stateless_run.assert_called_once()
    state_after_interrupt = graph.get_state(thread)

    print(state_after_interrupt)

    assert len(state_after_interrupt.tasks) > 0
    assert state_after_interrupt.tasks[0].interrupts is not None

    monkeypatch.setattr(
        agntcy_acp.ACPClient,
        "wait_for_stateless_run_output",
        mock_wait_for_stateless_run_output_2,
    )
    # Resume execution of graph
    graph.invoke(Command(resume={"user_feedback": "Yap I'm good"}), thread)

    final_state = graph.get_state(thread)
    assert len(final_state.tasks) == 0
    assert final_state.next == ()
