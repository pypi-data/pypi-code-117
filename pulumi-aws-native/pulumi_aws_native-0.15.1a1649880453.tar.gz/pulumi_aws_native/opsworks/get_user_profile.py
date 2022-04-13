# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetUserProfileResult',
    'AwaitableGetUserProfileResult',
    'get_user_profile',
    'get_user_profile_output',
]

@pulumi.output_type
class GetUserProfileResult:
    def __init__(__self__, allow_self_management=None, id=None, ssh_public_key=None, ssh_username=None):
        if allow_self_management and not isinstance(allow_self_management, bool):
            raise TypeError("Expected argument 'allow_self_management' to be a bool")
        pulumi.set(__self__, "allow_self_management", allow_self_management)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ssh_public_key and not isinstance(ssh_public_key, str):
            raise TypeError("Expected argument 'ssh_public_key' to be a str")
        pulumi.set(__self__, "ssh_public_key", ssh_public_key)
        if ssh_username and not isinstance(ssh_username, str):
            raise TypeError("Expected argument 'ssh_username' to be a str")
        pulumi.set(__self__, "ssh_username", ssh_username)

    @property
    @pulumi.getter(name="allowSelfManagement")
    def allow_self_management(self) -> Optional[bool]:
        return pulumi.get(self, "allow_self_management")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> Optional[str]:
        return pulumi.get(self, "ssh_public_key")

    @property
    @pulumi.getter(name="sshUsername")
    def ssh_username(self) -> Optional[str]:
        return pulumi.get(self, "ssh_username")


class AwaitableGetUserProfileResult(GetUserProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserProfileResult(
            allow_self_management=self.allow_self_management,
            id=self.id,
            ssh_public_key=self.ssh_public_key,
            ssh_username=self.ssh_username)


def get_user_profile(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserProfileResult:
    """
    Resource Type definition for AWS::OpsWorks::UserProfile
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:opsworks:getUserProfile', __args__, opts=opts, typ=GetUserProfileResult).value

    return AwaitableGetUserProfileResult(
        allow_self_management=__ret__.allow_self_management,
        id=__ret__.id,
        ssh_public_key=__ret__.ssh_public_key,
        ssh_username=__ret__.ssh_username)


@_utilities.lift_output_func(get_user_profile)
def get_user_profile_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserProfileResult]:
    """
    Resource Type definition for AWS::OpsWorks::UserProfile
    """
    ...
