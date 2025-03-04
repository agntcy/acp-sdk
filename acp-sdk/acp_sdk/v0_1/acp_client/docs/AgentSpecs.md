# AgentSpecs

Specification of agent capabilities, config, input, output, and interrupts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**AgentCapabilities**](AgentCapabilities.md) |  | 
**input** | **object** | This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object | 
**output** | **object** | This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object | 
**custom_streaming_update** | **object** | This describes the format of an Update in the streaming.  Must be specified if &#x60;streaming.custom&#x60; capability is true and cannot be specified otherwise. Format follows: https://spec.openapis.org/oas/v3.1.1.html#schema-object | [optional] 
**thread_state** | **object** | This describes the format of ThreadState.  Cannot be specified if &#x60;threads&#x60; capability is false. If not specified, when &#x60;threads&#x60; capability is true, then the API to retrieve ThreadState from a Thread or a Run is not available. This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object | [optional] 
**config** | **object** | This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object | 
**interrupts** | [**List[AgentSpecsInterruptsInner]**](AgentSpecsInterruptsInner.md) | List of possible interrupts that can be provided by the agent. If &#x60;interrupts&#x60; capability is true, this needs to have at least one item. | [optional] 

## Example

```python
from acp_client_v0_1.models.agent_specs import AgentSpecs

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSpecs from a JSON string
agent_specs_instance = AgentSpecs.from_json(json)
# print the JSON string representation of the object
print(AgentSpecs.to_json())

# convert the object into a dict
agent_specs_dict = agent_specs_instance.to_dict()
# create an instance of AgentSpecs from a dict
agent_specs_from_dict = AgentSpecs.from_dict(agent_specs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


