# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetGroupVersionResult',
    'AwaitableGetGroupVersionResult',
    'get_group_version',
    'get_group_version_output',
]

@pulumi.output_type
class GetGroupVersionResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetGroupVersionResult(GetGroupVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupVersionResult(
            id=self.id)


def get_group_version(id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupVersionResult:
    """
    Resource Type definition for AWS::Greengrass::GroupVersion
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:greengrass:getGroupVersion', __args__, opts=opts, typ=GetGroupVersionResult).value

    return AwaitableGetGroupVersionResult(
        id=__ret__.id)


@_utilities.lift_output_func(get_group_version)
def get_group_version_output(id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupVersionResult]:
    """
    Resource Type definition for AWS::Greengrass::GroupVersion
    """
    ...
