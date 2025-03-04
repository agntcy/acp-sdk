# CustomRunResultUpdate

Object holding a custom defined update of the agent result during streaming.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**run_id** | **str** | The ID of the run. | 
**status** | [**RunStatus**](RunStatus.md) | Status of the Run when this result was generated | 
**update** | **object** | An update in the SSE event streaming where streaming mode is set to custom. The schema is described in Agent Manifest under &#39;spec.custom_streaming_update&#39;. | 

## Example

```python
from acp_client_v0_1.models.custom_run_result_update import CustomRunResultUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRunResultUpdate from a JSON string
custom_run_result_update_instance = CustomRunResultUpdate.from_json(json)
# print the JSON string representation of the object
print(CustomRunResultUpdate.to_json())

# convert the object into a dict
custom_run_result_update_dict = custom_run_result_update_instance.to_dict()
# create an instance of CustomRunResultUpdate from a dict
custom_run_result_update_from_dict = CustomRunResultUpdate.from_dict(custom_run_result_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


