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


class GetAddOnToolsOutputV1(object):
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
        'add_on_tools': 'list[AddOnToolOutputV1]'
    }

    attribute_map = {
        'add_on_tools': 'addOnTools'
    }

    def __init__(self, add_on_tools=None):
        """
        GetAddOnToolsOutputV1 - a model defined in Swagger
        """

        self._add_on_tools = None

        if add_on_tools is not None:
          self.add_on_tools = add_on_tools

    @property
    def add_on_tools(self):
        """
        Gets the add_on_tools of this GetAddOnToolsOutputV1.
        The list of add-on tools

        :return: The add_on_tools of this GetAddOnToolsOutputV1.
        :rtype: list[AddOnToolOutputV1]
        """
        return self._add_on_tools

    @add_on_tools.setter
    def add_on_tools(self, add_on_tools):
        """
        Sets the add_on_tools of this GetAddOnToolsOutputV1.
        The list of add-on tools

        :param add_on_tools: The add_on_tools of this GetAddOnToolsOutputV1.
        :type: list[AddOnToolOutputV1]
        """

        self._add_on_tools = add_on_tools

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
        if not isinstance(other, GetAddOnToolsOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
