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

def process_inputs(state: state.OverallState) -> state.OverallState:
    user_message = state.messages[-1].content
    
    if user_message.upper() == "OK":
        state.has_composer_completed = True

    return state

def check_inputs(state: state.OverallState):
    return "mailcomposer"

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
    sg =  StateGraph(state.OverallState)# input=state.InputState, output=state.OutputState)

    sg.add_node(
        "process_inputs",
        process_inputs
    )
    # Add
    sg.add_node(
        acp_mailcomposer.name,
        acp_mailcomposer.as_runnable()
    )

    iom1 = iomappers.IoMapper1("iom1")
    sg.add_node("iom1", iom1)
    iom2 = iomappers.IoMapper2("iom2")
    sg.add_node("iom2", iom2)

    sg.add_edge(START, "process_inputs")
    sg.add_conditional_edges("process_inputs", check_inputs, path_map={"mailcomposer": "iom1", "done": "iom2"})
    sg.add_edge("iom1", acp_mailcomposer.name)
    sg.add_edge(acp_mailcomposer.name, "iom2")
    sg.add_edge("iom2",END)

    g = sg.compile()
    g.name = "Marketing Campaign Manager"

    return g

graph = build_graph()

