# Thread

Represents a collection of consecutive runs on an agent. Thread is associated with a state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | unique identifier of a thread | 
**agent_id** | **str** | Identifier of the agent this thread is executed on | 
**metadata** | **object** | Free form metadata for this thread | [optional] 

## Example

```python
from acp_client_v0_1.models.thread import Thread

# TODO update the JSON string below
json = "{}"
# create an instance of Thread from a JSON string
thread_instance = Thread.from_json(json)
# print the JSON string representation of the object
print(Thread.to_json())

# convert the object into a dict
thread_dict = thread_instance.to_dict()
# create an instance of Thread from a dict
thread_from_dict = Thread.from_dict(thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


