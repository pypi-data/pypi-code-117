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


class SwapOptionListV1(object):
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
        'swap_options': 'list[SwapOptionV1]'
    }

    attribute_map = {
        'swap_options': 'swapOptions'
    }

    def __init__(self, swap_options=None):
        """
        SwapOptionListV1 - a model defined in Swagger
        """

        self._swap_options = None

        if swap_options is not None:
          self.swap_options = swap_options

    @property
    def swap_options(self):
        """
        Gets the swap_options of this SwapOptionListV1.
        A list of Items that can be chosen as the swap root, ranked by the number of matchesfound between the Items to be swapped and the Items in the tree rooted at the Item to be swapped in.

        :return: The swap_options of this SwapOptionListV1.
        :rtype: list[SwapOptionV1]
        """
        return self._swap_options

    @swap_options.setter
    def swap_options(self, swap_options):
        """
        Sets the swap_options of this SwapOptionListV1.
        A list of Items that can be chosen as the swap root, ranked by the number of matchesfound between the Items to be swapped and the Items in the tree rooted at the Item to be swapped in.

        :param swap_options: The swap_options of this SwapOptionListV1.
        :type: list[SwapOptionV1]
        """

        self._swap_options = swap_options

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
        if not isinstance(other, SwapOptionListV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
