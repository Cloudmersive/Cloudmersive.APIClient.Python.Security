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


class StringXxeDetectionResult(object):
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
        'successful': 'bool',
        'contained_xxe': 'bool'
    }

    attribute_map = {
        'successful': 'Successful',
        'contained_xxe': 'ContainedXxe'
    }

    def __init__(self, successful=None, contained_xxe=None):  # noqa: E501
        """StringXxeDetectionResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._contained_xxe = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if contained_xxe is not None:
            self.contained_xxe = contained_xxe

    @property
    def successful(self):
        """Gets the successful of this StringXxeDetectionResult.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this StringXxeDetectionResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this StringXxeDetectionResult.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this StringXxeDetectionResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def contained_xxe(self):
        """Gets the contained_xxe of this StringXxeDetectionResult.  # noqa: E501

        True if the input contained XXE threats, false otherwise  # noqa: E501

        :return: The contained_xxe of this StringXxeDetectionResult.  # noqa: E501
        :rtype: bool
        """
        return self._contained_xxe

    @contained_xxe.setter
    def contained_xxe(self, contained_xxe):
        """Sets the contained_xxe of this StringXxeDetectionResult.

        True if the input contained XXE threats, false otherwise  # noqa: E501

        :param contained_xxe: The contained_xxe of this StringXxeDetectionResult.  # noqa: E501
        :type: bool
        """

        self._contained_xxe = contained_xxe

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
        if issubclass(StringXxeDetectionResult, dict):
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
        if not isinstance(other, StringXxeDetectionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
