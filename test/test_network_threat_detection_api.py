# coding: utf-8

"""
    securityapi

    The security APIs help you detect and block security threats.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_security_api_client
from cloudmersive_security_api_client.api.network_threat_detection_api import NetworkThreatDetectionApi  # noqa: E501
from cloudmersive_security_api_client.rest import ApiException


class TestNetworkThreatDetectionApi(unittest.TestCase):
    """NetworkThreatDetectionApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_security_api_client.api.network_threat_detection_api.NetworkThreatDetectionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_network_threat_detection_detect_ssrf_url(self):
        """Test case for network_threat_detection_detect_ssrf_url

        Check a URL for Server-side Request Forgery (SSRF) threats  # noqa: E501
        """
        pass

    def test_network_threat_detection_is_bot(self):
        """Test case for network_threat_detection_is_bot

        Check if IP address is a Bot client threat  # noqa: E501
        """
        pass

    def test_network_threat_detection_is_threat(self):
        """Test case for network_threat_detection_is_threat

        Check if IP address is a known threat  # noqa: E501
        """
        pass

    def test_network_threat_detection_is_tor_node(self):
        """Test case for network_threat_detection_is_tor_node

        Check if IP address is a Tor node server  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
