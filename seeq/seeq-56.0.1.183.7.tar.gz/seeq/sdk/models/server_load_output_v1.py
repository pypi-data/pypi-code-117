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


class ServerLoadOutputV1(object):
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
        'description': 'str',
        'load_percentage': 'float'
    }

    attribute_map = {
        'description': 'description',
        'load_percentage': 'loadPercentage'
    }

    def __init__(self, description=None, load_percentage=None):
        """
        ServerLoadOutputV1 - a model defined in Swagger
        """

        self._description = None
        self._load_percentage = None

        if description is not None:
          self.description = description
        if load_percentage is not None:
          self.load_percentage = load_percentage

    @property
    def description(self):
        """
        Gets the description of this ServerLoadOutputV1.
        A human readable description of what is most causing the server load.

        :return: The description of this ServerLoadOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ServerLoadOutputV1.
        A human readable description of what is most causing the server load.

        :param description: The description of this ServerLoadOutputV1.
        :type: str
        """

        self._description = description

    @property
    def load_percentage(self):
        """
        Gets the load_percentage of this ServerLoadOutputV1.
        A rough percentage of load that the server is experiencing, where 0.0 is entirely unloaded and 1.0 is entirely busy. Note, a load of greater than 1.0 is possible and perhaps normal, but it indicates the server is queuing effort and some users may have a degraded experience.

        :return: The load_percentage of this ServerLoadOutputV1.
        :rtype: float
        """
        return self._load_percentage

    @load_percentage.setter
    def load_percentage(self, load_percentage):
        """
        Sets the load_percentage of this ServerLoadOutputV1.
        A rough percentage of load that the server is experiencing, where 0.0 is entirely unloaded and 1.0 is entirely busy. Note, a load of greater than 1.0 is possible and perhaps normal, but it indicates the server is queuing effort and some users may have a degraded experience.

        :param load_percentage: The load_percentage of this ServerLoadOutputV1.
        :type: float
        """

        self._load_percentage = load_percentage

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
        if not isinstance(other, ServerLoadOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
