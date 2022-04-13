# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetParameterGroupResult',
    'AwaitableGetParameterGroupResult',
    'get_parameter_group',
    'get_parameter_group_output',
]

@pulumi.output_type
class GetParameterGroupResult:
    def __init__(__self__, a_rn=None, tags=None):
        if a_rn and not isinstance(a_rn, str):
            raise TypeError("Expected argument 'a_rn' to be a str")
        pulumi.set(__self__, "a_rn", a_rn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="aRN")
    def a_rn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the parameter group.
        """
        return pulumi.get(self, "a_rn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ParameterGroupTag']]:
        """
        An array of key-value pairs to apply to this parameter group.
        """
        return pulumi.get(self, "tags")


class AwaitableGetParameterGroupResult(GetParameterGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetParameterGroupResult(
            a_rn=self.a_rn,
            tags=self.tags)


def get_parameter_group(parameter_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetParameterGroupResult:
    """
    The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.


    :param str parameter_group_name: The name of the parameter group.
    """
    __args__ = dict()
    __args__['parameterGroupName'] = parameter_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:memorydb:getParameterGroup', __args__, opts=opts, typ=GetParameterGroupResult).value

    return AwaitableGetParameterGroupResult(
        a_rn=__ret__.a_rn,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_parameter_group)
def get_parameter_group_output(parameter_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetParameterGroupResult]:
    """
    The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.


    :param str parameter_group_name: The name of the parameter group.
    """
    ...
