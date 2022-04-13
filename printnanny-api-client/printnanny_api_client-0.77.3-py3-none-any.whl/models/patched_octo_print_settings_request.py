# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class PatchedOctoPrintSettingsRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'events_enabled': 'bool',
        'telemetry_enabled': 'bool',
        'sync_gcode': 'bool',
        'sync_printer_profiles': 'bool',
        'sync_backups': 'bool',
        'auto_backup': 'str',
        'monitoring_auto_start': 'bool',
        'monitoring_auto_pause': 'bool',
        'octoprint_install': 'int'
    }

    attribute_map = {
        'events_enabled': 'events_enabled',
        'telemetry_enabled': 'telemetry_enabled',
        'sync_gcode': 'sync_gcode',
        'sync_printer_profiles': 'sync_printer_profiles',
        'sync_backups': 'sync_backups',
        'auto_backup': 'auto_backup',
        'monitoring_auto_start': 'monitoring_auto_start',
        'monitoring_auto_pause': 'monitoring_auto_pause',
        'octoprint_install': 'octoprint_install'
    }

    def __init__(self, events_enabled=None, telemetry_enabled=None, sync_gcode=None, sync_printer_profiles=None, sync_backups=None, auto_backup=None, monitoring_auto_start=None, monitoring_auto_pause=None, octoprint_install=None, local_vars_configuration=None):  # noqa: E501
        """PatchedOctoPrintSettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._events_enabled = None
        self._telemetry_enabled = None
        self._sync_gcode = None
        self._sync_printer_profiles = None
        self._sync_backups = None
        self._auto_backup = None
        self._monitoring_auto_start = None
        self._monitoring_auto_pause = None
        self._octoprint_install = None
        self.discriminator = None

        if events_enabled is not None:
            self.events_enabled = events_enabled
        if telemetry_enabled is not None:
            self.telemetry_enabled = telemetry_enabled
        if sync_gcode is not None:
            self.sync_gcode = sync_gcode
        if sync_printer_profiles is not None:
            self.sync_printer_profiles = sync_printer_profiles
        if sync_backups is not None:
            self.sync_backups = sync_backups
        if auto_backup is not None:
            self.auto_backup = auto_backup
        if monitoring_auto_start is not None:
            self.monitoring_auto_start = monitoring_auto_start
        if monitoring_auto_pause is not None:
            self.monitoring_auto_pause = monitoring_auto_pause
        if octoprint_install is not None:
            self.octoprint_install = octoprint_install

    @property
    def events_enabled(self):
        """Gets the events_enabled of this PatchedOctoPrintSettingsRequest.  # noqa: E501

        Send OctoPrint events to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html  # noqa: E501

        :return: The events_enabled of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._events_enabled

    @events_enabled.setter
    def events_enabled(self, events_enabled):
        """Sets the events_enabled of this PatchedOctoPrintSettingsRequest.

        Send OctoPrint events to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html  # noqa: E501

        :param events_enabled: The events_enabled of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :type events_enabled: bool
        """

        self._events_enabled = events_enabled

    @property
    def telemetry_enabled(self):
        """Gets the telemetry_enabled of this PatchedOctoPrintSettingsRequest.  # noqa: E501

        Send telemetry data to PrintNanny Cloud for debugging/analytics purposes  # noqa: E501

        :return: The telemetry_enabled of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._telemetry_enabled

    @telemetry_enabled.setter
    def telemetry_enabled(self, telemetry_enabled):
        """Sets the telemetry_enabled of this PatchedOctoPrintSettingsRequest.

        Send telemetry data to PrintNanny Cloud for debugging/analytics purposes  # noqa: E501

        :param telemetry_enabled: The telemetry_enabled of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :type telemetry_enabled: bool
        """

        self._telemetry_enabled = telemetry_enabled

    @property
    def sync_gcode(self):
        """Gets the sync_gcode of this PatchedOctoPrintSettingsRequest.  # noqa: E501

        Sync Gcode files to/from PrintNanny Cloud  # noqa: E501

        :return: The sync_gcode of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sync_gcode

    @sync_gcode.setter
    def sync_gcode(self, sync_gcode):
        """Sets the sync_gcode of this PatchedOctoPrintSettingsRequest.

        Sync Gcode files to/from PrintNanny Cloud  # noqa: E501

        :param sync_gcode: The sync_gcode of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :type sync_gcode: bool
        """

        self._sync_gcode = sync_gcode

    @property
    def sync_printer_profiles(self):
        """Gets the sync_printer_profiles of this PatchedOctoPrintSettingsRequest.  # noqa: E501

        Sync Printer Profiles to/from PrintNanny Cloud  # noqa: E501

        :return: The sync_printer_profiles of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sync_printer_profiles

    @sync_printer_profiles.setter
    def sync_printer_profiles(self, sync_printer_profiles):
        """Sets the sync_printer_profiles of this PatchedOctoPrintSettingsRequest.

        Sync Printer Profiles to/from PrintNanny Cloud  # noqa: E501

        :param sync_printer_profiles: The sync_printer_profiles of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :type sync_printer_profiles: bool
        """

        self._sync_printer_profiles = sync_printer_profiles

    @property
    def sync_backups(self):
        """Gets the sync_backups of this PatchedOctoPrintSettingsRequest.  # noqa: E501

        Upload OctoPrint backups to PrintNanny Cloud  # noqa: E501

        :return: The sync_backups of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sync_backups

    @sync_backups.setter
    def sync_backups(self, sync_backups):
        """Sets the sync_backups of this PatchedOctoPrintSettingsRequest.

        Upload OctoPrint backups to PrintNanny Cloud  # noqa: E501

        :param sync_backups: The sync_backups of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :type sync_backups: bool
        """

        self._sync_backups = sync_backups

    @property
    def auto_backup(self):
        """Gets the auto_backup of this PatchedOctoPrintSettingsRequest.  # noqa: E501


        :return: The auto_backup of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_backup

    @auto_backup.setter
    def auto_backup(self, auto_backup):
        """Sets the auto_backup of this PatchedOctoPrintSettingsRequest.


        :param auto_backup: The auto_backup of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :type auto_backup: str
        """
        if (self.local_vars_configuration.client_side_validation and
                auto_backup is not None and len(auto_backup) > 64):
            raise ValueError("Invalid value for `auto_backup`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                auto_backup is not None and len(auto_backup) < 1):
            raise ValueError("Invalid value for `auto_backup`, length must be greater than or equal to `1`")  # noqa: E501

        self._auto_backup = auto_backup

    @property
    def monitoring_auto_start(self):
        """Gets the monitoring_auto_start of this PatchedOctoPrintSettingsRequest.  # noqa: E501

        Start PrintNanny monitoring automatically when a print job begins  # noqa: E501

        :return: The monitoring_auto_start of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._monitoring_auto_start

    @monitoring_auto_start.setter
    def monitoring_auto_start(self, monitoring_auto_start):
        """Sets the monitoring_auto_start of this PatchedOctoPrintSettingsRequest.

        Start PrintNanny monitoring automatically when a print job begins  # noqa: E501

        :param monitoring_auto_start: The monitoring_auto_start of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :type monitoring_auto_start: bool
        """

        self._monitoring_auto_start = monitoring_auto_start

    @property
    def monitoring_auto_pause(self):
        """Gets the monitoring_auto_pause of this PatchedOctoPrintSettingsRequest.  # noqa: E501

        Pause failing print jobs automatically  # noqa: E501

        :return: The monitoring_auto_pause of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._monitoring_auto_pause

    @monitoring_auto_pause.setter
    def monitoring_auto_pause(self, monitoring_auto_pause):
        """Sets the monitoring_auto_pause of this PatchedOctoPrintSettingsRequest.

        Pause failing print jobs automatically  # noqa: E501

        :param monitoring_auto_pause: The monitoring_auto_pause of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :type monitoring_auto_pause: bool
        """

        self._monitoring_auto_pause = monitoring_auto_pause

    @property
    def octoprint_install(self):
        """Gets the octoprint_install of this PatchedOctoPrintSettingsRequest.  # noqa: E501


        :return: The octoprint_install of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_install

    @octoprint_install.setter
    def octoprint_install(self, octoprint_install):
        """Sets the octoprint_install of this PatchedOctoPrintSettingsRequest.


        :param octoprint_install: The octoprint_install of this PatchedOctoPrintSettingsRequest.  # noqa: E501
        :type octoprint_install: int
        """

        self._octoprint_install = octoprint_install

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchedOctoPrintSettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedOctoPrintSettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
