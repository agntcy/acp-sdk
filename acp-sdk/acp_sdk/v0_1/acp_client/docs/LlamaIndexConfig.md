# LlamaIndexConfig

Describes llamaindex based agent deployment config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**framework_type** | **str** |  | 
**path** | **str** |  | 

## Example

```python
from acp_client_v0_1.models.llama_index_config import LlamaIndexConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LlamaIndexConfig from a JSON string
llama_index_config_instance = LlamaIndexConfig.from_json(json)
# print the JSON string representation of the object
print(LlamaIndexConfig.to_json())

# convert the object into a dict
llama_index_config_dict = llama_index_config_instance.to_dict()
# create an instance of LlamaIndexConfig from a dict
llama_index_config_from_dict = LlamaIndexConfig.from_dict(llama_index_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


