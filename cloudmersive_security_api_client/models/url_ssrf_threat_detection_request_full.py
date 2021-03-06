# coding: utf-8

"""
    securityapi

    The security APIs help you detect and block security threats.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UrlSsrfThreatDetectionRequestFull(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'blocked_domains': 'list[str]'
    }

    attribute_map = {
        'url': 'URL',
        'blocked_domains': 'BlockedDomains'
    }

    def __init__(self, url=None, blocked_domains=None):  # noqa: E501
        """UrlSsrfThreatDetectionRequestFull - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._blocked_domains = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if blocked_domains is not None:
            self.blocked_domains = blocked_domains

    @property
    def url(self):
        """Gets the url of this UrlSsrfThreatDetectionRequestFull.  # noqa: E501

        URL to validate  # noqa: E501

        :return: The url of this UrlSsrfThreatDetectionRequestFull.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UrlSsrfThreatDetectionRequestFull.

        URL to validate  # noqa: E501

        :param url: The url of this UrlSsrfThreatDetectionRequestFull.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def blocked_domains(self):
        """Gets the blocked_domains of this UrlSsrfThreatDetectionRequestFull.  # noqa: E501

        Top level domains that you do not want to allow access to, e.g. mydomain.com - will block all subdomains as well  # noqa: E501

        :return: The blocked_domains of this UrlSsrfThreatDetectionRequestFull.  # noqa: E501
        :rtype: list[str]
        """
        return self._blocked_domains

    @blocked_domains.setter
    def blocked_domains(self, blocked_domains):
        """Sets the blocked_domains of this UrlSsrfThreatDetectionRequestFull.

        Top level domains that you do not want to allow access to, e.g. mydomain.com - will block all subdomains as well  # noqa: E501

        :param blocked_domains: The blocked_domains of this UrlSsrfThreatDetectionRequestFull.  # noqa: E501
        :type: list[str]
        """

        self._blocked_domains = blocked_domains

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UrlSsrfThreatDetectionRequestFull, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UrlSsrfThreatDetectionRequestFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
