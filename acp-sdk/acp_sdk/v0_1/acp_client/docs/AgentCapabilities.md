# AgentCapabilities

Declares what invocation features this agent is capable of.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threads** | **bool** | This is &#x60;true&#x60; if the agent supports run threads. If this is &#x60;false&#x60;, then the threads tagged with &#x60;Threads&#x60; are not available. If missing, it means &#x60;false&#x60; | [optional] [default to False]
**interrupts** | **bool** | This is &#x60;true&#x60; if the agent runs can interrupt to request additional input and can be subsequently resumed. If missing, it means &#x60;false&#x60; | [optional] [default to False]
**callbacks** | **bool** | This is &#x60;true&#x60; if the agent supports a webhook to report run results. If this is &#x60;false&#x60;, providing a &#x60;webhook&#x60; at run creation has no effect. If missing, it means &#x60;false&#x60; | [optional] [default to False]
**streaming** | [**StreamingModes**](StreamingModes.md) |  | [optional] 

## Example

```python
from acp_client_v0_1.models.agent_capabilities import AgentCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCapabilities from a JSON string
agent_capabilities_instance = AgentCapabilities.from_json(json)
# print the JSON string representation of the object
print(AgentCapabilities.to_json())

# convert the object into a dict
agent_capabilities_dict = agent_capabilities_instance.to_dict()
# create an instance of AgentCapabilities from a dict
agent_capabilities_from_dict = AgentCapabilities.from_dict(agent_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


