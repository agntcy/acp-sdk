# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import logging
from typing import Any, Dict

from langchain_core.runnables import RunnableConfig

from .state import AgentState, Message, MsgType, OutputState

logger = logging.getLogger(__name__)


# Define agent function
def echo_agent(state: AgentState, config: RunnableConfig) -> Dict[str, Any]:
    args = config.get("configurable", {})
    logger.debug(f"enter --- state: {state.model_dump_json()}, config: {args}")
    ai_response = None

    # Note: subfields are not typed when running in the workflow server
    # so we fix that here.
    if hasattr(state.echo_input, "messages"):
        messages = getattr(state.echo_input, "messages")
    elif "messages" in state.echo_input:
        messages = [Message.model_validate(m) for m in state.echo_input["messages"]]
    else:
        messages = []

    if messages is not None:
        # Get last human message
        human_message = next(
            filter(lambda m: m.type == MsgType.human, reversed(messages)),
            None,
        )
        if human_message is not None:
            ai_response = human_message.content

    if "to_upper" in args:
        to_upper = args["to_upper"]
        if bool(to_upper) and ai_response is not None:
            ai_response = ai_response.upper()
    if "to_lower" in args:
        to_lower = args["to_lower"]
        if bool(to_lower) and ai_response is not None:
            ai_response = ai_response.lower()

    if ai_response is not None:
        output_messages = [Message(type=MsgType.assistant, content=ai_response)]
    else:
        output_messages = []

    return {"echo_output": OutputState(messages=messages + output_messages)}
