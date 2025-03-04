# StreamEventPayload

A serialized JSON data structure carried in the SSE event data field. The event can carry either a full `RunResult`, if streaming mode is `result` or an custom update if streaming mode is `custom`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**run_id** | **str** | The ID of the run. | 
**status** | [**RunStatus**](RunStatus.md) | Status of the Run when this result was generated | 
**result** | **object** | The output of the agent. The schema is described in Agent Manifest under &#39;spec.output&#39;. | 
**update** | **object** | An update in the SSE event streaming where streaming mode is set to custom. The schema is described in Agent Manifest under &#39;spec.custom_streaming_update&#39;. | 

## Example

```python
from acp_client_v0_1.models.stream_event_payload import StreamEventPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StreamEventPayload from a JSON string
stream_event_payload_instance = StreamEventPayload.from_json(json)
# print the JSON string representation of the object
print(StreamEventPayload.to_json())

# convert the object into a dict
stream_event_payload_dict = stream_event_payload_instance.to_dict()
# create an instance of StreamEventPayload from a dict
stream_event_payload_from_dict = StreamEventPayload.from_dict(stream_event_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


