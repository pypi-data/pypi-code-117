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
    'GetDBClusterResult',
    'AwaitableGetDBClusterResult',
    'get_db_cluster',
    'get_db_cluster_output',
]

@pulumi.output_type
class GetDBClusterResult:
    def __init__(__self__, associated_roles=None, backup_retention_period=None, cluster_resource_id=None, d_b_cluster_parameter_group_name=None, deletion_protection=None, enable_cloudwatch_logs_exports=None, endpoint=None, iam_auth_enabled=None, id=None, port=None, preferred_backup_window=None, preferred_maintenance_window=None, read_endpoint=None, tags=None, vpc_security_group_ids=None):
        if associated_roles and not isinstance(associated_roles, list):
            raise TypeError("Expected argument 'associated_roles' to be a list")
        pulumi.set(__self__, "associated_roles", associated_roles)
        if backup_retention_period and not isinstance(backup_retention_period, int):
            raise TypeError("Expected argument 'backup_retention_period' to be a int")
        pulumi.set(__self__, "backup_retention_period", backup_retention_period)
        if cluster_resource_id and not isinstance(cluster_resource_id, str):
            raise TypeError("Expected argument 'cluster_resource_id' to be a str")
        pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        if d_b_cluster_parameter_group_name and not isinstance(d_b_cluster_parameter_group_name, str):
            raise TypeError("Expected argument 'd_b_cluster_parameter_group_name' to be a str")
        pulumi.set(__self__, "d_b_cluster_parameter_group_name", d_b_cluster_parameter_group_name)
        if deletion_protection and not isinstance(deletion_protection, bool):
            raise TypeError("Expected argument 'deletion_protection' to be a bool")
        pulumi.set(__self__, "deletion_protection", deletion_protection)
        if enable_cloudwatch_logs_exports and not isinstance(enable_cloudwatch_logs_exports, list):
            raise TypeError("Expected argument 'enable_cloudwatch_logs_exports' to be a list")
        pulumi.set(__self__, "enable_cloudwatch_logs_exports", enable_cloudwatch_logs_exports)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if iam_auth_enabled and not isinstance(iam_auth_enabled, bool):
            raise TypeError("Expected argument 'iam_auth_enabled' to be a bool")
        pulumi.set(__self__, "iam_auth_enabled", iam_auth_enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if preferred_backup_window and not isinstance(preferred_backup_window, str):
            raise TypeError("Expected argument 'preferred_backup_window' to be a str")
        pulumi.set(__self__, "preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window and not isinstance(preferred_maintenance_window, str):
            raise TypeError("Expected argument 'preferred_maintenance_window' to be a str")
        pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if read_endpoint and not isinstance(read_endpoint, str):
            raise TypeError("Expected argument 'read_endpoint' to be a str")
        pulumi.set(__self__, "read_endpoint", read_endpoint)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpc_security_group_ids and not isinstance(vpc_security_group_ids, list):
            raise TypeError("Expected argument 'vpc_security_group_ids' to be a list")
        pulumi.set(__self__, "vpc_security_group_ids", vpc_security_group_ids)

    @property
    @pulumi.getter(name="associatedRoles")
    def associated_roles(self) -> Optional[Sequence['outputs.DBClusterRole']]:
        return pulumi.get(self, "associated_roles")

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[int]:
        return pulumi.get(self, "backup_retention_period")

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> Optional[str]:
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter(name="dBClusterParameterGroupName")
    def d_b_cluster_parameter_group_name(self) -> Optional[str]:
        return pulumi.get(self, "d_b_cluster_parameter_group_name")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[bool]:
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter(name="enableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "enable_cloudwatch_logs_exports")

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[str]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="iamAuthEnabled")
    def iam_auth_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "iam_auth_enabled")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[str]:
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[str]:
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="readEndpoint")
    def read_endpoint(self) -> Optional[str]:
        return pulumi.get(self, "read_endpoint")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DBClusterTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "vpc_security_group_ids")


class AwaitableGetDBClusterResult(GetDBClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDBClusterResult(
            associated_roles=self.associated_roles,
            backup_retention_period=self.backup_retention_period,
            cluster_resource_id=self.cluster_resource_id,
            d_b_cluster_parameter_group_name=self.d_b_cluster_parameter_group_name,
            deletion_protection=self.deletion_protection,
            enable_cloudwatch_logs_exports=self.enable_cloudwatch_logs_exports,
            endpoint=self.endpoint,
            iam_auth_enabled=self.iam_auth_enabled,
            id=self.id,
            port=self.port,
            preferred_backup_window=self.preferred_backup_window,
            preferred_maintenance_window=self.preferred_maintenance_window,
            read_endpoint=self.read_endpoint,
            tags=self.tags,
            vpc_security_group_ids=self.vpc_security_group_ids)


def get_db_cluster(id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDBClusterResult:
    """
    Resource Type definition for AWS::Neptune::DBCluster
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:neptune:getDBCluster', __args__, opts=opts, typ=GetDBClusterResult).value

    return AwaitableGetDBClusterResult(
        associated_roles=__ret__.associated_roles,
        backup_retention_period=__ret__.backup_retention_period,
        cluster_resource_id=__ret__.cluster_resource_id,
        d_b_cluster_parameter_group_name=__ret__.d_b_cluster_parameter_group_name,
        deletion_protection=__ret__.deletion_protection,
        enable_cloudwatch_logs_exports=__ret__.enable_cloudwatch_logs_exports,
        endpoint=__ret__.endpoint,
        iam_auth_enabled=__ret__.iam_auth_enabled,
        id=__ret__.id,
        port=__ret__.port,
        preferred_backup_window=__ret__.preferred_backup_window,
        preferred_maintenance_window=__ret__.preferred_maintenance_window,
        read_endpoint=__ret__.read_endpoint,
        tags=__ret__.tags,
        vpc_security_group_ids=__ret__.vpc_security_group_ids)


@_utilities.lift_output_func(get_db_cluster)
def get_db_cluster_output(id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDBClusterResult]:
    """
    Resource Type definition for AWS::Neptune::DBCluster
    """
    ...
