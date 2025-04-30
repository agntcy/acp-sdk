Module agntcy_acp.langgraph.io_mapper
=====================================

Functions
---------

`add_io_mapped_conditional_edge(g: langgraph.graph.state.StateGraph, start: str | agntcy_acp.langgraph.acp_node.ACPNode, path, iomapper_config_map: dict, llm: langchain_core.language_models.chat_models.BaseChatModel) ‑> dict`
:   Adds a conditional I/O-mapped edge to a LangGraph StateGraph.
    
    Parameters:
        g: The LangGraph StateGraph to which the conditional edge will be added.
        start: The starting node of the edge, which can be specified either as a string identifier or as an instance of an ACPNode.
        path: The conditional path that determines the conditions under which the edge will be traversed. The type and structure of 'path' should be specified based on its use case.
        iomapper_config_map: A dictionary containing metadata that the IO mapper agent requires for data translation. This map is used to configure the agent based on different conditions.
        llm: An instance of llm model
    Returns:
        None: This function modifies the graph in place by adding the specified conditional edge.

`add_io_mapped_edge(g: langgraph.graph.state.StateGraph, start: str | agntcy_acp.langgraph.acp_node.ACPNode, end: str | agntcy_acp.langgraph.acp_node.ACPNode, iomapper_config: agntcy_iomapper.base.models.IOMappingAgentMetadata, llm: langchain_core.language_models.chat_models.BaseChatModel) ‑> agntcy_iomapper.agent.agent_io_mapper.IOMappingAgent`
:   Adds an I/O-mapped edge to a LangGraph StateGraph.
    
    Parameters:
        g: The LangGraph StateGraph to which the edge will be added.
        start: The starting node of the edge, which can be specified either as a string identifier or as an instance of an ACPNode.
        end: The ending node of the edge, which can be specified either as a string identifier or as an instance of an ACPNode.
        iomapper_config: A dictionary containing all the metadata necessary for the IO mapper agent to perform data translation. Defaults to an empty dictionary.
        llm: An instance of llm model
    
    Returns:
        None: This function modifies the graph in place by adding the specified edge.