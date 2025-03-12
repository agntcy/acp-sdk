import logging
from agntcy_iomapper.langgraph import get_langgraph_io_mapper
from acp_sdk.langgraph import acp_node
from typing import Any, Union
from langgraph.graph import StateGraph

logger = logging.getLogger(__name__)

class IOMapperNode(acp_node.ACPNode):
    def __init__(self, name: str, iomapper_metadata: dict):
        self.__name__ = name
        self.metadata = iomapper_metadata
        if "output_fields" not in self.metadata:
            raise Exception("output_fields not found in the metadata")
        if "input_fields" not in self.metadata:
            raise Exception("input_fields not found in the metadata")


    def __call__(self, data: Any, config: dict):
        return get_langgraph_io_mapper(data, config, self.metadata).as_runnable()

def add_io_mapped_edge(g: StateGraph, start: Union[str, acp_node.ACPNode], end: Union[str, acp_node.ACPNode], iomapper_config:dict = {})->IOMapperNode:
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

        iom = IOMapperNode(f"{start_key}_{end_key}", iomapper_metadata=iomapper_config)
        g.add_node(iom)
        g.add_edge(start_key, iom.get_name())
        g.add_edge(iom.get_name(), end_key)
        return iom



def add_io_mapped_conditional_edge(g: StateGraph, start: Union[str, acp_node.ACPNode], path,
                                   iomapper_config_map: dict) -> dict:
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

        iom = IOMapperNode(f"{start_key}_{end_key}", iomapper_metadata=v["metadata"])
        g.add_node(iom)
        g.add_edge(iom.get_name(), end_key)
        iom_map[end_key] = iom
        condition_map[map_key] = iom.get_name()

    g.add_conditional_edges(start_key, path, condition_map)
    return iom_map


