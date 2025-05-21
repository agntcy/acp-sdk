# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import asyncio
import logging
from typing import Any, Dict, List, Optional

from langgraph.types import interrupt
from pydantic import RootModel

from .state import AgentState, Message, MessageList, MsgType

logger = logging.getLogger(__name__)


def _add_echo_message(
    messages: Optional[MessageList], to_upper: bool, to_lower: bool
) -> Optional[MessageList]:
    if not messages:
        return messages

    logger.debug(f"input messages: {messages}")
    # Get last human message
    human_message = next(
        filter(lambda m: m.type == MsgType.human, reversed(messages)),
        None,
    )
    if human_message is None:
        logger.debug("no human message found")
        return messages

    ai_response = human_message.content

    if to_lower:
        ai_response = ai_response.lower()
    elif to_upper:
        ai_response = ai_response.upper()

    messages.append(Message(type=MsgType.assistant, content=ai_response))
    return messages


# Define agent function
async def echo_agent(state: AgentState) -> Dict[str, Any]:
    logger.debug(f"starting state: {state}")
    output_messages = _add_echo_message(state.messages, state.to_upper, state.to_lower)

    if state.interrupt_left > 0:
        state.interrupt_left -= 1
        # Note: the workflow server checks the interrupt data against the schema
        # and requires base Python typing to do that.
        all_messages = RootModel[List[Message]].model_construct(output_messages)
        resume_input = interrupt({"messages": all_messages.model_dump(mode="json")})
        await asyncio.sleep(state.sleep_secs)

        resume_messages = [Message(**msg) for msg in resume_input.get("messages", [])]

        output_messages = _add_echo_message(
            resume_messages, state.to_upper, state.to_lower
        )

    logger.debug(f"output messages: {output_messages}")
    return {"messages": output_messages}
