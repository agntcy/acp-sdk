# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from .agent import echo_agent
from .state import AgentState


def build_graph() -> CompiledStateGraph:
    # Create the graph and add the agent node
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node("echo_agent", echo_agent)

    graph_builder.add_edge(START, "echo_agent")
    graph_builder.add_edge("echo_agent", END)

    return graph_builder.compile()


# Compile the graph
AGENT_GRAPH = build_graph()
