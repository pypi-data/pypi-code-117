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


class DatasourceCleanUpOutputV1(object):
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
        'num_newly_archived_items': 'int'
    }

    attribute_map = {
        'num_newly_archived_items': 'numNewlyArchivedItems'
    }

    def __init__(self, num_newly_archived_items=None):
        """
        DatasourceCleanUpOutputV1 - a model defined in Swagger
        """

        self._num_newly_archived_items = None

        if num_newly_archived_items is not None:
          self.num_newly_archived_items = num_newly_archived_items

    @property
    def num_newly_archived_items(self):
        """
        Gets the num_newly_archived_items of this DatasourceCleanUpOutputV1.
        The number of items that were archived for being stale.

        :return: The num_newly_archived_items of this DatasourceCleanUpOutputV1.
        :rtype: int
        """
        return self._num_newly_archived_items

    @num_newly_archived_items.setter
    def num_newly_archived_items(self, num_newly_archived_items):
        """
        Sets the num_newly_archived_items of this DatasourceCleanUpOutputV1.
        The number of items that were archived for being stale.

        :param num_newly_archived_items: The num_newly_archived_items of this DatasourceCleanUpOutputV1.
        :type: int
        """

        self._num_newly_archived_items = num_newly_archived_items

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
        if not isinstance(other, DatasourceCleanUpOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
