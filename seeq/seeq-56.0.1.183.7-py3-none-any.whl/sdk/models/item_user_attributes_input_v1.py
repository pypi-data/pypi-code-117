# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 56.0.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ItemUserAttributesInputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'opened_at': 'str',
        'opened_at_instant': 'int'
    }

    attribute_map = {
        'opened_at': 'openedAt',
        'opened_at_instant': 'openedAtInstant'
    }

    def __init__(self, opened_at=None, opened_at_instant=None):
        """
        ItemUserAttributesInputV1 - a model defined in Swagger
        """

        self._opened_at = None
        self._opened_at_instant = None

        if opened_at is not None:
          self.opened_at = opened_at
        if opened_at_instant is not None:
          self.opened_at_instant = opened_at_instant

    @property
    def opened_at(self):
        """
        Gets the opened_at of this ItemUserAttributesInputV1.
        The opened date of the item. Must be an ISO-8601 timestamp. If the value is 'null' the date will be cleared

        :return: The opened_at of this ItemUserAttributesInputV1.
        :rtype: str
        """
        return self._opened_at

    @opened_at.setter
    def opened_at(self, opened_at):
        """
        Sets the opened_at of this ItemUserAttributesInputV1.
        The opened date of the item. Must be an ISO-8601 timestamp. If the value is 'null' the date will be cleared

        :param opened_at: The opened_at of this ItemUserAttributesInputV1.
        :type: str
        """

        self._opened_at = opened_at

    @property
    def opened_at_instant(self):
        """
        Gets the opened_at_instant of this ItemUserAttributesInputV1.

        :return: The opened_at_instant of this ItemUserAttributesInputV1.
        :rtype: int
        """
        return self._opened_at_instant

    @opened_at_instant.setter
    def opened_at_instant(self, opened_at_instant):
        """
        Sets the opened_at_instant of this ItemUserAttributesInputV1.

        :param opened_at_instant: The opened_at_instant of this ItemUserAttributesInputV1.
        :type: int
        """

        self._opened_at_instant = opened_at_instant

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ItemUserAttributesInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
