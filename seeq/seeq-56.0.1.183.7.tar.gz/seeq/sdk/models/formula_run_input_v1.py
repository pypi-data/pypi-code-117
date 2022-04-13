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


class FormulaRunInputV1(object):
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
        'end': 'str',
        'formula': 'str',
        'fragments': 'list[str]',
        'function': 'str',
        'limit': 'int',
        'offset': 'int',
        'parameters': 'list[str]',
        'reduce_formula': 'str',
        'root': 'str',
        'start': 'str'
    }

    attribute_map = {
        'end': 'end',
        'formula': 'formula',
        'fragments': 'fragments',
        'function': 'function',
        'limit': 'limit',
        'offset': 'offset',
        'parameters': 'parameters',
        'reduce_formula': 'reduceFormula',
        'root': 'root',
        'start': 'start'
    }

    def __init__(self, end=None, formula=None, fragments=None, function=None, limit=None, offset=None, parameters=None, reduce_formula=None, root=None, start=None):
        """
        FormulaRunInputV1 - a model defined in Swagger
        """

        self._end = None
        self._formula = None
        self._fragments = None
        self._function = None
        self._limit = None
        self._offset = None
        self._parameters = None
        self._reduce_formula = None
        self._root = None
        self._start = None

        if end is not None:
          self.end = end
        if formula is not None:
          self.formula = formula
        if fragments is not None:
          self.fragments = fragments
        if function is not None:
          self.function = function
        if limit is not None:
          self.limit = limit
        if offset is not None:
          self.offset = offset
        if parameters is not None:
          self.parameters = parameters
        if reduce_formula is not None:
          self.reduce_formula = reduce_formula
        if root is not None:
          self.root = root
        if start is not None:
          self.start = start

    @property
    def end(self):
        """
        Gets the end of this FormulaRunInputV1.
        A string representing the ending index of the data to be returned.             The contents and whether or not it is required depends on the series type. For time series: a ISO 8601             timestamp (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm). For numeric (non-time) keys: a double-precision             number, optionally including units. For example: \"2.5ft\" or \"10 °C\"

        :return: The end of this FormulaRunInputV1.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this FormulaRunInputV1.
        A string representing the ending index of the data to be returned.             The contents and whether or not it is required depends on the series type. For time series: a ISO 8601             timestamp (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm). For numeric (non-time) keys: a double-precision             number, optionally including units. For example: \"2.5ft\" or \"10 °C\"

        :param end: The end of this FormulaRunInputV1.
        :type: str
        """

        self._end = end

    @property
    def formula(self):
        """
        Gets the formula of this FormulaRunInputV1.
        The formula to be applied

        :return: The formula of this FormulaRunInputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this FormulaRunInputV1.
        The formula to be applied

        :param formula: The formula of this FormulaRunInputV1.
        :type: str
        """
        if formula is None:
            raise ValueError("Invalid value for `formula`, must not be `None`")

        self._formula = formula

    @property
    def fragments(self):
        """
        Gets the fragments of this FormulaRunInputV1.
        The formula fragments for unbound parameters of the function. Each parameter should have a             format of 'name=formula' where 'name' is the variable identifier,             without the leading $ sign, and 'formula' is a self-contained formula fragment

        :return: The fragments of this FormulaRunInputV1.
        :rtype: list[str]
        """
        return self._fragments

    @fragments.setter
    def fragments(self, fragments):
        """
        Sets the fragments of this FormulaRunInputV1.
        The formula fragments for unbound parameters of the function. Each parameter should have a             format of 'name=formula' where 'name' is the variable identifier,             without the leading $ sign, and 'formula' is a self-contained formula fragment

        :param fragments: The fragments of this FormulaRunInputV1.
        :type: list[str]
        """

        self._fragments = fragments

    @property
    def function(self):
        """
        Gets the function of this FormulaRunInputV1.
        The ID of a function item for calling formulas with unbound values

        :return: The function of this FormulaRunInputV1.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """
        Sets the function of this FormulaRunInputV1.
        The ID of a function item for calling formulas with unbound values

        :param function: The function of this FormulaRunInputV1.
        :type: str
        """

        self._function = function

    @property
    def limit(self):
        """
        Gets the limit of this FormulaRunInputV1.
        The pagination limit, the total number of collection items that will be returned              in this page of results. Defaults to 1000

        :return: The limit of this FormulaRunInputV1.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this FormulaRunInputV1.
        The pagination limit, the total number of collection items that will be returned              in this page of results. Defaults to 1000

        :param limit: The limit of this FormulaRunInputV1.
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """
        Gets the offset of this FormulaRunInputV1.
        The pagination offset, the index of the first collection item that             will be returned in this page of results. Defaults to 0

        :return: The offset of this FormulaRunInputV1.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this FormulaRunInputV1.
        The pagination offset, the index of the first collection item that             will be returned in this page of results. Defaults to 0

        :param offset: The offset of this FormulaRunInputV1.
        :type: int
        """

        self._offset = offset

    @property
    def parameters(self):
        """
        Gets the parameters of this FormulaRunInputV1.
        Parameters for the formula. Each parameter should have a format of \"name=value\" where                     \"name\" is the variable identifier, without the leading $ sign, and \"value\" is the ID of an                     item or one of the following parameter expressions that can be used to access the properties of                      other items that are parameters: $signal.property('name') to access any property on an item,                     $signal.parentProperty('name') can be used if an item is in a tree to to access any property                     on the parent, and $signal.ancestors(', ') to return a list of all the ancestors, separated by                     the specified separator. In all of the above examples \"signal\" would need to be another                     parameter that references an item using an ID.

        :return: The parameters of this FormulaRunInputV1.
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this FormulaRunInputV1.
        Parameters for the formula. Each parameter should have a format of \"name=value\" where                     \"name\" is the variable identifier, without the leading $ sign, and \"value\" is the ID of an                     item or one of the following parameter expressions that can be used to access the properties of                      other items that are parameters: $signal.property('name') to access any property on an item,                     $signal.parentProperty('name') can be used if an item is in a tree to to access any property                     on the parent, and $signal.ancestors(', ') to return a list of all the ancestors, separated by                     the specified separator. In all of the above examples \"signal\" would need to be another                     parameter that references an item using an ID.

        :param parameters: The parameters of this FormulaRunInputV1.
        :type: list[str]
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")

        self._parameters = parameters

    @property
    def reduce_formula(self):
        """
        Gets the reduce_formula of this FormulaRunInputV1.
        Used when running a formula across assets, this is a formula that can further reduce the              results of each asset result. The variable $result             must be used to reference the data. Example of sorting the aggregated results:             $result.sort('temperature')'

        :return: The reduce_formula of this FormulaRunInputV1.
        :rtype: str
        """
        return self._reduce_formula

    @reduce_formula.setter
    def reduce_formula(self, reduce_formula):
        """
        Sets the reduce_formula of this FormulaRunInputV1.
        Used when running a formula across assets, this is a formula that can further reduce the              results of each asset result. The variable $result             must be used to reference the data. Example of sorting the aggregated results:             $result.sort('temperature')'

        :param reduce_formula: The reduce_formula of this FormulaRunInputV1.
        :type: str
        """

        self._reduce_formula = reduce_formula

    @property
    def root(self):
        """
        Gets the root of this FormulaRunInputV1.
        Used to run a formula across assets, this is the ID of the root asset whose immediate             children will be iterated. The formula must produce a table.

        :return: The root of this FormulaRunInputV1.
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        """
        Sets the root of this FormulaRunInputV1.
        Used to run a formula across assets, this is the ID of the root asset whose immediate             children will be iterated. The formula must produce a table.

        :param root: The root of this FormulaRunInputV1.
        :type: str
        """

        self._root = root

    @property
    def start(self):
        """
        Gets the start of this FormulaRunInputV1.
        A string representing the starting index of the data to be returned.             The contents and whether or not it is required depends on the series type. For time series: a ISO 8601             timestamp (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm). For numeric (non-time) keys: a double-precision             number, optionally including units. For example: \"2.5ft\" or \"10 °C\"

        :return: The start of this FormulaRunInputV1.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this FormulaRunInputV1.
        A string representing the starting index of the data to be returned.             The contents and whether or not it is required depends on the series type. For time series: a ISO 8601             timestamp (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm). For numeric (non-time) keys: a double-precision             number, optionally including units. For example: \"2.5ft\" or \"10 °C\"

        :param start: The start of this FormulaRunInputV1.
        :type: str
        """

        self._start = start

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
        if not isinstance(other, FormulaRunInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
