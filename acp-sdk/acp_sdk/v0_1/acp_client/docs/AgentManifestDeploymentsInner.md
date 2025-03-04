# AgentManifestDeploymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** | Name this deployment option is referred to within this agent. This is needed to indicate which one is preferred when this manifest is referred. Can be omitted, in such case selection is not possible. | [optional] 
**url** | **str** | Location of the source code. E.g. path to code root, github repo url etc. | 
**framework_config** | [**SourceCodeDeploymentFrameworkConfig**](SourceCodeDeploymentFrameworkConfig.md) |  | 
**protocol** | [**AgentConnectProtocol**](AgentConnectProtocol.md) |  | 
**image** | **str** | Container image for the agent | 

## Example

```python
from acp_client_v0_1.models.agent_manifest_deployments_inner import AgentManifestDeploymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AgentManifestDeploymentsInner from a JSON string
agent_manifest_deployments_inner_instance = AgentManifestDeploymentsInner.from_json(json)
# print the JSON string representation of the object
print(AgentManifestDeploymentsInner.to_json())

# convert the object into a dict
agent_manifest_deployments_inner_dict = agent_manifest_deployments_inner_instance.to_dict()
# create an instance of AgentManifestDeploymentsInner from a dict
agent_manifest_deployments_inner_from_dict = AgentManifestDeploymentsInner.from_dict(agent_manifest_deployments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


