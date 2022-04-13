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


class DocumentBackupOutputV1(object):
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
        'backup_date': 'str',
        'backup_name': 'str',
        'username': 'str'
    }

    attribute_map = {
        'backup_date': 'backupDate',
        'backup_name': 'backupName',
        'username': 'username'
    }

    def __init__(self, backup_date=None, backup_name=None, username=None):
        """
        DocumentBackupOutputV1 - a model defined in Swagger
        """

        self._backup_date = None
        self._backup_name = None
        self._username = None

        if backup_date is not None:
          self.backup_date = backup_date
        if backup_name is not None:
          self.backup_name = backup_name
        if username is not None:
          self.username = username

    @property
    def backup_date(self):
        """
        Gets the backup_date of this DocumentBackupOutputV1.
        The date of the changes contained in this backup

        :return: The backup_date of this DocumentBackupOutputV1.
        :rtype: str
        """
        return self._backup_date

    @backup_date.setter
    def backup_date(self, backup_date):
        """
        Sets the backup_date of this DocumentBackupOutputV1.
        The date of the changes contained in this backup

        :param backup_date: The backup_date of this DocumentBackupOutputV1.
        :type: str
        """

        self._backup_date = backup_date

    @property
    def backup_name(self):
        """
        Gets the backup_name of this DocumentBackupOutputV1.
        The name of this backup, for use in restoring it

        :return: The backup_name of this DocumentBackupOutputV1.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        """
        Sets the backup_name of this DocumentBackupOutputV1.
        The name of this backup, for use in restoring it

        :param backup_name: The backup_name of this DocumentBackupOutputV1.
        :type: str
        """

        self._backup_name = backup_name

    @property
    def username(self):
        """
        Gets the username of this DocumentBackupOutputV1.
        The name of the user whose change prompted this backup

        :return: The username of this DocumentBackupOutputV1.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this DocumentBackupOutputV1.
        The name of the user whose change prompted this backup

        :param username: The username of this DocumentBackupOutputV1.
        :type: str
        """

        self._username = username

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
        if not isinstance(other, DocumentBackupOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
