from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
from typing import List
import mailcomposer
import state
import iomappers
from acp_sdk.langgraph import ACPNode
from acp_sdk import Configuration
from agntcy_iomapper.langgraph import create_langraph_iomapper, LangGraphIOMapperConfig, io_mapper_node
from agntcy_iomapper import AgentIOMapperInput


def build_graph()->StateGraph:
    # Fill in client configuration for the remote agent
    mailcomposer_client_config = Configuration(
        #api_key={"api_key":"test_api_key"},
        host="http://localhost:8000")

    # Instantiate the local ACP node for the remote agent
    acp_mailcomposer = ACPNode(
        name="mailcomposer",
        inputModel=mailcomposer.Input,
        outputModel=mailcomposer.Output,
        clientConfig=mailcomposer_client_config,
        agentConfig=None)

    # Create the state graph
    # State must inherith ACPState
    sg =  StateGraph(state.State, input=state.InputState, output=state.OutputState)

    # Add
    sg.add_node(
        acp_mailcomposer.name,
        acp_mailcomposer.as_runnable()
    )

    iom1 = iomappers.IoMapper1("iom1")
    sg.add_node("iom1", iom1)
    iom2 = iomappers.IoMapper2("iom2")
    sg.add_node("iom2", iom2)

    sg.add_edge(START, "iom1")
    sg.add_edge("iom1", acp_mailcomposer.name)
    sg.add_edge(acp_mailcomposer.name, "iom2")
    sg.add_edge("iom2",END)

    # sg.add_node(
    #     "mailcomposer",
    #     sdk.acp_node,
    #     metadata={
    #
    #     }
    # )
    #
    #
    # sg.add_node(
    #     "iom1",
    #     io_mapper_node,
    #     metadata={
    #         "input_fields": ["description"],
    #         "output_fields": [f"{mc.statekey}.input"],
    #     },
    # )
    # iom2 = iomappers.IoMapper2("iom2")
    # sg.add_node(iom2.name, iom2)
    #
    #
    # sg.add_edge("iom1", mc.name)
    # sg.add_edge(mc.name, iom2.name)
    # sg.add_edge(iom2.name, END)

    g = sg.compile()
    g.name = "Marketing Campaign Manager"

    return g

graph = build_graph()

