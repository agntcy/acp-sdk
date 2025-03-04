# RunResult

Final result of a Run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**run_id** | **str** | The ID of the run. | 
**status** | [**RunStatus**](RunStatus.md) | Status of the Run when this result was generated. This is particurarly useful when this data structure is used for streaming results. As the server can indicate an interrupt or an error condition while streaming the result. | 
**result** | **object** | The output of the agent. The schema is described in Agent Manifest under &#39;spec.output&#39;. | 

## Example

```python
from acp_client_v0_1.models.run_result import RunResult

# TODO update the JSON string below
json = "{}"
# create an instance of RunResult from a JSON string
run_result_instance = RunResult.from_json(json)
# print the JSON string representation of the object
print(RunResult.to_json())

# convert the object into a dict
run_result_dict = run_result_instance.to_dict()
# create an instance of RunResult from a dict
run_result_from_dict = RunResult.from_dict(run_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


