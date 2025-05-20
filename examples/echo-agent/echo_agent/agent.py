# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import asyncio
import logging
import os
from typing import Any, Dict

from langchain_core.runnables import RunnableConfig
from langgraph.types import interrupt

from .state import AgentState, Message, MsgType

logger = logging.getLogger(__name__)


# Define agent function
async def echo_agent(state: AgentState, config: RunnableConfig) -> Dict[str, Any]:
    args = config.get("configurable", {})
    output_messages = []

    if state.messages:
        logger.debug(f"received messages: {state.messages}")
        # Get last human message
        human_message = next(
            filter(lambda m: m.type == MsgType.human, reversed(state.messages)),
            None,
        )
        if human_message is not None:
            ai_response = human_message.content

            to_upper = args.get("to_upper", os.getenv("TO_UPPER"))
            if to_upper is not None and bool(to_upper):
                ai_response = ai_response.upper()
            
            to_lower = args.get("to_lower", os.getenv("TO_LOWER"))
            if to_lower is not None and bool(to_lower):
                    ai_response = ai_response.lower()
            
            output_messages = [Message(type=MsgType.assistant, content=ai_response)]

    if args.get("interrupt", False):
        output_messages = interrupt(output_messages)
        await asyncio.sleep(2)

    return {"messages": state.messages + output_messages}
