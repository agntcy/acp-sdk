Module agntcy_acp.acp_v0.api_response
=====================================
API response object.

Classes
-------

`ApiResponse(**data: Any)`
:   API response object
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * typing.Generic

    ### Descendants

    * agntcy_acp.acp_v0.api_response.ApiResponse[AgentACPDescriptor]
    * agntcy_acp.acp_v0.api_response.ApiResponse[Agent]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[Agent]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[RunStateful]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[RunStateless]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[ThreadState]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[Thread]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunStateful]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunStateless]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateful]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateless]
    * agntcy_acp.acp_v0.api_response.ApiResponse[Thread]

    ### Class variables

    `data: ~T`
    :   The type of the None singleton.

    `headers: Mapping[str, str] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `raw_data: bytes`
    :   The type of the None singleton.

    `status_code: int`
    :   The type of the None singleton.