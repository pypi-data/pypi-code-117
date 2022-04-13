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


class MonitorDefinitionsOutputV1(object):
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
        'monitor_definitions': 'list[MonitorDefinitionOutputV1]'
    }

    attribute_map = {
        'monitor_definitions': 'monitorDefinitions'
    }

    def __init__(self, monitor_definitions=None):
        """
        MonitorDefinitionsOutputV1 - a model defined in Swagger
        """

        self._monitor_definitions = None

        if monitor_definitions is not None:
          self.monitor_definitions = monitor_definitions

    @property
    def monitor_definitions(self):
        """
        Gets the monitor_definitions of this MonitorDefinitionsOutputV1.

        :return: The monitor_definitions of this MonitorDefinitionsOutputV1.
        :rtype: list[MonitorDefinitionOutputV1]
        """
        return self._monitor_definitions

    @monitor_definitions.setter
    def monitor_definitions(self, monitor_definitions):
        """
        Sets the monitor_definitions of this MonitorDefinitionsOutputV1.

        :param monitor_definitions: The monitor_definitions of this MonitorDefinitionsOutputV1.
        :type: list[MonitorDefinitionOutputV1]
        """

        self._monitor_definitions = monitor_definitions

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
        if not isinstance(other, MonitorDefinitionsOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
