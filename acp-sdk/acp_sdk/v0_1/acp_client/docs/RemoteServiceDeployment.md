# RemoteServiceDeployment

Describes the network endpoint where the agent is available

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**protocol** | [**AgentConnectProtocol**](AgentConnectProtocol.md) |  | 

## Example

```python
from acp_client_v0_1.models.remote_service_deployment import RemoteServiceDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteServiceDeployment from a JSON string
remote_service_deployment_instance = RemoteServiceDeployment.from_json(json)
# print the JSON string representation of the object
print(RemoteServiceDeployment.to_json())

# convert the object into a dict
remote_service_deployment_dict = remote_service_deployment_instance.to_dict()
# create an instance of RemoteServiceDeployment from a dict
remote_service_deployment_from_dict = RemoteServiceDeployment.from_dict(remote_service_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


