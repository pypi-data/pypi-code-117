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


class FormulaErrorOutputV1(object):
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
        'column': 'int',
        'error_category': 'str',
        'error_type': 'str',
        'line': 'int',
        'message': 'str',
        'status_message': 'str'
    }

    attribute_map = {
        'column': 'column',
        'error_category': 'errorCategory',
        'error_type': 'errorType',
        'line': 'line',
        'message': 'message',
        'status_message': 'statusMessage'
    }

    def __init__(self, column=None, error_category=None, error_type=None, line=None, message=None, status_message=None):
        """
        FormulaErrorOutputV1 - a model defined in Swagger
        """

        self._column = None
        self._error_category = None
        self._error_type = None
        self._line = None
        self._message = None
        self._status_message = None

        if column is not None:
          self.column = column
        if error_category is not None:
          self.error_category = error_category
        if error_type is not None:
          self.error_type = error_type
        if line is not None:
          self.line = line
        if message is not None:
          self.message = message
        if status_message is not None:
          self.status_message = status_message

    @property
    def column(self):
        """
        Gets the column of this FormulaErrorOutputV1.
        The column of the formula that resulted in an error

        :return: The column of this FormulaErrorOutputV1.
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """
        Sets the column of this FormulaErrorOutputV1.
        The column of the formula that resulted in an error

        :param column: The column of this FormulaErrorOutputV1.
        :type: int
        """

        self._column = column

    @property
    def error_category(self):
        """
        Gets the error_category of this FormulaErrorOutputV1.
        The category of the formula error, i.e. when it was encountered

        :return: The error_category of this FormulaErrorOutputV1.
        :rtype: str
        """
        return self._error_category

    @error_category.setter
    def error_category(self, error_category):
        """
        Sets the error_category of this FormulaErrorOutputV1.
        The category of the formula error, i.e. when it was encountered

        :param error_category: The error_category of this FormulaErrorOutputV1.
        :type: str
        """
        allowed_values = ["SYNTAX", "METADATA", "RUNTIME", "UPSTREAM"]
        if error_category not in allowed_values:
            raise ValueError(
                "Invalid value for `error_category` ({0}), must be one of {1}"
                .format(error_category, allowed_values)
            )

        self._error_category = error_category

    @property
    def error_type(self):
        """
        Gets the error_type of this FormulaErrorOutputV1.
        The type of formula error that occurred

        :return: The error_type of this FormulaErrorOutputV1.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this FormulaErrorOutputV1.
        The type of formula error that occurred

        :param error_type: The error_type of this FormulaErrorOutputV1.
        :type: str
        """
        allowed_values = ["SYNTAX_ERROR", "METADATA_ERROR", "DATA_SPEC_ERROR", "RUNTIME_ERROR", "INCOMPATIBLE_UNITS", "MAX_DURATION_REQUIRED", "MAX_DURATION_PROHIBITED", "CONTINUOUS_REQUIRED", "PROPERTY_ERROR", "LOCALLY_CONSTANT", "ILLEGAL_VALUE", "ILLEGAL_PARAMETER", "UPSTREAM_ERROR"]
        if error_type not in allowed_values:
            raise ValueError(
                "Invalid value for `error_type` ({0}), must be one of {1}"
                .format(error_type, allowed_values)
            )

        self._error_type = error_type

    @property
    def line(self):
        """
        Gets the line of this FormulaErrorOutputV1.
        The line of the formula that resulted in an error

        :return: The line of this FormulaErrorOutputV1.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """
        Sets the line of this FormulaErrorOutputV1.
        The line of the formula that resulted in an error

        :param line: The line of this FormulaErrorOutputV1.
        :type: int
        """

        self._line = line

    @property
    def message(self):
        """
        Gets the message of this FormulaErrorOutputV1.
        An error message for the compiled formula

        :return: The message of this FormulaErrorOutputV1.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this FormulaErrorOutputV1.
        An error message for the compiled formula

        :param message: The message of this FormulaErrorOutputV1.
        :type: str
        """

        self._message = message

    @property
    def status_message(self):
        """
        Gets the status_message of this FormulaErrorOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this FormulaErrorOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this FormulaErrorOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this FormulaErrorOutputV1.
        :type: str
        """

        self._status_message = status_message

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
        if not isinstance(other, FormulaErrorOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
