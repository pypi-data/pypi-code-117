# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetUserPoolUserResult',
    'AwaitableGetUserPoolUserResult',
    'get_user_pool_user',
    'get_user_pool_user_output',
]

@pulumi.output_type
class GetUserPoolUserResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetUserPoolUserResult(GetUserPoolUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserPoolUserResult(
            id=self.id)


def get_user_pool_user(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserPoolUserResult:
    """
    Resource Type definition for AWS::Cognito::UserPoolUser
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:cognito:getUserPoolUser', __args__, opts=opts, typ=GetUserPoolUserResult).value

    return AwaitableGetUserPoolUserResult(
        id=__ret__.id)


@_utilities.lift_output_func(get_user_pool_user)
def get_user_pool_user_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserPoolUserResult]:
    """
    Resource Type definition for AWS::Cognito::UserPoolUser
    """
    ...
