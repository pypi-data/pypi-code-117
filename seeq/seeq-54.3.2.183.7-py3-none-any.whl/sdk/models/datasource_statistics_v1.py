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


class DatasourceStatisticsV1(object):
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
        'median_datasource_nanos': 'int',
        'median_queue_nanos': 'int',
        'median_total_nanos': 'int',
        'most_recent_cancellation': 'str',
        'most_recent_failure': 'str',
        'most_recent_success': 'str',
        'most_recent_timeout': 'str',
        'num_cancellations': 'int',
        'num_failures': 'int',
        'num_successes': 'int',
        'num_timeouts': 'int',
        'total_num_datums': 'int'
    }

    attribute_map = {
        'median_datasource_nanos': 'medianDatasourceNanos',
        'median_queue_nanos': 'medianQueueNanos',
        'median_total_nanos': 'medianTotalNanos',
        'most_recent_cancellation': 'mostRecentCancellation',
        'most_recent_failure': 'mostRecentFailure',
        'most_recent_success': 'mostRecentSuccess',
        'most_recent_timeout': 'mostRecentTimeout',
        'num_cancellations': 'numCancellations',
        'num_failures': 'numFailures',
        'num_successes': 'numSuccesses',
        'num_timeouts': 'numTimeouts',
        'total_num_datums': 'totalNumDatums'
    }

    def __init__(self, median_datasource_nanos=None, median_queue_nanos=None, median_total_nanos=None, most_recent_cancellation=None, most_recent_failure=None, most_recent_success=None, most_recent_timeout=None, num_cancellations=None, num_failures=None, num_successes=None, num_timeouts=None, total_num_datums=None):
        """
        DatasourceStatisticsV1 - a model defined in Swagger
        """

        self._median_datasource_nanos = None
        self._median_queue_nanos = None
        self._median_total_nanos = None
        self._most_recent_cancellation = None
        self._most_recent_failure = None
        self._most_recent_success = None
        self._most_recent_timeout = None
        self._num_cancellations = None
        self._num_failures = None
        self._num_successes = None
        self._num_timeouts = None
        self._total_num_datums = None

        if median_datasource_nanos is not None:
          self.median_datasource_nanos = median_datasource_nanos
        if median_queue_nanos is not None:
          self.median_queue_nanos = median_queue_nanos
        if median_total_nanos is not None:
          self.median_total_nanos = median_total_nanos
        if most_recent_cancellation is not None:
          self.most_recent_cancellation = most_recent_cancellation
        if most_recent_failure is not None:
          self.most_recent_failure = most_recent_failure
        if most_recent_success is not None:
          self.most_recent_success = most_recent_success
        if most_recent_timeout is not None:
          self.most_recent_timeout = most_recent_timeout
        if num_cancellations is not None:
          self.num_cancellations = num_cancellations
        if num_failures is not None:
          self.num_failures = num_failures
        if num_successes is not None:
          self.num_successes = num_successes
        if num_timeouts is not None:
          self.num_timeouts = num_timeouts
        if total_num_datums is not None:
          self.total_num_datums = total_num_datums

    @property
    def median_datasource_nanos(self):
        """
        Gets the median_datasource_nanos of this DatasourceStatisticsV1.
        The median duration that recent requests to this datasource spend running at the connector, in nanoseconds. If there were no recent requests, the value will be reported as 0.

        :return: The median_datasource_nanos of this DatasourceStatisticsV1.
        :rtype: int
        """
        return self._median_datasource_nanos

    @median_datasource_nanos.setter
    def median_datasource_nanos(self, median_datasource_nanos):
        """
        Sets the median_datasource_nanos of this DatasourceStatisticsV1.
        The median duration that recent requests to this datasource spend running at the connector, in nanoseconds. If there were no recent requests, the value will be reported as 0.

        :param median_datasource_nanos: The median_datasource_nanos of this DatasourceStatisticsV1.
        :type: int
        """

        self._median_datasource_nanos = median_datasource_nanos

    @property
    def median_queue_nanos(self):
        """
        Gets the median_queue_nanos of this DatasourceStatisticsV1.
        The median duration that recent requests to this datasource spend in a queue at the connector, in nanoseconds. If there were no recent requests, the value will be reported as 0.

        :return: The median_queue_nanos of this DatasourceStatisticsV1.
        :rtype: int
        """
        return self._median_queue_nanos

    @median_queue_nanos.setter
    def median_queue_nanos(self, median_queue_nanos):
        """
        Sets the median_queue_nanos of this DatasourceStatisticsV1.
        The median duration that recent requests to this datasource spend in a queue at the connector, in nanoseconds. If there were no recent requests, the value will be reported as 0.

        :param median_queue_nanos: The median_queue_nanos of this DatasourceStatisticsV1.
        :type: int
        """

        self._median_queue_nanos = median_queue_nanos

    @property
    def median_total_nanos(self):
        """
        Gets the median_total_nanos of this DatasourceStatisticsV1.
        The median duration that recent requests to this datasource spend running in total, from the perspective of the Seeq server. This measurement includes network latency to the agent/connector, queueing on the agent/connector, and processing on the agent/connector. If there were no recent requests, the value will be reported as 0.

        :return: The median_total_nanos of this DatasourceStatisticsV1.
        :rtype: int
        """
        return self._median_total_nanos

    @median_total_nanos.setter
    def median_total_nanos(self, median_total_nanos):
        """
        Sets the median_total_nanos of this DatasourceStatisticsV1.
        The median duration that recent requests to this datasource spend running in total, from the perspective of the Seeq server. This measurement includes network latency to the agent/connector, queueing on the agent/connector, and processing on the agent/connector. If there were no recent requests, the value will be reported as 0.

        :param median_total_nanos: The median_total_nanos of this DatasourceStatisticsV1.
        :type: int
        """

        self._median_total_nanos = median_total_nanos

    @property
    def most_recent_cancellation(self):
        """
        Gets the most_recent_cancellation of this DatasourceStatisticsV1.
        The time of the most recent cancelled request, in ISO-8601 format

        :return: The most_recent_cancellation of this DatasourceStatisticsV1.
        :rtype: str
        """
        return self._most_recent_cancellation

    @most_recent_cancellation.setter
    def most_recent_cancellation(self, most_recent_cancellation):
        """
        Sets the most_recent_cancellation of this DatasourceStatisticsV1.
        The time of the most recent cancelled request, in ISO-8601 format

        :param most_recent_cancellation: The most_recent_cancellation of this DatasourceStatisticsV1.
        :type: str
        """

        self._most_recent_cancellation = most_recent_cancellation

    @property
    def most_recent_failure(self):
        """
        Gets the most_recent_failure of this DatasourceStatisticsV1.
        The time of the most recent failed request, in ISO-8601 format

        :return: The most_recent_failure of this DatasourceStatisticsV1.
        :rtype: str
        """
        return self._most_recent_failure

    @most_recent_failure.setter
    def most_recent_failure(self, most_recent_failure):
        """
        Sets the most_recent_failure of this DatasourceStatisticsV1.
        The time of the most recent failed request, in ISO-8601 format

        :param most_recent_failure: The most_recent_failure of this DatasourceStatisticsV1.
        :type: str
        """

        self._most_recent_failure = most_recent_failure

    @property
    def most_recent_success(self):
        """
        Gets the most_recent_success of this DatasourceStatisticsV1.
        The time of the most recent successful request, in ISO-8601 format

        :return: The most_recent_success of this DatasourceStatisticsV1.
        :rtype: str
        """
        return self._most_recent_success

    @most_recent_success.setter
    def most_recent_success(self, most_recent_success):
        """
        Sets the most_recent_success of this DatasourceStatisticsV1.
        The time of the most recent successful request, in ISO-8601 format

        :param most_recent_success: The most_recent_success of this DatasourceStatisticsV1.
        :type: str
        """

        self._most_recent_success = most_recent_success

    @property
    def most_recent_timeout(self):
        """
        Gets the most_recent_timeout of this DatasourceStatisticsV1.
        The time of the most recent timed-out request, in ISO-8601 format

        :return: The most_recent_timeout of this DatasourceStatisticsV1.
        :rtype: str
        """
        return self._most_recent_timeout

    @most_recent_timeout.setter
    def most_recent_timeout(self, most_recent_timeout):
        """
        Sets the most_recent_timeout of this DatasourceStatisticsV1.
        The time of the most recent timed-out request, in ISO-8601 format

        :param most_recent_timeout: The most_recent_timeout of this DatasourceStatisticsV1.
        :type: str
        """

        self._most_recent_timeout = most_recent_timeout

    @property
    def num_cancellations(self):
        """
        Gets the num_cancellations of this DatasourceStatisticsV1.
        Total number of cancelled requests to this datasource since the last restart of Seeq server.

        :return: The num_cancellations of this DatasourceStatisticsV1.
        :rtype: int
        """
        return self._num_cancellations

    @num_cancellations.setter
    def num_cancellations(self, num_cancellations):
        """
        Sets the num_cancellations of this DatasourceStatisticsV1.
        Total number of cancelled requests to this datasource since the last restart of Seeq server.

        :param num_cancellations: The num_cancellations of this DatasourceStatisticsV1.
        :type: int
        """

        self._num_cancellations = num_cancellations

    @property
    def num_failures(self):
        """
        Gets the num_failures of this DatasourceStatisticsV1.
        Total number of failed requests to this datasource since the last restart of Seeq server.

        :return: The num_failures of this DatasourceStatisticsV1.
        :rtype: int
        """
        return self._num_failures

    @num_failures.setter
    def num_failures(self, num_failures):
        """
        Sets the num_failures of this DatasourceStatisticsV1.
        Total number of failed requests to this datasource since the last restart of Seeq server.

        :param num_failures: The num_failures of this DatasourceStatisticsV1.
        :type: int
        """

        self._num_failures = num_failures

    @property
    def num_successes(self):
        """
        Gets the num_successes of this DatasourceStatisticsV1.
        Total number of successful requests to this datasource since the last restart of Seeq server.

        :return: The num_successes of this DatasourceStatisticsV1.
        :rtype: int
        """
        return self._num_successes

    @num_successes.setter
    def num_successes(self, num_successes):
        """
        Sets the num_successes of this DatasourceStatisticsV1.
        Total number of successful requests to this datasource since the last restart of Seeq server.

        :param num_successes: The num_successes of this DatasourceStatisticsV1.
        :type: int
        """

        self._num_successes = num_successes

    @property
    def num_timeouts(self):
        """
        Gets the num_timeouts of this DatasourceStatisticsV1.
        Total number of timed-out requests to this datasource since the last restart of Seeq server.

        :return: The num_timeouts of this DatasourceStatisticsV1.
        :rtype: int
        """
        return self._num_timeouts

    @num_timeouts.setter
    def num_timeouts(self, num_timeouts):
        """
        Sets the num_timeouts of this DatasourceStatisticsV1.
        Total number of timed-out requests to this datasource since the last restart of Seeq server.

        :param num_timeouts: The num_timeouts of this DatasourceStatisticsV1.
        :type: int
        """

        self._num_timeouts = num_timeouts

    @property
    def total_num_datums(self):
        """
        Gets the total_num_datums of this DatasourceStatisticsV1.
        Total number of datums (i.e, samples, capsules, or rows) that were received in response to requests to this datasource since the last restart of Seeq server.

        :return: The total_num_datums of this DatasourceStatisticsV1.
        :rtype: int
        """
        return self._total_num_datums

    @total_num_datums.setter
    def total_num_datums(self, total_num_datums):
        """
        Sets the total_num_datums of this DatasourceStatisticsV1.
        Total number of datums (i.e, samples, capsules, or rows) that were received in response to requests to this datasource since the last restart of Seeq server.

        :param total_num_datums: The total_num_datums of this DatasourceStatisticsV1.
        :type: int
        """

        self._total_num_datums = total_num_datums

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
        if not isinstance(other, DatasourceStatisticsV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
