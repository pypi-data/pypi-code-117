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


class ConnectionStatusOutputV1(object):
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
        'agent_name': 'str',
        'connection_id': 'str',
        'connection_message': 'str',
        'connector_name': 'str',
        'datasource_managed': 'bool',
        'disabled_at': 'str',
        'disabled_by': 'str',
        'last_successful_connected_at': 'str',
        'name': 'str',
        'status': 'str',
        'sync_status': 'str'
    }

    attribute_map = {
        'agent_name': 'agentName',
        'connection_id': 'connectionId',
        'connection_message': 'connectionMessage',
        'connector_name': 'connectorName',
        'datasource_managed': 'datasourceManaged',
        'disabled_at': 'disabledAt',
        'disabled_by': 'disabledBy',
        'last_successful_connected_at': 'lastSuccessfulConnectedAt',
        'name': 'name',
        'status': 'status',
        'sync_status': 'syncStatus'
    }

    def __init__(self, agent_name=None, connection_id=None, connection_message=None, connector_name=None, datasource_managed=False, disabled_at=None, disabled_by=None, last_successful_connected_at=None, name=None, status=None, sync_status=None):
        """
        ConnectionStatusOutputV1 - a model defined in Swagger
        """

        self._agent_name = None
        self._connection_id = None
        self._connection_message = None
        self._connector_name = None
        self._datasource_managed = None
        self._disabled_at = None
        self._disabled_by = None
        self._last_successful_connected_at = None
        self._name = None
        self._status = None
        self._sync_status = None

        if agent_name is not None:
          self.agent_name = agent_name
        if connection_id is not None:
          self.connection_id = connection_id
        if connection_message is not None:
          self.connection_message = connection_message
        if connector_name is not None:
          self.connector_name = connector_name
        if datasource_managed is not None:
          self.datasource_managed = datasource_managed
        if disabled_at is not None:
          self.disabled_at = disabled_at
        if disabled_by is not None:
          self.disabled_by = disabled_by
        if last_successful_connected_at is not None:
          self.last_successful_connected_at = last_successful_connected_at
        if name is not None:
          self.name = name
        if status is not None:
          self.status = status
        if sync_status is not None:
          self.sync_status = sync_status

    @property
    def agent_name(self):
        """
        Gets the agent_name of this ConnectionStatusOutputV1.
        The name identifying the agent where the connector is hosted

        :return: The agent_name of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """
        Sets the agent_name of this ConnectionStatusOutputV1.
        The name identifying the agent where the connector is hosted

        :param agent_name: The agent_name of this ConnectionStatusOutputV1.
        :type: str
        """
        if agent_name is None:
            raise ValueError("Invalid value for `agent_name`, must not be `None`")

        self._agent_name = agent_name

    @property
    def connection_id(self):
        """
        Gets the connection_id of this ConnectionStatusOutputV1.
        The connectionID of the connection. This ID uniquely identifies this connection but it would not necessary be in the form of an UUID

        :return: The connection_id of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this ConnectionStatusOutputV1.
        The connectionID of the connection. This ID uniquely identifies this connection but it would not necessary be in the form of an UUID

        :param connection_id: The connection_id of this ConnectionStatusOutputV1.
        :type: str
        """
        if connection_id is None:
            raise ValueError("Invalid value for `connection_id`, must not be `None`")

        self._connection_id = connection_id

    @property
    def connection_message(self):
        """
        Gets the connection_message of this ConnectionStatusOutputV1.
        The message indicating the status of the connection to the datasource (e.g. reason for disconnection)

        :return: The connection_message of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._connection_message

    @connection_message.setter
    def connection_message(self, connection_message):
        """
        Sets the connection_message of this ConnectionStatusOutputV1.
        The message indicating the status of the connection to the datasource (e.g. reason for disconnection)

        :param connection_message: The connection_message of this ConnectionStatusOutputV1.
        :type: str
        """

        self._connection_message = connection_message

    @property
    def connector_name(self):
        """
        Gets the connector_name of this ConnectionStatusOutputV1.
        The name identifying the connector

        :return: The connector_name of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """
        Sets the connector_name of this ConnectionStatusOutputV1.
        The name identifying the connector

        :param connector_name: The connector_name of this ConnectionStatusOutputV1.
        :type: str
        """

        self._connector_name = connector_name

    @property
    def datasource_managed(self):
        """
        Gets the datasource_managed of this ConnectionStatusOutputV1.
        Indicates if the configuration is managed by the datasource and cannot be changed in Seeq

        :return: The datasource_managed of this ConnectionStatusOutputV1.
        :rtype: bool
        """
        return self._datasource_managed

    @datasource_managed.setter
    def datasource_managed(self, datasource_managed):
        """
        Sets the datasource_managed of this ConnectionStatusOutputV1.
        Indicates if the configuration is managed by the datasource and cannot be changed in Seeq

        :param datasource_managed: The datasource_managed of this ConnectionStatusOutputV1.
        :type: bool
        """

        self._datasource_managed = datasource_managed

    @property
    def disabled_at(self):
        """
        Gets the disabled_at of this ConnectionStatusOutputV1.
        The ISO 8601 date of when the connection was disabled (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The disabled_at of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._disabled_at

    @disabled_at.setter
    def disabled_at(self, disabled_at):
        """
        Sets the disabled_at of this ConnectionStatusOutputV1.
        The ISO 8601 date of when the connection was disabled (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param disabled_at: The disabled_at of this ConnectionStatusOutputV1.
        :type: str
        """

        self._disabled_at = disabled_at

    @property
    def disabled_by(self):
        """
        Gets the disabled_by of this ConnectionStatusOutputV1.
        The username of the user who disabled the connection

        :return: The disabled_by of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._disabled_by

    @disabled_by.setter
    def disabled_by(self, disabled_by):
        """
        Sets the disabled_by of this ConnectionStatusOutputV1.
        The username of the user who disabled the connection

        :param disabled_by: The disabled_by of this ConnectionStatusOutputV1.
        :type: str
        """

        self._disabled_by = disabled_by

    @property
    def last_successful_connected_at(self):
        """
        Gets the last_successful_connected_at of this ConnectionStatusOutputV1.
        The ISO 8601 date of the last successful connection to the external datasource(YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The last_successful_connected_at of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._last_successful_connected_at

    @last_successful_connected_at.setter
    def last_successful_connected_at(self, last_successful_connected_at):
        """
        Sets the last_successful_connected_at of this ConnectionStatusOutputV1.
        The ISO 8601 date of the last successful connection to the external datasource(YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param last_successful_connected_at: The last_successful_connected_at of this ConnectionStatusOutputV1.
        :type: str
        """

        self._last_successful_connected_at = last_successful_connected_at

    @property
    def name(self):
        """
        Gets the name of this ConnectionStatusOutputV1.
        The name of this connection. The name should represent the specific data source to which this connection connects.  Example: AMAZONA-4RV912N

        :return: The name of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectionStatusOutputV1.
        The name of this connection. The name should represent the specific data source to which this connection connects.  Example: AMAZONA-4RV912N

        :param name: The name of this ConnectionStatusOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def status(self):
        """
        Gets the status of this ConnectionStatusOutputV1.
        The status of the current connection between the datasource and the connector. Valid values are CONNECTING, CONNECTED, DISCONNECTED and DISABLED. If the state is DISCONNECTED (or CONNECTING), it could be caused by a failure in the connection between the connector and its datasource or a failed connection between the Seeq application server and the agent hosting this connector. See connectionMessage.

        :return: The status of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConnectionStatusOutputV1.
        The status of the current connection between the datasource and the connector. Valid values are CONNECTING, CONNECTED, DISCONNECTED and DISABLED. If the state is DISCONNECTED (or CONNECTING), it could be caused by a failure in the connection between the connector and its datasource or a failed connection between the Seeq application server and the agent hosting this connector. See connectionMessage.

        :param status: The status of this ConnectionStatusOutputV1.
        :type: str
        """

        self._status = status

    @property
    def sync_status(self):
        """
        Gets the sync_status of this ConnectionStatusOutputV1.
        The synchronization status of the current connection between the datasource and this connector. Valid values are UNKNOWN, SYNC_INITIALIZING, SYNC_IN_PROGRESS, SYNC_COMPLETE, SYNC_ARCHIVING_DELETED_ITEMS

        :return: The sync_status of this ConnectionStatusOutputV1.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """
        Sets the sync_status of this ConnectionStatusOutputV1.
        The synchronization status of the current connection between the datasource and this connector. Valid values are UNKNOWN, SYNC_INITIALIZING, SYNC_IN_PROGRESS, SYNC_COMPLETE, SYNC_ARCHIVING_DELETED_ITEMS

        :param sync_status: The sync_status of this ConnectionStatusOutputV1.
        :type: str
        """

        self._sync_status = sync_status

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
        if not isinstance(other, ConnectionStatusOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
