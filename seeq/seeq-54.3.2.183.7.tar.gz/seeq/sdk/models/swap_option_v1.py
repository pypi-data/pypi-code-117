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


class SwapOptionV1(object):
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
        'invalid_swap_outs': 'list[InvalidSwapOutV1]',
        'items_with_swap_pairs': 'list[ItemWithSwapPairsV1]',
        'swap_root_candidate': 'ItemPreviewWithAssetsV1'
    }

    attribute_map = {
        'invalid_swap_outs': 'invalidSwapOuts',
        'items_with_swap_pairs': 'itemsWithSwapPairs',
        'swap_root_candidate': 'swapRootCandidate'
    }

    def __init__(self, invalid_swap_outs=None, items_with_swap_pairs=None, swap_root_candidate=None):
        """
        SwapOptionV1 - a model defined in Swagger
        """

        self._invalid_swap_outs = None
        self._items_with_swap_pairs = None
        self._swap_root_candidate = None

        if invalid_swap_outs is not None:
          self.invalid_swap_outs = invalid_swap_outs
        if items_with_swap_pairs is not None:
          self.items_with_swap_pairs = items_with_swap_pairs
        if swap_root_candidate is not None:
          self.swap_root_candidate = swap_root_candidate

    @property
    def invalid_swap_outs(self):
        """
        Gets the invalid_swap_outs of this SwapOptionV1.
        The list of items from the query parameters that are invalid for swapping out with root item

        :return: The invalid_swap_outs of this SwapOptionV1.
        :rtype: list[InvalidSwapOutV1]
        """
        return self._invalid_swap_outs

    @invalid_swap_outs.setter
    def invalid_swap_outs(self, invalid_swap_outs):
        """
        Sets the invalid_swap_outs of this SwapOptionV1.
        The list of items from the query parameters that are invalid for swapping out with root item

        :param invalid_swap_outs: The invalid_swap_outs of this SwapOptionV1.
        :type: list[InvalidSwapOutV1]
        """

        self._invalid_swap_outs = invalid_swap_outs

    @property
    def items_with_swap_pairs(self):
        """
        Gets the items_with_swap_pairs of this SwapOptionV1.
        The list of items from the query parameters that can be swapped, augmented with the swap pairs needed to perform the swap

        :return: The items_with_swap_pairs of this SwapOptionV1.
        :rtype: list[ItemWithSwapPairsV1]
        """
        return self._items_with_swap_pairs

    @items_with_swap_pairs.setter
    def items_with_swap_pairs(self, items_with_swap_pairs):
        """
        Sets the items_with_swap_pairs of this SwapOptionV1.
        The list of items from the query parameters that can be swapped, augmented with the swap pairs needed to perform the swap

        :param items_with_swap_pairs: The items_with_swap_pairs of this SwapOptionV1.
        :type: list[ItemWithSwapPairsV1]
        """

        self._items_with_swap_pairs = items_with_swap_pairs

    @property
    def swap_root_candidate(self):
        """
        Gets the swap_root_candidate of this SwapOptionV1.
        The candidate Item to be swapped out for the swap-in Item

        :return: The swap_root_candidate of this SwapOptionV1.
        :rtype: ItemPreviewWithAssetsV1
        """
        return self._swap_root_candidate

    @swap_root_candidate.setter
    def swap_root_candidate(self, swap_root_candidate):
        """
        Sets the swap_root_candidate of this SwapOptionV1.
        The candidate Item to be swapped out for the swap-in Item

        :param swap_root_candidate: The swap_root_candidate of this SwapOptionV1.
        :type: ItemPreviewWithAssetsV1
        """

        self._swap_root_candidate = swap_root_candidate

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
        if not isinstance(other, SwapOptionV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
