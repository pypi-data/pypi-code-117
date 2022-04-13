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


class AddOnToolOutputV1(object):
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
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'icon_class': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'link_type': 'str',
        'name': 'str',
        'reuse_window': 'bool',
        'sort_key': 'str',
        'status_message': 'str',
        'target_url': 'str',
        'type': 'str',
        'window_details': 'str'
    }

    attribute_map = {
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'icon_class': 'iconClass',
        'id': 'id',
        'is_archived': 'isArchived',
        'link_type': 'linkType',
        'name': 'name',
        'reuse_window': 'reuseWindow',
        'sort_key': 'sortKey',
        'status_message': 'statusMessage',
        'target_url': 'targetUrl',
        'type': 'type',
        'window_details': 'windowDetails'
    }

    def __init__(self, description=None, effective_permissions=None, icon_class=None, id=None, is_archived=False, link_type=None, name=None, reuse_window=False, sort_key=None, status_message=None, target_url=None, type=None, window_details=None):
        """
        AddOnToolOutputV1 - a model defined in Swagger
        """

        self._description = None
        self._effective_permissions = None
        self._icon_class = None
        self._id = None
        self._is_archived = None
        self._link_type = None
        self._name = None
        self._reuse_window = None
        self._sort_key = None
        self._status_message = None
        self._target_url = None
        self._type = None
        self._window_details = None

        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if icon_class is not None:
          self.icon_class = icon_class
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if link_type is not None:
          self.link_type = link_type
        if name is not None:
          self.name = name
        if reuse_window is not None:
          self.reuse_window = reuse_window
        if sort_key is not None:
          self.sort_key = sort_key
        if status_message is not None:
          self.status_message = status_message
        if target_url is not None:
          self.target_url = target_url
        if type is not None:
          self.type = type
        if window_details is not None:
          self.window_details = window_details

    @property
    def description(self):
        """
        Gets the description of this AddOnToolOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AddOnToolOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this AddOnToolOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this AddOnToolOutputV1.
        The permissions the current user has to the item.

        :return: The effective_permissions of this AddOnToolOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this AddOnToolOutputV1.
        The permissions the current user has to the item.

        :param effective_permissions: The effective_permissions of this AddOnToolOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def icon_class(self):
        """
        Gets the icon_class of this AddOnToolOutputV1.
        The icon class to be displayed for the add-on tool (e.g. 'fa fa-magic')

        :return: The icon_class of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._icon_class

    @icon_class.setter
    def icon_class(self, icon_class):
        """
        Sets the icon_class of this AddOnToolOutputV1.
        The icon class to be displayed for the add-on tool (e.g. 'fa fa-magic')

        :param icon_class: The icon_class of this AddOnToolOutputV1.
        :type: str
        """
        if icon_class is None:
            raise ValueError("Invalid value for `icon_class`, must not be `None`")

        self._icon_class = icon_class

    @property
    def id(self):
        """
        Gets the id of this AddOnToolOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AddOnToolOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this AddOnToolOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this AddOnToolOutputV1.

        :return: The is_archived of this AddOnToolOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this AddOnToolOutputV1.

        :param is_archived: The is_archived of this AddOnToolOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def link_type(self):
        """
        Gets the link_type of this AddOnToolOutputV1.
        Add-on tool link type (one of 'window', 'tab' or 'none')

        :return: The link_type of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """
        Sets the link_type of this AddOnToolOutputV1.
        Add-on tool link type (one of 'window', 'tab' or 'none')

        :param link_type: The link_type of this AddOnToolOutputV1.
        :type: str
        """
        if link_type is None:
            raise ValueError("Invalid value for `link_type`, must not be `None`")

        self._link_type = link_type

    @property
    def name(self):
        """
        Gets the name of this AddOnToolOutputV1.
        The human readable name

        :return: The name of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AddOnToolOutputV1.
        The human readable name

        :param name: The name of this AddOnToolOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def reuse_window(self):
        """
        Gets the reuse_window of this AddOnToolOutputV1.
        Whether the window is reused if already opened. Only used when 'linkType' is set to 'window'.

        :return: The reuse_window of this AddOnToolOutputV1.
        :rtype: bool
        """
        return self._reuse_window

    @reuse_window.setter
    def reuse_window(self, reuse_window):
        """
        Sets the reuse_window of this AddOnToolOutputV1.
        Whether the window is reused if already opened. Only used when 'linkType' is set to 'window'.

        :param reuse_window: The reuse_window of this AddOnToolOutputV1.
        :type: bool
        """
        if reuse_window is None:
            raise ValueError("Invalid value for `reuse_window`, must not be `None`")

        self._reuse_window = reuse_window

    @property
    def sort_key(self):
        """
        Gets the sort_key of this AddOnToolOutputV1.
        Determines the order in which Add-On Tools are displayed in the tool panel

        :return: The sort_key of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """
        Sets the sort_key of this AddOnToolOutputV1.
        Determines the order in which Add-On Tools are displayed in the tool panel

        :param sort_key: The sort_key of this AddOnToolOutputV1.
        :type: str
        """
        if sort_key is None:
            raise ValueError("Invalid value for `sort_key`, must not be `None`")

        self._sort_key = sort_key

    @property
    def status_message(self):
        """
        Gets the status_message of this AddOnToolOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this AddOnToolOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this AddOnToolOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def target_url(self):
        """
        Gets the target_url of this AddOnToolOutputV1.
        URL of the target application

        :return: The target_url of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """
        Sets the target_url of this AddOnToolOutputV1.
        URL of the target application

        :param target_url: The target_url of this AddOnToolOutputV1.
        :type: str
        """
        if target_url is None:
            raise ValueError("Invalid value for `target_url`, must not be `None`")

        self._target_url = target_url

    @property
    def type(self):
        """
        Gets the type of this AddOnToolOutputV1.
        The type of the item

        :return: The type of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AddOnToolOutputV1.
        The type of the item

        :param type: The type of this AddOnToolOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def window_details(self):
        """
        Gets the window_details of this AddOnToolOutputV1.
        Display characteristics used when 'linkType' is set to 'window'

        :return: The window_details of this AddOnToolOutputV1.
        :rtype: str
        """
        return self._window_details

    @window_details.setter
    def window_details(self, window_details):
        """
        Sets the window_details of this AddOnToolOutputV1.
        Display characteristics used when 'linkType' is set to 'window'

        :param window_details: The window_details of this AddOnToolOutputV1.
        :type: str
        """
        if window_details is None:
            raise ValueError("Invalid value for `window_details`, must not be `None`")

        self._window_details = window_details

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
        if not isinstance(other, AddOnToolOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
