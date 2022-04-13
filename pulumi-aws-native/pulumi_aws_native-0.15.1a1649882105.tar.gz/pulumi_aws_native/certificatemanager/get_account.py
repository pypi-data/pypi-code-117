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
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
    'get_account_output',
]

@pulumi.output_type
class GetAccountResult:
    def __init__(__self__, account_id=None, expiry_events_configuration=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if expiry_events_configuration and not isinstance(expiry_events_configuration, dict):
            raise TypeError("Expected argument 'expiry_events_configuration' to be a dict")
        pulumi.set(__self__, "expiry_events_configuration", expiry_events_configuration)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="expiryEventsConfiguration")
    def expiry_events_configuration(self) -> Optional['outputs.AccountExpiryEventsConfiguration']:
        return pulumi.get(self, "expiry_events_configuration")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            account_id=self.account_id,
            expiry_events_configuration=self.expiry_events_configuration)


def get_account(account_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    Resource schema for AWS::CertificateManager::Account.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:certificatemanager:getAccount', __args__, opts=opts, typ=GetAccountResult).value

    return AwaitableGetAccountResult(
        account_id=__ret__.account_id,
        expiry_events_configuration=__ret__.expiry_events_configuration)


@_utilities.lift_output_func(get_account)
def get_account_output(account_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountResult]:
    """
    Resource schema for AWS::CertificateManager::Account.
    """
    ...
