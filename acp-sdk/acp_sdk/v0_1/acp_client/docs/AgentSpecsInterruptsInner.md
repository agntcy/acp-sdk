# AgentSpecsInterruptsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interrupt_type** | **str** | Name of this interrupt type. Needs to be unique in the list of interrupts. | 
**interrupt_payload** | **object** | This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object | 
**resume_payload** | **object** | This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object | 

## Example

```python
from acp_client_v0_1.models.agent_specs_interrupts_inner import AgentSpecsInterruptsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSpecsInterruptsInner from a JSON string
agent_specs_interrupts_inner_instance = AgentSpecsInterruptsInner.from_json(json)
# print the JSON string representation of the object
print(AgentSpecsInterruptsInner.to_json())

# convert the object into a dict
agent_specs_interrupts_inner_dict = agent_specs_interrupts_inner_instance.to_dict()
# create an instance of AgentSpecsInterruptsInner from a dict
agent_specs_interrupts_inner_from_dict = AgentSpecsInterruptsInner.from_dict(agent_specs_interrupts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


