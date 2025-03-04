# ThreadCreate

Detail of an empty thread to be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Identifier of the agent this thread is executed on | 
**metadata** | **object** | Free form metadata for this thread | [optional] 

## Example

```python
from acp_client_v0_1.models.thread_create import ThreadCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadCreate from a JSON string
thread_create_instance = ThreadCreate.from_json(json)
# print the JSON string representation of the object
print(ThreadCreate.to_json())

# convert the object into a dict
thread_create_dict = thread_create_instance.to_dict()
# create an instance of ThreadCreate from a dict
thread_create_from_dict = ThreadCreate.from_dict(thread_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


