# ThreadSearchRequest

Payload for listing runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Matches all threads associated with the specified agent ID. | [optional] 
**metadata** | **object** | Matches all threads for which metadata has  keys and values equal to those specified in this object. | [optional] 
**limit** | **int** | Maximum number to return. | [optional] [default to 10]
**offset** | **int** | Offset to start from. | [optional] [default to 0]

## Example

```python
from acp_client_v0_1.models.thread_search_request import ThreadSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadSearchRequest from a JSON string
thread_search_request_instance = ThreadSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ThreadSearchRequest.to_json())

# convert the object into a dict
thread_search_request_dict = thread_search_request_instance.to_dict()
# create an instance of ThreadSearchRequest from a dict
thread_search_request_from_dict = ThreadSearchRequest.from_dict(thread_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


