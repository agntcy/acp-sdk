# RunCreate

Payload for creating a run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | The ID of the agent. | 
**thread_id** | **str** | Optional Thread ID wher the Run belongs to. This can be used only for agents supporting Threads. | [optional] 
**input** | **object** | The input to the agent. The schema is described in Agent Manifest under &#39;spec.thread_state&#39;.&#39;input&#39;. | [optional] 
**metadata** | **object** | Metadata to assign to the run. Optional free format metadata to attach to the run. | [optional] 
**config** | **object** | The configuration for this agent. The schema is described in Agent Manifest under &#39;spec.config&#39;. If missing, default values are used. | [optional] 
**webhook** | **str** | Webhook to call upon change of run status. This is a url that accepts a POST containing the &#x60;Run&#x60; object as body. See Callbacks definition. | [optional] 
**streaming** | [**StreamingMode**](StreamingMode.md) | If populated, indicates that the client requests to stream results with the specified streaming mode. The requested streaming mode must be one of the one supported by the agent as declared in its manifest under &#x60;specs.capabilities&#x60; | [optional] 

## Example

```python
from acp_client_v0_1.models.run_create import RunCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RunCreate from a JSON string
run_create_instance = RunCreate.from_json(json)
# print the JSON string representation of the object
print(RunCreate.to_json())

# convert the object into a dict
run_create_dict = run_create_instance.to_dict()
# create an instance of RunCreate from a dict
run_create_from_dict = RunCreate.from_dict(run_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


