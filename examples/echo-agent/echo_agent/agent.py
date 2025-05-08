# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import asyncio
import logging
from typing import Any, Dict

from langchain_core.runnables import RunnableConfig
from langgraph.types import interrupt

from .state import AgentState, Message, MsgType

logger = logging.getLogger(__name__)


# Define agent function
async def echo_agent(state: AgentState, config: RunnableConfig) -> Dict[str, Any]:
    args = config.get("configurable", {})
    ai_response = None

    # Note: subfields are not typed when running in the workflow server
    # so we fix that here.
    messages = state.messages or []

    if messages:
        logger.debug(f"received messages: {messages}")
        # Get last human message
        human_message = next(
            filter(lambda m: m["type"] == MsgType.human, reversed(messages)),
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

    interrupt_messages = []
    if "interrupt" in args:
        answer_from_human = interrupt({"question": "Do you think this is correct"})
        await asyncio.sleep(2)

        interrupt_messages.append(answer_from_human)

    return {"messages": messages + output_messages + interrupt_messages}
