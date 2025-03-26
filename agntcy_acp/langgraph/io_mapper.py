# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import logging
from typing import Union

from agntcy_iomapper import IOMappingAgent, IOMappingAgentMetadata
from langchain_core.language_models import BaseChatModel
from langgraph.graph import StateGraph

from agntcy_acp.langgraph import acp_node

logger = logging.getLogger(__name__)


def add_io_mapped_edge(
    g: StateGraph,
    start: Union[str, acp_node.ACPNode],
    end: Union[str, acp_node.ACPNode],
    iomapper_config: IOMappingAgentMetadata,
    llm: BaseChatModel,
) -> IOMappingAgent:
    """
    Adds an I/O-mapped edge to a LangGraph StateGraph.

    Parameters:
        g: The LangGraph StateGraph to which the edge will be added.
        start: The starting node of the edge, which can be specified either as a string identifier or as an instance of an ACPNode.
        end: The ending node of the edge, which can be specified either as a string identifier or as an instance of an ACPNode.
        iomapper_config: A dictionary containing all the metadata necessary for the IO mapper agent to perform data translation. Defaults to an empty dictionary.
        llm: An instance of llm model

    Returns:
        None: This function modifies the graph in place by adding the specified edge.
    """
    if isinstance(start, str):
        start_key = start
    else:
        start_key = start.get_name()
        node: acp_node.ACPNode = start
        if "input_fields" not in iomapper_config:
            iomapper_config["input_fields"] = [node.outputPath]

    if isinstance(end, str):
        end_key = end
    else:
        end_key = end.get_name()
        node: acp_node.ACPNode = end
        if "output_fields" not in iomapper_config:
            iomapper_config["output_fields"] = [node.inputPath]

    mapping_agent = IOMappingAgent(metadata=iomapper_config, llm=llm)

    iom_name = f"{start_key}_{end_key}"
    g.add_node(iom_name, mapping_agent.langgraph_node)

    g.add_edge(start_key, iom_name)
    g.add_edge(iom_name, end_key)
    return mapping_agent


def add_io_mapped_conditional_edge(
    g: StateGraph,
    start: Union[str, acp_node.ACPNode],
    path,
    iomapper_config_map: dict,
    llm: BaseChatModel,
) -> dict:
    """
    Adds a conditional I/O-mapped edge to a LangGraph StateGraph.

    Parameters:
        g: The LangGraph StateGraph to which the conditional edge will be added.
        start: The starting node of the edge, which can be specified either as a string identifier or as an instance of an ACPNode.
        path: The conditional path that determines the conditions under which the edge will be traversed. The type and structure of 'path' should be specified based on its use case.
        iomapper_config_map: A dictionary containing metadata that the IO mapper agent requires for data translation. This map is used to configure the agent based on different conditions.
        llm: An instance of llm model
    Returns:
        None: This function modifies the graph in place by adding the specified conditional edge.
    """
    start_node = None
    if isinstance(start, str):
        start_key = start
    else:
        start_key = start.get_name()
        start_node: acp_node.ACPNode = start

    condition_map = {}
    iom_map = {}
    for map_key, v in iomapper_config_map.items():
        end_node = None
        if isinstance(v["end"], str):
            end_key = v["end"]
        else:
            end_key = v["end"].get_name()
            end_node = v["end"]

        if v["metadata"] is None:
            # No IO Mapper is needed
            condition_map[map_key] = end_key
        else:
            if start_node and "input_fields" not in v["metadata"]:
                v["metadata"]["input_fields"] = [start_node.outputPath]
            if end_node and "output_fields" not in v["metadata"]:
                v["metadata"]["output_fields"] = [end_node.inputPath]

            mapping_agent = IOMappingAgent(metadata=v["metadata"], llm=llm)

            iom_name = f"{start_key}_{end_key}"
            g.add_node(iom_name, mapping_agent.langgraph_node)
            g.add_edge(iom_name, end_key)
            iom_map[end_key] = mapping_agent
            condition_map[map_key] = iom_name

    g.add_conditional_edges(start_key, path, condition_map)
    return iom_map
