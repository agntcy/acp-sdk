# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import itertools
import logging
import uuid

import click
from langchain_core.runnables import RunnableConfig
from langgraph.types import Command

from .langgraph import AGENT_GRAPH
from .state import AgentState, ConfigSchema, Message, MsgType

logger = logging.getLogger(__name__)


class ParamMessage(click.ParamType):
    name = "message"

    def __init__(self, **kwargs):
        self.msg_type = kwargs.pop("msg_type", MsgType.human)
        super().__init__(**kwargs)

    def convert(self, value, param, ctx):
        try:
            return Message(type=self.msg_type, content=value)
        except ValueError:
            self.fail(f"{value!r} is not valid message content", param, ctx)


@click.command(short_help="Validate agent ACP descriptor")
@click.option(
    "--to-upper",
    envvar="TO_UPPER",
    is_flag=True,
    show_envvar=True,
    default=False,
    help="Convert input to upper case.",
)
@click.option(
    "--to-lower",
    envvar="TO_LOWER",
    is_flag=True,
    show_envvar=True,
    default=False,
    help="Convert input to lower case.",
)
@click.option(
    "--log-level",
    type=click.Choice(
        ["critical", "error", "warning", "info", "debug"], case_sensitive=False
    ),
    default="info",
    help="Set logging level.",
)
@click.option(
    "--human",
    type=ParamMessage(msg_type=MsgType.human),
    multiple=True,
    help="Add a human message.",
)
@click.option(
    "--assistant",
    type=ParamMessage(msg_type=MsgType.assistant),
    multiple=True,
    help="Add a human message.",
)
@click.option(
    "--interrupt", is_flag=True, multiple=False, help="Add an interrupt in the flow"
)
def echo_server_agent(to_upper, to_lower, human, assistant, log_level, interrupt):
    """ """
    logging.basicConfig(level=log_level.upper())

    config = ConfigSchema(to_lower=to_lower, to_upper=to_upper)
    if human is not None and assistant is not None:
        # Interleave list starting with human. Stops at shortest list.
        messages = list(itertools.chain(*zip(human, assistant)))
        # Append rest of list.
        if len(human) > len(assistant):
            messages += human[len(assistant) :]
        elif len(assistant) > len(human):
            messages += assistant[len(human) :]
    elif human is not None:
        messages = human
    elif assistant is not None:
        messages = assistant
    else:
        messages = []

    logger.debug(f"input messages: {messages}")

    # Imitate input from ACP API
    input_api_object = AgentState(messages=messages).model_dump(mode="json")

    config["thread_id"] = str(uuid.uuid4())
    runnable_config = RunnableConfig(configurable=config)

    output_state = AGENT_GRAPH.invoke(
        AGENT_GRAPH.builder.schema.model_validate(input_api_object),
        config=runnable_config,
    )

    logger.debug(f"output messages: {output_state}")
    agent_state = AgentState(messages=output_state.get("messages", []))

    # Get state to check if agent is interrupted
    current_graph_state = AGENT_GRAPH.get_state(runnable_config)
    logger.debug(current_graph_state)

    # Check if graph is interrupted by mailcomposer
    if (
        len(current_graph_state.tasks) > 0
        and len(current_graph_state.tasks[0].interrupts) > 0
    ):
        command = Command(resume=Message(type="human", content="Alright"))
        # Send a signal to the graph to resume execution
        output_state = AGENT_GRAPH.invoke(command, config=runnable_config)

        logger.info(f"output message after interrupt: {output_state}")

    agent_state = AgentState(messages=output_state.get("messages", []))
    print(agent_state.model_dump_json(indent=2))


if __name__ == "__main__":
    echo_server_agent()  # type: ignore
