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


class DatasourceStatusV1(object):
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
        'datasource_class': 'str',
        'datasource_guid': 'str',
        'datasource_id': 'str',
        'datasource_name': 'str',
        'enabled': 'bool',
        'seeq_internal': 'bool',
        'statistics': 'DatasourceStatisticsV1',
        'stored_in_seeq': 'bool'
    }

    attribute_map = {
        'datasource_class': 'datasourceClass',
        'datasource_guid': 'datasourceGuid',
        'datasource_id': 'datasourceId',
        'datasource_name': 'datasourceName',
        'enabled': 'enabled',
        'seeq_internal': 'seeqInternal',
        'statistics': 'statistics',
        'stored_in_seeq': 'storedInSeeq'
    }

    def __init__(self, datasource_class=None, datasource_guid=None, datasource_id=None, datasource_name=None, enabled=False, seeq_internal=False, statistics=None, stored_in_seeq=False):
        """
        DatasourceStatusV1 - a model defined in Swagger
        """

        self._datasource_class = None
        self._datasource_guid = None
        self._datasource_id = None
        self._datasource_name = None
        self._enabled = None
        self._seeq_internal = None
        self._statistics = None
        self._stored_in_seeq = None

        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_guid is not None:
          self.datasource_guid = datasource_guid
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if datasource_name is not None:
          self.datasource_name = datasource_name
        if enabled is not None:
          self.enabled = enabled
        if seeq_internal is not None:
          self.seeq_internal = seeq_internal
        if statistics is not None:
          self.statistics = statistics
        if stored_in_seeq is not None:
          self.stored_in_seeq = stored_in_seeq

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this DatasourceStatusV1.
        The class of the datasource

        :return: The datasource_class of this DatasourceStatusV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this DatasourceStatusV1.
        The class of the datasource

        :param datasource_class: The datasource_class of this DatasourceStatusV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_guid(self):
        """
        Gets the datasource_guid of this DatasourceStatusV1.
        The Seeq ID of the datasource

        :return: The datasource_guid of this DatasourceStatusV1.
        :rtype: str
        """
        return self._datasource_guid

    @datasource_guid.setter
    def datasource_guid(self, datasource_guid):
        """
        Sets the datasource_guid of this DatasourceStatusV1.
        The Seeq ID of the datasource

        :param datasource_guid: The datasource_guid of this DatasourceStatusV1.
        :type: str
        """

        self._datasource_guid = datasource_guid

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this DatasourceStatusV1.
        The ID of the datasource

        :return: The datasource_id of this DatasourceStatusV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this DatasourceStatusV1.
        The ID of the datasource

        :param datasource_id: The datasource_id of this DatasourceStatusV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def datasource_name(self):
        """
        Gets the datasource_name of this DatasourceStatusV1.
        The name of the datasource

        :return: The datasource_name of this DatasourceStatusV1.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        """
        Sets the datasource_name of this DatasourceStatusV1.
        The name of the datasource

        :param datasource_name: The datasource_name of this DatasourceStatusV1.
        :type: str
        """

        self._datasource_name = datasource_name

    @property
    def enabled(self):
        """
        Gets the enabled of this DatasourceStatusV1.
        Whether the datasource is enabled

        :return: The enabled of this DatasourceStatusV1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this DatasourceStatusV1.
        Whether the datasource is enabled

        :param enabled: The enabled of this DatasourceStatusV1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def seeq_internal(self):
        """
        Gets the seeq_internal of this DatasourceStatusV1.
        Whether this datasource is internal to Seeq (System Datasource) or not.

        :return: The seeq_internal of this DatasourceStatusV1.
        :rtype: bool
        """
        return self._seeq_internal

    @seeq_internal.setter
    def seeq_internal(self, seeq_internal):
        """
        Sets the seeq_internal of this DatasourceStatusV1.
        Whether this datasource is internal to Seeq (System Datasource) or not.

        :param seeq_internal: The seeq_internal of this DatasourceStatusV1.
        :type: bool
        """

        self._seeq_internal = seeq_internal

    @property
    def statistics(self):
        """
        Gets the statistics of this DatasourceStatusV1.
        Statistics about the current status of the datasource

        :return: The statistics of this DatasourceStatusV1.
        :rtype: DatasourceStatisticsV1
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this DatasourceStatusV1.
        Statistics about the current status of the datasource

        :param statistics: The statistics of this DatasourceStatusV1.
        :type: DatasourceStatisticsV1
        """

        self._statistics = statistics

    @property
    def stored_in_seeq(self):
        """
        Gets the stored_in_seeq of this DatasourceStatusV1.
        Whether the actual data is stored in Seeq or not.

        :return: The stored_in_seeq of this DatasourceStatusV1.
        :rtype: bool
        """
        return self._stored_in_seeq

    @stored_in_seeq.setter
    def stored_in_seeq(self, stored_in_seeq):
        """
        Sets the stored_in_seeq of this DatasourceStatusV1.
        Whether the actual data is stored in Seeq or not.

        :param stored_in_seeq: The stored_in_seeq of this DatasourceStatusV1.
        :type: bool
        """

        self._stored_in_seeq = stored_in_seeq

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
        if not isinstance(other, DatasourceStatusV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
