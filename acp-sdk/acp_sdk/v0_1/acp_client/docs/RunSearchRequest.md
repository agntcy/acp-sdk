# RunSearchRequest

Payload for listing runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Matches all the Runs associated with the specified Agent ID. | [optional] 
**status** | [**RunStatus**](RunStatus.md) | Matches all the Runs associated with the specified status. One of &#39;pending&#39;, &#39;error&#39;, &#39;success&#39;, &#39;timeout&#39;, &#39;interrupted&#39;. | [optional] 
**metadata** | **object** | Matches all threads for which metadata has  keys and values equal to those specified in this object. | [optional] 
**limit** | **int** | Maximum number to return. | [optional] [default to 10]
**offset** | **int** | Offset to start from. | [optional] [default to 0]

## Example

```python
from acp_client_v0_1.models.run_search_request import RunSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunSearchRequest from a JSON string
run_search_request_instance = RunSearchRequest.from_json(json)
# print the JSON string representation of the object
print(RunSearchRequest.to_json())

# convert the object into a dict
run_search_request_dict = run_search_request_instance.to_dict()
# create an instance of RunSearchRequest from a dict
run_search_request_from_dict = RunSearchRequest.from_dict(run_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


