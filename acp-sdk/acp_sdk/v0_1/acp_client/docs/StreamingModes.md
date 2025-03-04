# StreamingModes

Supported streaming modes. If missing, streaming is not supported.  If no mode is supported attempts to stream output will result in an error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | This is &#x60;true&#x60; if the agent supports result streaming. If &#x60;false&#x60; or missing, result streaming is not supported. Result streaming consists of a stream of objects of type &#x60;RunResult&#x60;, where each one sent over the stream fully replace the previous one. | [optional] 
**custom** | **bool** | This is &#x60;true&#x60; if the agent supports custom objects streaming. If &#x60;false&#x60; or missing, custom streaming is not supported. Custom Objects streaming consists of a stream of object whose schema is specified by the agent in its manifest under &#x60;specs.custom_streaming_update&#x60;. | [optional] 

## Example

```python
from acp_client_v0_1.models.streaming_modes import StreamingModes

# TODO update the JSON string below
json = "{}"
# create an instance of StreamingModes from a JSON string
streaming_modes_instance = StreamingModes.from_json(json)
# print the JSON string representation of the object
print(StreamingModes.to_json())

# convert the object into a dict
streaming_modes_dict = streaming_modes_instance.to_dict()
# create an instance of StreamingModes from a dict
streaming_modes_from_dict = StreamingModes.from_dict(streaming_modes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


