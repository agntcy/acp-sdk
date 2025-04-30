Module agntcy_acp.langgraph.acp_node
====================================

Classes
-------

`ACPNode(name: str, agent_id: str, client_config: agntcy_acp.ApiClientConfiguration, input_path: str, input_type, output_path: str, output_type, config_path: str | None = None, config_type=None, auth_header: Dict | None = None)`
:   This class represents a Langgraph Node that holds a remote connection to an ACP Agent
    It can be instantiated and added to any langgraph graph.
    
    my_node = ACPNode(...)
    sg = StateGraph(GraphState)
    sg.add_node(my_node)
    
    Instantiate a Langgraph node encapsulating a remote ACP agent
    
    :param name: Name of the langgraph node
    :param agent_id: Agent ID in the remote server
    :param client_config: Configuration of the ACP Client
    :param input_path: Dot-separated path of the ACP Agent input in the graph overall state
    :param input_type: Pydantic class defining the schema of the ACP Agent input
    :param output_path: Dot-separated path of the ACP Agent output in the graph overall state
    :param output_type: Pydantic class defining the schema of the ACP Agent output
    :param config_path: Dot-separated path of the ACP Agent config in the graph configurable
    :param config_type: Pydantic class defining the schema of the ACP Agent config
    :param auth_header: A dictionary containing auth details necessary to communicate with the node

    ### Descendants

    * agntcy_acp.langgraph.api_bridge.APIBridgeAgentNode

    ### Methods

    `ainvoke(self, state: Any, config: langchain_core.runnables.config.RunnableConfig) ‑> Any`
    :

    `get_name(self)`
    :

    `invoke(self, state: Any, config: langchain_core.runnables.config.RunnableConfig) ‑> Any`
    :