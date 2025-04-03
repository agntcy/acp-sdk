# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import itertools
import logging

import click
from langchain_core.runnables import RunnableConfig

from .langgraph import AGENT_GRAPH
from .state import AgentState, ConfigSchema, InputState, Message, MsgType

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
    help="Convert input to upper case.",
)
@click.option(
    "--to-lower",
    envvar="TO_LOWER",
    is_flag=True,
    show_envvar=True,
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
def echo_server_agent(
    to_upper,
    to_lower,
    human,
    assistant,
    log_level,
):
    """ """
    logging.basicConfig(level=log_level.upper())

    config = ConfigSchema()
    if to_upper is not None:
        config["to_upper"] = to_upper
    if to_lower is not None:
        config["to_lower"] = to_lower
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

    echo_input = InputState(messages=messages)
    logger.debug(f"input messages: {echo_input.model_dump_json()}")

    # Imitate input from ACP API
    input_api_object = AgentState(echo_input=echo_input).model_dump(mode="json")

    output_state = AGENT_GRAPH.invoke(
        AGENT_GRAPH.builder.schema.model_validate(input_api_object),
        config=RunnableConfig(configurable=config),
    )

    logger.debug(f"output messages: {output_state}")
    print(output_state["echo_output"].model_dump_json(indent=2))


if __name__ == "__main__":
    echo_server_agent()  # type: ignore
