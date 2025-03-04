# AgentManifestRef

Reference to an Agent Manifest, it includes name, version and a locator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the agent that identifies the agent in its manifest | 
**version** | **str** | Version of the agent in its manifest. Should be formatted according to semantic versioning (https://semver.org) | 
**url** | **str** | URL of the manifest. Can be a network location or a file. | [optional] 

## Example

```python
from acp_client_v0_1.models.agent_manifest_ref import AgentManifestRef

# TODO update the JSON string below
json = "{}"
# create an instance of AgentManifestRef from a JSON string
agent_manifest_ref_instance = AgentManifestRef.from_json(json)
# print the JSON string representation of the object
print(AgentManifestRef.to_json())

# convert the object into a dict
agent_manifest_ref_dict = agent_manifest_ref_instance.to_dict()
# create an instance of AgentManifestRef from a dict
agent_manifest_ref_from_dict = AgentManifestRef.from_dict(agent_manifest_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


