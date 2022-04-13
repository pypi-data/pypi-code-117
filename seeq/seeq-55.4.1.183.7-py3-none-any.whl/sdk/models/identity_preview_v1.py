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


class IdentityPreviewV1(object):
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
        'datasource': 'DatasourcePreviewV1',
        'email': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'is_enabled': 'bool',
        'is_redacted': 'bool',
        'is_remote_group_editable': 'bool',
        'name': 'str',
        'translation_key': 'str',
        'type': 'str',
        'username': 'str',
        'username_readable': 'bool'
    }

    attribute_map = {
        'datasource': 'datasource',
        'email': 'email',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_enabled': 'isEnabled',
        'is_redacted': 'isRedacted',
        'is_remote_group_editable': 'isRemoteGroupEditable',
        'name': 'name',
        'translation_key': 'translationKey',
        'type': 'type',
        'username': 'username',
        'username_readable': 'usernameReadable'
    }

    def __init__(self, datasource=None, email=None, id=None, is_archived=False, is_enabled=False, is_redacted=False, is_remote_group_editable=False, name=None, translation_key=None, type=None, username=None, username_readable=False):
        """
        IdentityPreviewV1 - a model defined in Swagger
        """

        self._datasource = None
        self._email = None
        self._id = None
        self._is_archived = None
        self._is_enabled = None
        self._is_redacted = None
        self._is_remote_group_editable = None
        self._name = None
        self._translation_key = None
        self._type = None
        self._username = None
        self._username_readable = None

        if datasource is not None:
          self.datasource = datasource
        if email is not None:
          self.email = email
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_enabled is not None:
          self.is_enabled = is_enabled
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if is_remote_group_editable is not None:
          self.is_remote_group_editable = is_remote_group_editable
        if name is not None:
          self.name = name
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type
        if username is not None:
          self.username = username
        if username_readable is not None:
          self.username_readable = username_readable

    @property
    def datasource(self):
        """
        Gets the datasource of this IdentityPreviewV1.
        The data source (authentication directory) containing the identity

        :return: The datasource of this IdentityPreviewV1.
        :rtype: DatasourcePreviewV1
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """
        Sets the datasource of this IdentityPreviewV1.
        The data source (authentication directory) containing the identity

        :param datasource: The datasource of this IdentityPreviewV1.
        :type: DatasourcePreviewV1
        """

        self._datasource = datasource

    @property
    def email(self):
        """
        Gets the email of this IdentityPreviewV1.
        The email address of the user

        :return: The email of this IdentityPreviewV1.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this IdentityPreviewV1.
        The email address of the user

        :param email: The email of this IdentityPreviewV1.
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """
        Gets the id of this IdentityPreviewV1.
        The ID that can be used to interact with the item

        :return: The id of this IdentityPreviewV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IdentityPreviewV1.
        The ID that can be used to interact with the item

        :param id: The id of this IdentityPreviewV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this IdentityPreviewV1.
        Whether item is archived

        :return: The is_archived of this IdentityPreviewV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this IdentityPreviewV1.
        Whether item is archived

        :param is_archived: The is_archived of this IdentityPreviewV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this IdentityPreviewV1.
        True if the identity is enabled

        :return: The is_enabled of this IdentityPreviewV1.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this IdentityPreviewV1.
        True if the identity is enabled

        :param is_enabled: The is_enabled of this IdentityPreviewV1.
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this IdentityPreviewV1.
        Whether item is redacted

        :return: The is_redacted of this IdentityPreviewV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this IdentityPreviewV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this IdentityPreviewV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def is_remote_group_editable(self):
        """
        Gets the is_remote_group_editable of this IdentityPreviewV1.
        Whether the user group is editable in Seeq even when sourced from a remote system

        :return: The is_remote_group_editable of this IdentityPreviewV1.
        :rtype: bool
        """
        return self._is_remote_group_editable

    @is_remote_group_editable.setter
    def is_remote_group_editable(self, is_remote_group_editable):
        """
        Sets the is_remote_group_editable of this IdentityPreviewV1.
        Whether the user group is editable in Seeq even when sourced from a remote system

        :param is_remote_group_editable: The is_remote_group_editable of this IdentityPreviewV1.
        :type: bool
        """

        self._is_remote_group_editable = is_remote_group_editable

    @property
    def name(self):
        """
        Gets the name of this IdentityPreviewV1.
        The human readable name

        :return: The name of this IdentityPreviewV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IdentityPreviewV1.
        The human readable name

        :param name: The name of this IdentityPreviewV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def translation_key(self):
        """
        Gets the translation_key of this IdentityPreviewV1.
        The item's translation key, if any

        :return: The translation_key of this IdentityPreviewV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this IdentityPreviewV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this IdentityPreviewV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this IdentityPreviewV1.
        The type of the item

        :return: The type of this IdentityPreviewV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IdentityPreviewV1.
        The type of the item

        :param type: The type of this IdentityPreviewV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def username(self):
        """
        Gets the username of this IdentityPreviewV1.
        The username of the user

        :return: The username of this IdentityPreviewV1.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this IdentityPreviewV1.
        The username of the user

        :param username: The username of this IdentityPreviewV1.
        :type: str
        """

        self._username = username

    @property
    def username_readable(self):
        """
        Gets the username_readable of this IdentityPreviewV1.

        :return: The username_readable of this IdentityPreviewV1.
        :rtype: bool
        """
        return self._username_readable

    @username_readable.setter
    def username_readable(self, username_readable):
        """
        Sets the username_readable of this IdentityPreviewV1.

        :param username_readable: The username_readable of this IdentityPreviewV1.
        :type: bool
        """

        self._username_readable = username_readable

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
        if not isinstance(other, IdentityPreviewV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
