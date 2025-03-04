# AgentManifest

Describe all the details of an agent, including how to use, how to deploy and its dependencies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**AgentMetadata**](AgentMetadata.md) |  | 
**specs** | [**AgentSpecs**](AgentSpecs.md) |  | 
**dependencies** | [**List[AgentManifestRef]**](AgentManifestRef.md) | List of all other agents this agent depends on | [optional] 
**deployments** | [**List[AgentManifestDeploymentsInner]**](AgentManifestDeploymentsInner.md) | List of possible methods to instantiate or consume the agent.  Any of the available option could be used. Every option could be associated with a unique name within this agent. If present, when another manifest refers to this manifest, it can also select the preferred deployment option. | [optional] 

## Example

```python
from acp_client_v0_1.models.agent_manifest import AgentManifest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentManifest from a JSON string
agent_manifest_instance = AgentManifest.from_json(json)
# print the JSON string representation of the object
print(AgentManifest.to_json())

# convert the object into a dict
agent_manifest_dict = agent_manifest_instance.to_dict()
# create an instance of AgentManifest from a dict
agent_manifest_from_dict = AgentManifest.from_dict(agent_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


