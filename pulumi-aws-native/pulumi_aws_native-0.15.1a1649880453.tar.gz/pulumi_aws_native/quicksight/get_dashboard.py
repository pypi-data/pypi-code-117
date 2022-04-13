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
    'GetDashboardResult',
    'AwaitableGetDashboardResult',
    'get_dashboard',
    'get_dashboard_output',
]

@pulumi.output_type
class GetDashboardResult:
    def __init__(__self__, arn=None, last_published_time=None, name=None, permissions=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if last_published_time and not isinstance(last_published_time, str):
            raise TypeError("Expected argument 'last_published_time' to be a str")
        pulumi.set(__self__, "last_published_time", last_published_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        <p>The Amazon Resource Name (ARN) of the resource.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="lastPublishedTime")
    def last_published_time(self) -> Optional[str]:
        """
        <p>The last time that this dataset was published.</p>
        """
        return pulumi.get(self, "last_published_time")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        <p>The display name of the dashboard.</p>
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence['outputs.DashboardResourcePermission']]:
        """
        <p>A structure that contains the permissions of the dashboard. You can use this structure
                    for granting permissions by providing a list of IAM action information for each
                    principal ARN. </p>

                <p>To specify no permissions, omit the permissions list.</p>
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DashboardTag']]:
        """
        <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the
                    dashboard.</p>
        """
        return pulumi.get(self, "tags")


class AwaitableGetDashboardResult(GetDashboardResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDashboardResult(
            arn=self.arn,
            last_published_time=self.last_published_time,
            name=self.name,
            permissions=self.permissions,
            tags=self.tags)


def get_dashboard(aws_account_id: Optional[str] = None,
                  dashboard_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDashboardResult:
    """
    Definition of the AWS::QuickSight::Dashboard Resource Type.
    """
    __args__ = dict()
    __args__['awsAccountId'] = aws_account_id
    __args__['dashboardId'] = dashboard_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:quicksight:getDashboard', __args__, opts=opts, typ=GetDashboardResult).value

    return AwaitableGetDashboardResult(
        arn=__ret__.arn,
        last_published_time=__ret__.last_published_time,
        name=__ret__.name,
        permissions=__ret__.permissions,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_dashboard)
def get_dashboard_output(aws_account_id: Optional[pulumi.Input[str]] = None,
                         dashboard_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDashboardResult]:
    """
    Definition of the AWS::QuickSight::Dashboard Resource Type.
    """
    ...
