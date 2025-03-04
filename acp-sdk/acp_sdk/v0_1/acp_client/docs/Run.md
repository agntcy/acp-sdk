# Run

Holds all the information of a run

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation** | [**RunCreate**](RunCreate.md) |  | 
**run_id** | **str** | The ID of the run. | 
**agent_id** | **str** | The agent that was used for this run. | 
**thread_id** | **str** | Optional Thread ID wher the Run belongs to. This is populated only for runs on agents agents supporting Threads. | [optional] 
**created_at** | **datetime** | The time the run was created. | 
**updated_at** | **datetime** | The last time the run was updated. | 
**status** | [**RunStatus**](RunStatus.md) | The status of the run. One of &#39;pending&#39;, &#39;error&#39;, &#39;success&#39;, &#39;timeout&#39;, &#39;interrupted&#39;. | 

## Example

```python
from acp_client_v0_1.models.run import Run

# TODO update the JSON string below
json = "{}"
# create an instance of Run from a JSON string
run_instance = Run.from_json(json)
# print the JSON string representation of the object
print(Run.to_json())

# convert the object into a dict
run_dict = run_instance.to_dict()
# create an instance of Run from a dict
run_from_dict = Run.from_dict(run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


