# RunOutputStream

Server-sent event containing one agent output event. Actual event type is carried inside the data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the event | 
**event** | **str** | Event type. This is the constant string &#x60;agent_event&#x60; to be compatible with SSE spec. The actual type differentiation is done in the event itself. | 
**data** | [**StreamEventPayload**](StreamEventPayload.md) |  | 

## Example

```python
from acp_client_v0_1.models.run_output_stream import RunOutputStream

# TODO update the JSON string below
json = "{}"
# create an instance of RunOutputStream from a JSON string
run_output_stream_instance = RunOutputStream.from_json(json)
# print the JSON string representation of the object
print(RunOutputStream.to_json())

# convert the object into a dict
run_output_stream_dict = run_output_stream_instance.to_dict()
# create an instance of RunOutputStream from a dict
run_output_stream_from_dict = RunOutputStream.from_dict(run_output_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


