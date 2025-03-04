# coding: utf-8

"""
    Agent Connect Protocol

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from acp_client_v0_1.models.llama_index_config import LlamaIndexConfig

class TestLlamaIndexConfig(unittest.TestCase):
    """LlamaIndexConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LlamaIndexConfig:
        """Test LlamaIndexConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LlamaIndexConfig`
        """
        model = LlamaIndexConfig()
        if include_optional:
            return LlamaIndexConfig(
                framework_type = 'llamaindex',
                path = ''
            )
        else:
            return LlamaIndexConfig(
                framework_type = 'llamaindex',
                path = '',
        )
        """

    def testLlamaIndexConfig(self):
        """Test LlamaIndexConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
