# LangGraphConfig

Describes langgraph based agent deployment config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**framework_type** | **str** |  | 
**graph** | **str** |  | 

## Example

```python
from acp_client_v0_1.models.lang_graph_config import LangGraphConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LangGraphConfig from a JSON string
lang_graph_config_instance = LangGraphConfig.from_json(json)
# print the JSON string representation of the object
print(LangGraphConfig.to_json())

# convert the object into a dict
lang_graph_config_dict = lang_graph_config_instance.to_dict()
# create an instance of LangGraphConfig from a dict
lang_graph_config_from_dict = LangGraphConfig.from_dict(lang_graph_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


