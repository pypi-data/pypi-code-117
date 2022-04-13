# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ConnectionArgs', 'Connection']

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 cloud_sql: Optional[pulumi.Input['CloudSqlPropertiesArgs']] = None,
                 connection_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Connection resource.
        :param pulumi.Input['CloudSqlPropertiesArgs'] cloud_sql: Cloud SQL properties.
        :param pulumi.Input[str] connection_id: Optional. Connection id that should be assigned to the created connection.
        :param pulumi.Input[str] description: User provided description.
        :param pulumi.Input[str] friendly_name: User provided display name for the connection.
        :param pulumi.Input[str] name: The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`
        """
        if cloud_sql is not None:
            pulumi.set(__self__, "cloud_sql", cloud_sql)
        if connection_id is not None:
            pulumi.set(__self__, "connection_id", connection_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="cloudSql")
    def cloud_sql(self) -> Optional[pulumi.Input['CloudSqlPropertiesArgs']]:
        """
        Cloud SQL properties.
        """
        return pulumi.get(self, "cloud_sql")

    @cloud_sql.setter
    def cloud_sql(self, value: Optional[pulumi.Input['CloudSqlPropertiesArgs']]):
        pulumi.set(self, "cloud_sql", value)

    @property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Connection id that should be assigned to the created connection.
        """
        return pulumi.get(self, "connection_id")

    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User provided description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        User provided display name for the connection.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_sql: Optional[pulumi.Input[pulumi.InputType['CloudSqlPropertiesArgs']]] = None,
                 connection_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new connection.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CloudSqlPropertiesArgs']] cloud_sql: Cloud SQL properties.
        :param pulumi.Input[str] connection_id: Optional. Connection id that should be assigned to the created connection.
        :param pulumi.Input[str] description: User provided description.
        :param pulumi.Input[str] friendly_name: User provided display name for the connection.
        :param pulumi.Input[str] name: The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ConnectionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new connection.

        :param str resource_name: The name of the resource.
        :param ConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_sql: Optional[pulumi.Input[pulumi.InputType['CloudSqlPropertiesArgs']]] = None,
                 connection_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionArgs.__new__(ConnectionArgs)

            __props__.__dict__["cloud_sql"] = cloud_sql
            __props__.__dict__["connection_id"] = connection_id
            __props__.__dict__["description"] = description
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["has_credential"] = None
            __props__.__dict__["last_modified_time"] = None
        super(Connection, __self__).__init__(
            'google-native:bigqueryconnection/v1beta1:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Connection':
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectionArgs.__new__(ConnectionArgs)

        __props__.__dict__["cloud_sql"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["has_credential"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        return Connection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cloudSql")
    def cloud_sql(self) -> pulumi.Output['outputs.CloudSqlPropertiesResponse']:
        """
        Cloud SQL properties.
        """
        return pulumi.get(self, "cloud_sql")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The creation timestamp of the connection.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        User provided description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[str]:
        """
        User provided display name for the connection.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hasCredential")
    def has_credential(self) -> pulumi.Output[bool]:
        """
        True, if credential is configured for this connection.
        """
        return pulumi.get(self, "has_credential")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        """
        The last update timestamp of the connection.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`
        """
        return pulumi.get(self, "name")

