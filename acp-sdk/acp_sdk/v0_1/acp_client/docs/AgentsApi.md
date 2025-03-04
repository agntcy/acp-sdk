# acp_client_v0_1.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_by_id**](AgentsApi.md#get_agent_by_id) | **GET** /agents/{agent_id} | Get Agent
[**get_agent_manifest_by_id**](AgentsApi.md#get_agent_manifest_by_id) | **GET** /agents/{agent_id}/manifest | Get Agent Manifest from its id
[**search_agents**](AgentsApi.md#search_agents) | **POST** /agents/search | Search Agents


# **get_agent_by_id**
> Agent get_agent_by_id(agent_id)

Get Agent

Get an agent by ID.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.agent import Agent
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.

    try:
        # Get Agent
        api_response = api_instance.get_agent_by_id(agent_id)
        print("The response of AgentsApi->get_agent_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 

### Return type

[**Agent**](Agent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_manifest_by_id**
> AgentManifest get_agent_manifest_by_id(agent_id)

Get Agent Manifest from its id

Get an agent manifest by agent ID.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.agent_manifest import AgentManifest
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.

    try:
        # Get Agent Manifest from its id
        api_response = api_instance.get_agent_manifest_by_id(agent_id)
        print("The response of AgentsApi->get_agent_manifest_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_manifest_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 

### Return type

[**AgentManifest**](AgentManifest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_agents**
> List[Agent] search_agents(agent_search_request)

Search Agents

Returns a list of agents matching the criteria provided in the request.

This endpoint also functions as the endpoint to list all agents.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.agent import Agent
from acp_client_v0_1.models.agent_search_request import AgentSearchRequest
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.AgentsApi(api_client)
    agent_search_request = acp_client_v0_1.AgentSearchRequest() # AgentSearchRequest | 

    try:
        # Search Agents
        api_response = api_instance.search_agents(agent_search_request)
        print("The response of AgentsApi->search_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->search_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_search_request** | [**AgentSearchRequest**](AgentSearchRequest.md)|  | 

### Return type

[**List[Agent]**](Agent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

