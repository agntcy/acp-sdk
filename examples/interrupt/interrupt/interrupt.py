import asyncio
import uuid
from typing import Optional

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver
from langgraph.constants import END, START
from langgraph.graph import StateGraph
from langgraph.types import Command, interrupt
from typing_extensions import TypedDict


class State(TypedDict):
    """The graph state."""

    input: str
    """The input value of the node."""

    ai_answer: Optional[str]
    """AI answer"""

    human_answer: Optional[str]
    """Human value will be updated using an interrupt."""


class FirstInterrupt(TypedDict):
    """The first interrupt value."""

    ai_first_question: str
    """The question asked by the AI."""

    needs_answer: bool
    """Whether the interrupt needs a non-empty answer."""


class SecondInterrupt(TypedDict):
    """The second interrupt value."""

    ai_second_question: str
    """The question asked by the AI."""


class FirstInterruptAnswer(TypedDict):
    """The first interrupt answer."""

    answer: str
    """The answer given by the human."""


class SecondInterruptAnswer(TypedDict):
    """The second interrupt answer."""

    answer: str
    """The answer given by the human."""


async def node1(state: State):
    print(f"> Node1 input: {state['input']}")
    await asyncio.sleep(1)
    return {"ai_answer": "This is the output of node1"}


async def node2(state: State):
    print(f"> Received input: {state['ai_answer']}")
    needs_answer = True
    answer: FirstInterruptAnswer = interrupt(
        # This value will be sent to the client
        # as part of the interrupt information.
        FirstInterrupt(
            ai_first_question="What's your favorite color?",
            needs_answer=needs_answer,
        )
    )
    print(f"> Received an input from the 1st interrupt: {answer}")
    if needs_answer and not answer["answer"].strip():
        print("> The answer is empty, but it was required.")

    await asyncio.sleep(2)
    return {"human_answer": answer}


async def node3(state: State):
    answer = interrupt(
        # This value will be sent to the client
        # as part of the interrupt information.
        SecondInterrupt(
            ai_second_question="What's your favorite food?",
        )
    )
    print(f"> Received an input from the 2nd interrupt: {answer}")
    await asyncio.sleep(2)
    return {"human_answer": answer}


async def node4(state: State):
    print(f"> Received input: {state['human_answer']}")
    await asyncio.sleep(3)
    return {"ai_answer": "This is the output of node4"}


builder = StateGraph(State)
builder.add_node("node1", node1)
builder.add_node("node2", node2)
builder.add_node("node3", node3)
builder.add_node("node4", node4)

builder.add_edge(START, "node1")
builder.add_edge("node1", "node2")
builder.add_edge("node2", "node3")
builder.add_edge("node3", "node4")
builder.add_edge("node4", END)


# A checkpointer must be enabled for interrupts to work!
checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = RunnableConfig(
    configurable={"thread_id": uuid.uuid4()},
)


async def run_graph():
    async for chunk in graph.astream({"input": "something"}, config):
        print(chunk)

    first_anwer = input("Enter the 1st interrupt answer: ")
    command = Command(resume=FirstInterruptAnswer(answer=first_anwer))

    async for chunk in graph.astream(command, config):
        print(chunk)

    second_answer = input("Enter the 2nd interrupt answer: ")
    command = Command(resume=SecondInterruptAnswer(answer=second_answer))

    async for chunk in graph.astream(command, config):
        print(chunk)


if __name__ == "__main__":
    asyncio.run(run_graph())
