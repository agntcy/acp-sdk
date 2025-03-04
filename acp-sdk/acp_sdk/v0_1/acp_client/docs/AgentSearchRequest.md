# AgentSearchRequest

Payload for listing agents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Match all agents with the name specified. | [optional] 
**version** | **str** | Match all agents with the version specified. Formatted according to semantic versioning (https://semver.org) | [optional] 
**limit** | **int** | Maximum number to return. | [optional] [default to 10]
**offset** | **int** | Offset to start from. | [optional] [default to 0]

## Example

```python
from acp_client_v0_1.models.agent_search_request import AgentSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchRequest from a JSON string
agent_search_request_instance = AgentSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AgentSearchRequest.to_json())

# convert the object into a dict
agent_search_request_dict = agent_search_request_instance.to_dict()
# create an instance of AgentSearchRequest from a dict
agent_search_request_from_dict = AgentSearchRequest.from_dict(agent_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


