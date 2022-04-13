# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetGroupResult',
    'AwaitableGetGroupResult',
    'get_group',
    'get_group_output',
]

@pulumi.output_type
class GetGroupResult:
    def __init__(__self__, arn=None, configuration=None, description=None, resource_query=None, resources=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if configuration and not isinstance(configuration, list):
            raise TypeError("Expected argument 'configuration' to be a list")
        pulumi.set(__self__, "configuration", configuration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if resource_query and not isinstance(resource_query, dict):
            raise TypeError("Expected argument 'resource_query' to be a dict")
        pulumi.set(__self__, "resource_query", resource_query)
        if resources and not isinstance(resources, list):
            raise TypeError("Expected argument 'resources' to be a list")
        pulumi.set(__self__, "resources", resources)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Resource Group ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def configuration(self) -> Optional[Sequence['outputs.GroupConfigurationItem']]:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the resource group
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="resourceQuery")
    def resource_query(self) -> Optional['outputs.GroupResourceQuery']:
        return pulumi.get(self, "resource_query")

    @property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.GroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetGroupResult(GetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupResult(
            arn=self.arn,
            configuration=self.configuration,
            description=self.description,
            resource_query=self.resource_query,
            resources=self.resources,
            tags=self.tags)


def get_group(name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupResult:
    """
    Schema for ResourceGroups::Group


    :param str name: The name of the resource group
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:resourcegroups:getGroup', __args__, opts=opts, typ=GetGroupResult).value

    return AwaitableGetGroupResult(
        arn=__ret__.arn,
        configuration=__ret__.configuration,
        description=__ret__.description,
        resource_query=__ret__.resource_query,
        resources=__ret__.resources,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_group)
def get_group_output(name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupResult]:
    """
    Schema for ResourceGroups::Group


    :param str name: The name of the resource group
    """
    ...
