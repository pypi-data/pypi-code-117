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


class LogMessage(object):
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
        'level': 'str',
        'message': 'str',
        'source': 'str',
        'time': 'str'
    }

    attribute_map = {
        'level': 'level',
        'message': 'message',
        'source': 'source',
        'time': 'time'
    }

    def __init__(self, level=None, message=None, source=None, time=None):
        """
        LogMessage - a model defined in Swagger
        """

        self._level = None
        self._message = None
        self._source = None
        self._time = None

        if level is not None:
          self.level = level
        if message is not None:
          self.message = message
        if source is not None:
          self.source = source
        if time is not None:
          self.time = time

    @property
    def level(self):
        """
        Gets the level of this LogMessage.

        :return: The level of this LogMessage.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this LogMessage.

        :param level: The level of this LogMessage.
        :type: str
        """

        self._level = level

    @property
    def message(self):
        """
        Gets the message of this LogMessage.

        :return: The message of this LogMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this LogMessage.

        :param message: The message of this LogMessage.
        :type: str
        """

        self._message = message

    @property
    def source(self):
        """
        Gets the source of this LogMessage.

        :return: The source of this LogMessage.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this LogMessage.

        :param source: The source of this LogMessage.
        :type: str
        """

        self._source = source

    @property
    def time(self):
        """
        Gets the time of this LogMessage.

        :return: The time of this LogMessage.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this LogMessage.

        :param time: The time of this LogMessage.
        :type: str
        """

        self._time = time

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
        if not isinstance(other, LogMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
