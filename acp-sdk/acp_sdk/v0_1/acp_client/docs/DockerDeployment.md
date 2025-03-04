# DockerDeployment

Describes the docker deployment for this agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**image** | **str** | Container image for the agent | 
**protocol** | [**AgentConnectProtocol**](AgentConnectProtocol.md) |  | 

## Example

```python
from acp_client_v0_1.models.docker_deployment import DockerDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of DockerDeployment from a JSON string
docker_deployment_instance = DockerDeployment.from_json(json)
# print the JSON string representation of the object
print(DockerDeployment.to_json())

# convert the object into a dict
docker_deployment_dict = docker_deployment_instance.to_dict()
# create an instance of DockerDeployment from a dict
docker_deployment_from_dict = DockerDeployment.from_dict(docker_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


