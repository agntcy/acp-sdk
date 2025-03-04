# coding: utf-8

"""
    Agent Connect Protocol

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from acp_client_v0_1.models.stream_event_payload import StreamEventPayload

class TestStreamEventPayload(unittest.TestCase):
    """StreamEventPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StreamEventPayload:
        """Test StreamEventPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamEventPayload`
        """
        model = StreamEventPayload()
        if include_optional:
            return StreamEventPayload(
                type = 'result',
                run_id = '',
                status = 'pending',
                result = acp_client_v0_1.models.output_schema.Output Schema(),
                update = acp_client_v0_1.models.stream_update_schema.Stream Update Schema()
            )
        else:
            return StreamEventPayload(
                type = 'result',
                run_id = '',
                status = 'pending',
                result = acp_client_v0_1.models.output_schema.Output Schema(),
                update = acp_client_v0_1.models.stream_update_schema.Stream Update Schema(),
        )
        """

    def testStreamEventPayload(self):
        """Test StreamEventPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
