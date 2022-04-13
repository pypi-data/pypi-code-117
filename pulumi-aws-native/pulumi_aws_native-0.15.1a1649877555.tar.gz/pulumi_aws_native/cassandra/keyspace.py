# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['KeyspaceArgs', 'Keyspace']

@pulumi.input_type
class KeyspaceArgs:
    def __init__(__self__, *,
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['KeyspaceTagArgs']]]] = None):
        """
        The set of arguments for constructing a Keyspace resource.
        :param pulumi.Input[str] keyspace_name: Name for Cassandra keyspace
        """
        if keyspace_name is not None:
            pulumi.set(__self__, "keyspace_name", keyspace_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for Cassandra keyspace
        """
        return pulumi.get(self, "keyspace_name")

    @keyspace_name.setter
    def keyspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keyspace_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KeyspaceTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KeyspaceTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Keyspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyspaceTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Cassandra::Keyspace

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] keyspace_name: Name for Cassandra keyspace
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[KeyspaceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Cassandra::Keyspace

        :param str resource_name: The name of the resource.
        :param KeyspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyspaceTagArgs']]]]] = None,
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
            __props__ = KeyspaceArgs.__new__(KeyspaceArgs)

            __props__.__dict__["keyspace_name"] = keyspace_name
            __props__.__dict__["tags"] = tags
        super(Keyspace, __self__).__init__(
            'aws-native:cassandra:Keyspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Keyspace':
        """
        Get an existing Keyspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KeyspaceArgs.__new__(KeyspaceArgs)

        __props__.__dict__["keyspace_name"] = None
        __props__.__dict__["tags"] = None
        return Keyspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name for Cassandra keyspace
        """
        return pulumi.get(self, "keyspace_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.KeyspaceTag']]]:
        return pulumi.get(self, "tags")

