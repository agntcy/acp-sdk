# RunOutput

Output of a Run. Can be the final result or an interrupt.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**run_id** | **str** | The ID of the run. | 
**status** | [**RunStatus**](RunStatus.md) | Status of the Run when this result was generated. This is particurarly useful when this data structure is used for streaming results. As the server can indicate an interrupt or an error condition while streaming the result. | 
**result** | **object** | The output of the agent. The schema is described in Agent Manifest under &#39;spec.output&#39;. | 
**interrupt** | **object** | This schema describes the interrupt payload. Actual schema describes a polimorphic object, which means a schema structured with &#x60;oneOf&#x60; and &#x60;discriminator&#x60;. The discriminator is the &#x60;interrupt_type&#x60;, while the schemas will be the ones defined in the agent spec under &#x60;interrupts&#x60;/&#x60;interrupt_payload&#x60; For example:          oneOf:   - $ref: &#39;#/components/schemas/ApprovalInterruptPayload&#39;   - $ref: &#39;#/components/schemas/QuestionInterruptPayload&#39; discriminator:   propertyName: interruput_type   mapping:     approval: &#39;#/components/schemas/ApprovalInterruptPayload&#39;     question: &#39;#/components/schemas/QuestionInterruptPayload&#39; | 
**errcode** | **int** | code of the error | 
**description** | **str** | description of the error | 

## Example

```python
from acp_client_v0_1.models.run_output import RunOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RunOutput from a JSON string
run_output_instance = RunOutput.from_json(json)
# print the JSON string representation of the object
print(RunOutput.to_json())

# convert the object into a dict
run_output_dict = run_output_instance.to_dict()
# create an instance of RunOutput from a dict
run_output_from_dict = RunOutput.from_dict(run_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


