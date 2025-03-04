# RunInterrupt

Interrupt occurred during a Run

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**interrupt** | **object** | This schema describes the interrupt payload. Actual schema describes a polimorphic object, which means a schema structured with &#x60;oneOf&#x60; and &#x60;discriminator&#x60;. The discriminator is the &#x60;interrupt_type&#x60;, while the schemas will be the ones defined in the agent spec under &#x60;interrupts&#x60;/&#x60;interrupt_payload&#x60; For example:          oneOf:   - $ref: &#39;#/components/schemas/ApprovalInterruptPayload&#39;   - $ref: &#39;#/components/schemas/QuestionInterruptPayload&#39; discriminator:   propertyName: interruput_type   mapping:     approval: &#39;#/components/schemas/ApprovalInterruptPayload&#39;     question: &#39;#/components/schemas/QuestionInterruptPayload&#39; | 

## Example

```python
from acp_client_v0_1.models.run_interrupt import RunInterrupt

# TODO update the JSON string below
json = "{}"
# create an instance of RunInterrupt from a JSON string
run_interrupt_instance = RunInterrupt.from_json(json)
# print the JSON string representation of the object
print(RunInterrupt.to_json())

# convert the object into a dict
run_interrupt_dict = run_interrupt_instance.to_dict()
# create an instance of RunInterrupt from a dict
run_interrupt_from_dict = RunInterrupt.from_dict(run_interrupt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


