import logging
from agntcy_iomapper import IOMappingAgentMetadata, IOMappingAgent
from langchain_core.language_models import BaseChatModel
from agntcy_acp.langgraph import acp_node
from typing import Any, Union
from langgraph.graph import StateGraph

logger = logging.getLogger(__name__)


def add_io_mapped_edge(g: StateGraph, start: Union[str, acp_node.ACPNode], end: Union[str, acp_node.ACPNode], iomapper_config:IOMappingAgentMetadata, llm: BaseChatModel)->IOMappingAgent:
        if isinstance(start, str):
            start_key = start
        else:
            start_key=start.get_name()
            node:acp_node.ACPNode = start
            if "input_fields" not in iomapper_config:
                iomapper_config["input_fields"] = [node.outputPath]

        if isinstance(end, str):
            end_key = end
        else:
            end_key=end.get_name()
            node:acp_node.ACPNode = end
            if "output_fields" not in iomapper_config:
                iomapper_config["output_fields"] = [node.inputPath]


        mapping_agent = IOMappingAgent(metadata=iomapper_config, llm=llm)

        iom_name = f"{start_key}_{end_key}"
        g.add_node(iom_name, mapping_agent.langgraph_node)

        g.add_edge(start_key, iom_name)
        g.add_edge(iom_name, end_key)
        return mapping_agent



def add_io_mapped_conditional_edge(g: StateGraph, start: Union[str, acp_node.ACPNode], path,
                                   iomapper_config_map: dict, llm: BaseChatModel) -> dict:
    start_node = None
    if isinstance(start, str):
        start_key = start
    else:
        start_key = start.get_name()
        start_node: acp_node.ACPNode = start

    condition_map = {}
    iom_map={}
    for map_key, v in iomapper_config_map.items():
        end_node = None
        if isinstance(v["end"], str):
            end_key = v["end"]
        else:
            end_key = v["end"].get_name()
            end_node = v["end"]

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


