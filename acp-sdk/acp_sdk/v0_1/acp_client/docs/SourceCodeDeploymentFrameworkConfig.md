# SourceCodeDeploymentFrameworkConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**framework_type** | **str** |  | 
**graph** | **str** |  | 
**path** | **str** |  | 

## Example

```python
from acp_client_v0_1.models.source_code_deployment_framework_config import SourceCodeDeploymentFrameworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCodeDeploymentFrameworkConfig from a JSON string
source_code_deployment_framework_config_instance = SourceCodeDeploymentFrameworkConfig.from_json(json)
# print the JSON string representation of the object
print(SourceCodeDeploymentFrameworkConfig.to_json())

# convert the object into a dict
source_code_deployment_framework_config_dict = source_code_deployment_framework_config_instance.to_dict()
# create an instance of SourceCodeDeploymentFrameworkConfig from a dict
source_code_deployment_framework_config_from_dict = SourceCodeDeploymentFrameworkConfig.from_dict(source_code_deployment_framework_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


