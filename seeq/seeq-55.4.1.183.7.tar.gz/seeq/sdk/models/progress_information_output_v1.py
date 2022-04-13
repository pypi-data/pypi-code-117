# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 55.4.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProgressInformationOutputV1(object):
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
        'completed_count': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'completed_count': 'completedCount',
        'total_count': 'totalCount'
    }

    def __init__(self, completed_count=None, total_count=None):
        """
        ProgressInformationOutputV1 - a model defined in Swagger
        """

        self._completed_count = None
        self._total_count = None

        if completed_count is not None:
          self.completed_count = completed_count
        if total_count is not None:
          self.total_count = total_count

    @property
    def completed_count(self):
        """
        Gets the completed_count of this ProgressInformationOutputV1.

        :return: The completed_count of this ProgressInformationOutputV1.
        :rtype: int
        """
        return self._completed_count

    @completed_count.setter
    def completed_count(self, completed_count):
        """
        Sets the completed_count of this ProgressInformationOutputV1.

        :param completed_count: The completed_count of this ProgressInformationOutputV1.
        :type: int
        """

        self._completed_count = completed_count

    @property
    def total_count(self):
        """
        Gets the total_count of this ProgressInformationOutputV1.

        :return: The total_count of this ProgressInformationOutputV1.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this ProgressInformationOutputV1.

        :param total_count: The total_count of this ProgressInformationOutputV1.
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, ProgressInformationOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
