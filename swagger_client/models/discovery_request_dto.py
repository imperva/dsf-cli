# coding: utf-8

"""
    DSF Data Security Fabric Open APIs

    DSF Data Security Fabric Open APIs Documentation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DiscoveryRequestDto(object):
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
        'discovery_type': 'str',
        'subscription_id': 'str'
    }

    attribute_map = {
        'discovery_type': 'discoveryType',
        'subscription_id': 'subscriptionId'
    }

    def __init__(self, discovery_type=None, subscription_id=None):  # noqa: E501
        """DiscoveryRequestDto - a model defined in Swagger"""  # noqa: E501
        self._discovery_type = None
        self._subscription_id = None
        self.discriminator = None
        self.discovery_type = discovery_type
        if subscription_id is not None:
            self.subscription_id = subscription_id

    @property
    def discovery_type(self):
        """Gets the discovery_type of this DiscoveryRequestDto.  # noqa: E501


        :return: The discovery_type of this DiscoveryRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._discovery_type

    @discovery_type.setter
    def discovery_type(self, discovery_type):
        """Sets the discovery_type of this DiscoveryRequestDto.


        :param discovery_type: The discovery_type of this DiscoveryRequestDto.  # noqa: E501
        :type: str
        """
        if discovery_type is None:
            raise ValueError("Invalid value for `discovery_type`, must not be `None`")  # noqa: E501
        allowed_values = ["AWS_RDS", "AWS_REDSHIFT", "AZURE", "GCP", "ALL"]  # noqa: E501
        if discovery_type not in allowed_values:
            raise ValueError(
                "Invalid value for `discovery_type` ({0}), must be one of {1}"  # noqa: E501
                .format(discovery_type, allowed_values)
            )

        self._discovery_type = discovery_type

    @property
    def subscription_id(self):
        """Gets the subscription_id of this DiscoveryRequestDto.  # noqa: E501


        :return: The subscription_id of this DiscoveryRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this DiscoveryRequestDto.


        :param subscription_id: The subscription_id of this DiscoveryRequestDto.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

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
        if issubclass(DiscoveryRequestDto, dict):
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
        if not isinstance(other, DiscoveryRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
