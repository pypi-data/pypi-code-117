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


class CapsulesInputV1(object):
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
        'capsules': 'list[CapsuleInputV1]',
        'key_unit_of_measure': 'str'
    }

    attribute_map = {
        'capsules': 'capsules',
        'key_unit_of_measure': 'keyUnitOfMeasure'
    }

    def __init__(self, capsules=None, key_unit_of_measure=None):
        """
        CapsulesInputV1 - a model defined in Swagger
        """

        self._capsules = None
        self._key_unit_of_measure = None

        if capsules is not None:
          self.capsules = capsules
        if key_unit_of_measure is not None:
          self.key_unit_of_measure = key_unit_of_measure

    @property
    def capsules(self):
        """
        Gets the capsules of this CapsulesInputV1.
        The list of capsules

        :return: The capsules of this CapsulesInputV1.
        :rtype: list[CapsuleInputV1]
        """
        return self._capsules

    @capsules.setter
    def capsules(self, capsules):
        """
        Sets the capsules of this CapsulesInputV1.
        The list of capsules

        :param capsules: The capsules of this CapsulesInputV1.
        :type: list[CapsuleInputV1]
        """
        if capsules is None:
            raise ValueError("Invalid value for `capsules`, must not be `None`")

        self._capsules = capsules

    @property
    def key_unit_of_measure(self):
        """
        Gets the key_unit_of_measure of this CapsulesInputV1.
        The unit of measure for the capsule starts and ends. If left empty, input is assumed to be in ISO8601 format.

        :return: The key_unit_of_measure of this CapsulesInputV1.
        :rtype: str
        """
        return self._key_unit_of_measure

    @key_unit_of_measure.setter
    def key_unit_of_measure(self, key_unit_of_measure):
        """
        Sets the key_unit_of_measure of this CapsulesInputV1.
        The unit of measure for the capsule starts and ends. If left empty, input is assumed to be in ISO8601 format.

        :param key_unit_of_measure: The key_unit_of_measure of this CapsulesInputV1.
        :type: str
        """

        self._key_unit_of_measure = key_unit_of_measure

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
        if not isinstance(other, CapsulesInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
