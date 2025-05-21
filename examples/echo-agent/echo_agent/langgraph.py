# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import logging
import os

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from .agent import echo_agent
from .state import AgentState, ConfigSchema, InputState


def setup_config(state: AgentState, config: RunnableConfig) -> AgentState:
    args = config.get("configurable", {})
    state.to_upper = bool(args.get("to_upper", os.getenv("TO_UPPER", state.to_upper)))
    state.to_lower = bool(args.get("to_lower", os.getenv("TO_LOWER", state.to_lower)))

    sleep_secs = args.get("sleep_secs", os.getenv("SLEEP_SECS", state.sleep_secs))
    if state.sleep_secs < 0:
        raise ValueError(f"sleep seconds {state.sleep_secs} must be non-negative")
    elif state.sleep_secs > 1000:
        raise ValueError(f"sleep seconds {state.sleep_secs} must be <= 1000")
    state.sleep_secs = sleep_secs

    interrupt_count = args.get("interrupt_count", os.getenv("INTERRUPT_COUNT", 0))
    if interrupt_count < 0:
        raise ValueError(f"interrupt {interrupt_count} must be non-negative")
    elif interrupt_count > 1000:
        raise ValueError(f"interrupt {interrupt_count} must be <= 1000")
    state.interrupt_left = interrupt_count

    logger = logging.getLogger("echo_agent.agent")
    logger.setLevel(args.get("log_level", "warning").upper())
    logger.debug(f"agent config: {state}")
    return state


def build_graph() -> CompiledStateGraph:
    # Create the graph and add the agent node
    graph_builder = StateGraph(AgentState, config_schema=ConfigSchema, input=InputState)
    graph_builder.add_node("setup_config", setup_config)
    graph_builder.add_node("echo_agent", echo_agent)

    graph_builder.add_edge(START, "setup_config")
    graph_builder.add_edge("setup_config", "echo_agent")
    graph_builder.add_edge("echo_agent", END)

    checkpointer = InMemorySaver()
    return graph_builder.compile(checkpointer=checkpointer)


AGENT_GRAPH = build_graph()
