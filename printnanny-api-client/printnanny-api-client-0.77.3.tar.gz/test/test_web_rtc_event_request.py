# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.web_rtc_event_request import WebRTCEventRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestWebRTCEventRequest(unittest.TestCase):
    """WebRTCEventRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WebRTCEventRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.web_rtc_event_request.WebRTCEventRequest()  # noqa: E501
        if include_optional :
            return WebRTCEventRequest(
                model = 'WebRTCEvent', 
                source = 'octoprint', 
                send_ws = True, 
                event_name = 'stream_start_success', 
                data = {
                    'key' : null
                    }, 
                device = 56, 
                stream = 56
            )
        else :
            return WebRTCEventRequest(
                model = 'WebRTCEvent',
                source = 'octoprint',
                event_name = 'stream_start_success',
                device = 56,
                stream = 56,
        )

    def testWebRTCEventRequest(self):
        """Test WebRTCEventRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
