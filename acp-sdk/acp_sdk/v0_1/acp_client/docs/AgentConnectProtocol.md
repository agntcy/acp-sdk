# AgentConnectProtocol

ACP endpoint description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url** | **str** | URL pointing to the ACP endpoint root. | 
**agent_id** | **str** | Agent identifier in ACP server. If missing, the first returned agent with matching name and version should be used. | [optional] 
**authentication** | **object** | This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#security-scheme-object-0 | [optional] 

## Example

```python
from acp_client_v0_1.models.agent_connect_protocol import AgentConnectProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of AgentConnectProtocol from a JSON string
agent_connect_protocol_instance = AgentConnectProtocol.from_json(json)
# print the JSON string representation of the object
print(AgentConnectProtocol.to_json())

# convert the object into a dict
agent_connect_protocol_dict = agent_connect_protocol_instance.to_dict()
# create an instance of AgentConnectProtocol from a dict
agent_connect_protocol_from_dict = AgentConnectProtocol.from_dict(agent_connect_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


