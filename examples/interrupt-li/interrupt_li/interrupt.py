# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import asyncio
from typing import Any

from dotenv import find_dotenv, load_dotenv
from llama_index.core.agent.react import ReActChatFormatter, ReActOutputParser
from llama_index.core.llms.llm import LLM
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.tools.types import BaseTool
from llama_index.core.workflow import (
    Context,
    Event,
    StartEvent,
    StopEvent,
    Workflow,
    step,
)

load_dotenv(dotenv_path=find_dotenv(usecwd=True))


class HumanMessage(Event):
    human_answer: str


class FirstEvent(Event):
    ai_answer: str


class SecondEvent(Event):
    ai_answer: str


class ThirdEvent(Event):
    ai_answer: str


class FirstInterruptEvent(Event):
    first_question: str
    needs_answer: bool


class SecondInterruptEvent(Event):
    second_question: str


class InterruptResponseEvent(Event):
    answer: str


class Interrupt(Workflow):
    def __init__(
        self,
        *args: Any,
        llm: LLM | None = None,
        tools: list[BaseTool] | None = None,
        extra_context: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.tools = tools or []

        self.llm = llm

        self.memory = ChatMemoryBuffer.from_defaults(llm=llm)
        self.formatter = ReActChatFormatter.from_defaults(context=extra_context or "")
        self.output_parser = ReActOutputParser()
        self.sources = []

    @step
    async def first_step(self, ev: StartEvent) -> FirstEvent:
        print(f"> first_step input: {ev.input}")
        await asyncio.sleep(1)
        return FirstEvent(ai_answer="This is the output of first_step")

    @step
    async def step_interrupt_one(self, ctx: Context, ev: FirstEvent) -> SecondEvent:
        print(f"> step_interrupt_one input : {ev.ai_answer}")
        await asyncio.sleep(1)
        # wait until we see a HumanResponseEvent
        needs_answer = True
        response = await ctx.wait_for_event(
            InterruptResponseEvent,
            waiter_id="waiter_step_interrupt_one",
            waiter_event=FirstInterruptEvent(
                first_question="What's your favorite color?", needs_answer=needs_answer
            ),
        )

        if needs_answer and not response.answer:
            raise ValueError("This needs a non-empty answer")

        return SecondEvent(ai_answer=f"Received human answer: {response.answer}")

    @step
    async def step_interrupt_two(self, ctx: Context, ev: SecondEvent) -> ThirdEvent:
        print(f"> step_interrupt_two input : {ev.ai_answer}")
        await asyncio.sleep(1)
        response = await ctx.wait_for_event(
            InterruptResponseEvent,
            waiter_id="waiter_step_interrupt_two",
            waiter_event=SecondInterruptEvent(
                second_question="What's your favorite movie?"
            ),
        )

        return ThirdEvent(ai_answer=f"Received human answer: {response.answer}")

    @step
    async def last_step(self, ev: ThirdEvent) -> StopEvent:
        print(f"> last_step input: {ev.ai_answer}")
        await asyncio.sleep(1)
        return StopEvent(result={"ai_answer": "This is the output of last_step"})


def interrupt_workflow() -> Interrupt:
    interrupt_workflow = Interrupt(timeout=None, verbose=True)
    return interrupt_workflow


async def main():
    workflow = interrupt_workflow()

    # print(await workflow.run(email=email_example, target_audience=audience_example))

    response = "Hello"
    handler = workflow.run(input=response)
    ctx = handler.ctx

    async for ev in handler.stream_events():
        print(type(ev), ev)
        if isinstance(ev, FirstInterruptEvent):
            # capture keyboard input
            response = input(ev.first_question)
            ctx = handler.ctx
            break
            # send our response back

    handler2 = workflow.run(ctx=ctx)

    handler2.ctx.send_event(
        InterruptResponseEvent(
            answer=response,
        )
    )

    async for ev in handler2.stream_events():
        print(type(ev), ev)
        if isinstance(ev, SecondInterruptEvent):
            # capture keyboard input
            response = input(ev.second_question)
            ctx = handler2.ctx
            break

    handler3 = workflow.run(ctx=ctx)

    handler3.ctx.send_event(
        InterruptResponseEvent(
            answer=response,
        )
    )

    async for ev in handler3.stream_events():
        print(type(ev), ev)

    final_result = await handler3
    print("Final result: ", final_result)


if __name__ == "__main__":
    asyncio.run(main())
