# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 54.3.2-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PermissionsV1(object):
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
        'manage': 'bool',
        'read': 'bool',
        'write': 'bool'
    }

    attribute_map = {
        'manage': 'manage',
        'read': 'read',
        'write': 'write'
    }

    def __init__(self, manage=False, read=False, write=False):
        """
        PermissionsV1 - a model defined in Swagger
        """

        self._manage = None
        self._read = None
        self._write = None

        if manage is not None:
          self.manage = manage
        if read is not None:
          self.read = read
        if write is not None:
          self.write = write

    @property
    def manage(self):
        """
        Gets the manage of this PermissionsV1.

        :return: The manage of this PermissionsV1.
        :rtype: bool
        """
        return self._manage

    @manage.setter
    def manage(self, manage):
        """
        Sets the manage of this PermissionsV1.

        :param manage: The manage of this PermissionsV1.
        :type: bool
        """

        self._manage = manage

    @property
    def read(self):
        """
        Gets the read of this PermissionsV1.

        :return: The read of this PermissionsV1.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this PermissionsV1.

        :param read: The read of this PermissionsV1.
        :type: bool
        """

        self._read = read

    @property
    def write(self):
        """
        Gets the write of this PermissionsV1.

        :return: The write of this PermissionsV1.
        :rtype: bool
        """
        return self._write

    @write.setter
    def write(self, write):
        """
        Sets the write of this PermissionsV1.

        :param write: The write of this PermissionsV1.
        :type: bool
        """

        self._write = write

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
        if not isinstance(other, PermissionsV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
