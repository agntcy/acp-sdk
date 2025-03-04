# RunError

Run terminated with an error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**run_id** | **str** | The ID of the run. | 
**errcode** | **int** | code of the error | 
**description** | **str** | description of the error | 

## Example

```python
from acp_client_v0_1.models.run_error import RunError

# TODO update the JSON string below
json = "{}"
# create an instance of RunError from a JSON string
run_error_instance = RunError.from_json(json)
# print the JSON string representation of the object
print(RunError.to_json())

# convert the object into a dict
run_error_dict = run_error_instance.to_dict()
# create an instance of RunError from a dict
run_error_from_dict = RunError.from_dict(run_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


