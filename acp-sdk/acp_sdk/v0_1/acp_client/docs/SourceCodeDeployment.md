# SourceCodeDeployment

Describes the source code where the agent is available. It specifies also the type of deployer that it supports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** | Name this deployment option is referred to within this agent. This is needed to indicate which one is preferred when this manifest is referred. Can be omitted, in such case selection is not possible. | [optional] 
**url** | **str** | Location of the source code. E.g. path to code root, github repo url etc. | 
**framework_config** | [**SourceCodeDeploymentFrameworkConfig**](SourceCodeDeploymentFrameworkConfig.md) |  | 

## Example

```python
from acp_client_v0_1.models.source_code_deployment import SourceCodeDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCodeDeployment from a JSON string
source_code_deployment_instance = SourceCodeDeployment.from_json(json)
# print the JSON string representation of the object
print(SourceCodeDeployment.to_json())

# convert the object into a dict
source_code_deployment_dict = source_code_deployment_instance.to_dict()
# create an instance of SourceCodeDeployment from a dict
source_code_deployment_from_dict = SourceCodeDeployment.from_dict(source_code_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


