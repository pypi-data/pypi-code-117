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

__all__ = ['VirtualClusterArgs', 'VirtualCluster']

@pulumi.input_type
class VirtualClusterArgs:
    def __init__(__self__, *,
                 container_provider: pulumi.Input['VirtualClusterContainerProviderArgs'],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualClusterTagArgs']]]] = None):
        """
        The set of arguments for constructing a VirtualCluster resource.
        :param pulumi.Input['VirtualClusterContainerProviderArgs'] container_provider: Container provider of the virtual cluster.
        :param pulumi.Input[str] name: Name of the virtual cluster.
        :param pulumi.Input[Sequence[pulumi.Input['VirtualClusterTagArgs']]] tags: An array of key-value pairs to apply to this virtual cluster.
        """
        pulumi.set(__self__, "container_provider", container_provider)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="containerProvider")
    def container_provider(self) -> pulumi.Input['VirtualClusterContainerProviderArgs']:
        """
        Container provider of the virtual cluster.
        """
        return pulumi.get(self, "container_provider")

    @container_provider.setter
    def container_provider(self, value: pulumi.Input['VirtualClusterContainerProviderArgs']):
        pulumi.set(self, "container_provider", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the virtual cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VirtualClusterTagArgs']]]]:
        """
        An array of key-value pairs to apply to this virtual cluster.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualClusterTagArgs']]]]):
        pulumi.set(self, "tags", value)


class VirtualCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_provider: Optional[pulumi.Input[pulumi.InputType['VirtualClusterContainerProviderArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualClusterTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Schema of AWS::EMRContainers::VirtualCluster Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['VirtualClusterContainerProviderArgs']] container_provider: Container provider of the virtual cluster.
        :param pulumi.Input[str] name: Name of the virtual cluster.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualClusterTagArgs']]]] tags: An array of key-value pairs to apply to this virtual cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Schema of AWS::EMRContainers::VirtualCluster Type

        :param str resource_name: The name of the resource.
        :param VirtualClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_provider: Optional[pulumi.Input[pulumi.InputType['VirtualClusterContainerProviderArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualClusterTagArgs']]]]] = None,
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
            __props__ = VirtualClusterArgs.__new__(VirtualClusterArgs)

            if container_provider is None and not opts.urn:
                raise TypeError("Missing required property 'container_provider'")
            __props__.__dict__["container_provider"] = container_provider
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(VirtualCluster, __self__).__init__(
            'aws-native:emrcontainers:VirtualCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualCluster':
        """
        Get an existing VirtualCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualClusterArgs.__new__(VirtualClusterArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["container_provider"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return VirtualCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="containerProvider")
    def container_provider(self) -> pulumi.Output['outputs.VirtualClusterContainerProvider']:
        """
        Container provider of the virtual cluster.
        """
        return pulumi.get(self, "container_provider")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the virtual cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VirtualClusterTag']]]:
        """
        An array of key-value pairs to apply to this virtual cluster.
        """
        return pulumi.get(self, "tags")

