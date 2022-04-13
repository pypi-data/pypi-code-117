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


class UserGroupOutputV1(object):
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
        'created_at': 'str',
        'data_id': 'str',
        'data_version_check': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'datasource_name': 'str',
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'id': 'str',
        'is_archived': 'bool',
        'is_enabled': 'bool',
        'is_redacted': 'bool',
        'is_remote_group_editable': 'bool',
        'is_used_in_access_control_entries': 'bool',
        'members': 'list[ItemPreviewV1]',
        'name': 'str',
        'status_message': 'str',
        'sync_token': 'str',
        'translation_key': 'str',
        'type': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'data_id': 'dataId',
        'data_version_check': 'dataVersionCheck',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'datasource_name': 'datasourceName',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_enabled': 'isEnabled',
        'is_redacted': 'isRedacted',
        'is_remote_group_editable': 'isRemoteGroupEditable',
        'is_used_in_access_control_entries': 'isUsedInAccessControlEntries',
        'members': 'members',
        'name': 'name',
        'status_message': 'statusMessage',
        'sync_token': 'syncToken',
        'translation_key': 'translationKey',
        'type': 'type'
    }

    def __init__(self, created_at=None, data_id=None, data_version_check=None, datasource_class=None, datasource_id=None, datasource_name=None, description=None, effective_permissions=None, id=None, is_archived=False, is_enabled=False, is_redacted=False, is_remote_group_editable=False, is_used_in_access_control_entries=False, members=None, name=None, status_message=None, sync_token=None, translation_key=None, type=None):
        """
        UserGroupOutputV1 - a model defined in Swagger
        """

        self._created_at = None
        self._data_id = None
        self._data_version_check = None
        self._datasource_class = None
        self._datasource_id = None
        self._datasource_name = None
        self._description = None
        self._effective_permissions = None
        self._id = None
        self._is_archived = None
        self._is_enabled = None
        self._is_redacted = None
        self._is_remote_group_editable = None
        self._is_used_in_access_control_entries = None
        self._members = None
        self._name = None
        self._status_message = None
        self._sync_token = None
        self._translation_key = None
        self._type = None

        if created_at is not None:
          self.created_at = created_at
        if data_id is not None:
          self.data_id = data_id
        if data_version_check is not None:
          self.data_version_check = data_version_check
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if datasource_name is not None:
          self.datasource_name = datasource_name
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
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
        if is_used_in_access_control_entries is not None:
          self.is_used_in_access_control_entries = is_used_in_access_control_entries
        if members is not None:
          self.members = members
        if name is not None:
          self.name = name
        if status_message is not None:
          self.status_message = status_message
        if sync_token is not None:
          self.sync_token = sync_token
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type

    @property
    def created_at(self):
        """
        Gets the created_at of this UserGroupOutputV1.
        The ISO 8601 date of when the user was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The created_at of this UserGroupOutputV1.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UserGroupOutputV1.
        The ISO 8601 date of when the user was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param created_at: The created_at of this UserGroupOutputV1.
        :type: str
        """

        self._created_at = created_at

    @property
    def data_id(self):
        """
        Gets the data_id of this UserGroupOutputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :return: The data_id of this UserGroupOutputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this UserGroupOutputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :param data_id: The data_id of this UserGroupOutputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def data_version_check(self):
        """
        Gets the data_version_check of this UserGroupOutputV1.
        The data version check string. When updating an existing user group, if the data version check string is unchanged, then the update will be skipped.

        :return: The data_version_check of this UserGroupOutputV1.
        :rtype: str
        """
        return self._data_version_check

    @data_version_check.setter
    def data_version_check(self, data_version_check):
        """
        Sets the data_version_check of this UserGroupOutputV1.
        The data version check string. When updating an existing user group, if the data version check string is unchanged, then the update will be skipped.

        :param data_version_check: The data_version_check of this UserGroupOutputV1.
        :type: str
        """

        self._data_version_check = data_version_check

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this UserGroupOutputV1.
        The datasource class, which is the type of system holding the item, such as OSIsoft PI

        :return: The datasource_class of this UserGroupOutputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this UserGroupOutputV1.
        The datasource class, which is the type of system holding the item, such as OSIsoft PI

        :param datasource_class: The datasource_class of this UserGroupOutputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this UserGroupOutputV1.
        The datasource identifier, which is how the datasource holding this item identifies itself

        :return: The datasource_id of this UserGroupOutputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this UserGroupOutputV1.
        The datasource identifier, which is how the datasource holding this item identifies itself

        :param datasource_id: The datasource_id of this UserGroupOutputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def datasource_name(self):
        """
        Gets the datasource_name of this UserGroupOutputV1.
        The name of the data source (authentication directory) containing the group

        :return: The datasource_name of this UserGroupOutputV1.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        """
        Sets the datasource_name of this UserGroupOutputV1.
        The name of the data source (authentication directory) containing the group

        :param datasource_name: The datasource_name of this UserGroupOutputV1.
        :type: str
        """

        self._datasource_name = datasource_name

    @property
    def description(self):
        """
        Gets the description of this UserGroupOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this UserGroupOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UserGroupOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this UserGroupOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this UserGroupOutputV1.
        The permissions the current user has to the item.

        :return: The effective_permissions of this UserGroupOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this UserGroupOutputV1.
        The permissions the current user has to the item.

        :param effective_permissions: The effective_permissions of this UserGroupOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def id(self):
        """
        Gets the id of this UserGroupOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this UserGroupOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserGroupOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this UserGroupOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this UserGroupOutputV1.
        Whether item is archived

        :return: The is_archived of this UserGroupOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this UserGroupOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this UserGroupOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UserGroupOutputV1.
        Whether the group is enabled

        :return: The is_enabled of this UserGroupOutputV1.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UserGroupOutputV1.
        Whether the group is enabled

        :param is_enabled: The is_enabled of this UserGroupOutputV1.
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this UserGroupOutputV1.
        Whether item is redacted

        :return: The is_redacted of this UserGroupOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this UserGroupOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this UserGroupOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def is_remote_group_editable(self):
        """
        Gets the is_remote_group_editable of this UserGroupOutputV1.
        Whether the user group remains editable in Seeq even when sourced from a remote system.

        :return: The is_remote_group_editable of this UserGroupOutputV1.
        :rtype: bool
        """
        return self._is_remote_group_editable

    @is_remote_group_editable.setter
    def is_remote_group_editable(self, is_remote_group_editable):
        """
        Sets the is_remote_group_editable of this UserGroupOutputV1.
        Whether the user group remains editable in Seeq even when sourced from a remote system.

        :param is_remote_group_editable: The is_remote_group_editable of this UserGroupOutputV1.
        :type: bool
        """

        self._is_remote_group_editable = is_remote_group_editable

    @property
    def is_used_in_access_control_entries(self):
        """
        Gets the is_used_in_access_control_entries of this UserGroupOutputV1.
        Whether the group is used in any access control entries

        :return: The is_used_in_access_control_entries of this UserGroupOutputV1.
        :rtype: bool
        """
        return self._is_used_in_access_control_entries

    @is_used_in_access_control_entries.setter
    def is_used_in_access_control_entries(self, is_used_in_access_control_entries):
        """
        Sets the is_used_in_access_control_entries of this UserGroupOutputV1.
        Whether the group is used in any access control entries

        :param is_used_in_access_control_entries: The is_used_in_access_control_entries of this UserGroupOutputV1.
        :type: bool
        """

        self._is_used_in_access_control_entries = is_used_in_access_control_entries

    @property
    def members(self):
        """
        Gets the members of this UserGroupOutputV1.
        The members of the group

        :return: The members of this UserGroupOutputV1.
        :rtype: list[ItemPreviewV1]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this UserGroupOutputV1.
        The members of the group

        :param members: The members of this UserGroupOutputV1.
        :type: list[ItemPreviewV1]
        """

        self._members = members

    @property
    def name(self):
        """
        Gets the name of this UserGroupOutputV1.
        The human readable name

        :return: The name of this UserGroupOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserGroupOutputV1.
        The human readable name

        :param name: The name of this UserGroupOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def status_message(self):
        """
        Gets the status_message of this UserGroupOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this UserGroupOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this UserGroupOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this UserGroupOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def sync_token(self):
        """
        Gets the sync_token of this UserGroupOutputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be  archived using the Datasources clean-up API.

        :return: The sync_token of this UserGroupOutputV1.
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """
        Sets the sync_token of this UserGroupOutputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be  archived using the Datasources clean-up API.

        :param sync_token: The sync_token of this UserGroupOutputV1.
        :type: str
        """

        self._sync_token = sync_token

    @property
    def translation_key(self):
        """
        Gets the translation_key of this UserGroupOutputV1.
        The item's translation key, if any

        :return: The translation_key of this UserGroupOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this UserGroupOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this UserGroupOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this UserGroupOutputV1.
        The type of the item

        :return: The type of this UserGroupOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserGroupOutputV1.
        The type of the item

        :param type: The type of this UserGroupOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if not isinstance(other, UserGroupOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
