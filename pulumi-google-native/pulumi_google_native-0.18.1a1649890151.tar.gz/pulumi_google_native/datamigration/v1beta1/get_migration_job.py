# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetMigrationJobResult',
    'AwaitableGetMigrationJobResult',
    'get_migration_job',
    'get_migration_job_output',
]

@pulumi.output_type
class GetMigrationJobResult:
    def __init__(__self__, create_time=None, destination=None, destination_database=None, display_name=None, dump_path=None, duration=None, end_time=None, error=None, labels=None, name=None, phase=None, reverse_ssh_connectivity=None, source=None, source_database=None, state=None, static_ip_connectivity=None, type=None, update_time=None, vpc_peering_connectivity=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if destination and not isinstance(destination, str):
            raise TypeError("Expected argument 'destination' to be a str")
        pulumi.set(__self__, "destination", destination)
        if destination_database and not isinstance(destination_database, dict):
            raise TypeError("Expected argument 'destination_database' to be a dict")
        pulumi.set(__self__, "destination_database", destination_database)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if dump_path and not isinstance(dump_path, str):
            raise TypeError("Expected argument 'dump_path' to be a str")
        pulumi.set(__self__, "dump_path", dump_path)
        if duration and not isinstance(duration, str):
            raise TypeError("Expected argument 'duration' to be a str")
        pulumi.set(__self__, "duration", duration)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if phase and not isinstance(phase, str):
            raise TypeError("Expected argument 'phase' to be a str")
        pulumi.set(__self__, "phase", phase)
        if reverse_ssh_connectivity and not isinstance(reverse_ssh_connectivity, dict):
            raise TypeError("Expected argument 'reverse_ssh_connectivity' to be a dict")
        pulumi.set(__self__, "reverse_ssh_connectivity", reverse_ssh_connectivity)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if source_database and not isinstance(source_database, dict):
            raise TypeError("Expected argument 'source_database' to be a dict")
        pulumi.set(__self__, "source_database", source_database)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if static_ip_connectivity and not isinstance(static_ip_connectivity, dict):
            raise TypeError("Expected argument 'static_ip_connectivity' to be a dict")
        pulumi.set(__self__, "static_ip_connectivity", static_ip_connectivity)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if vpc_peering_connectivity and not isinstance(vpc_peering_connectivity, dict):
            raise TypeError("Expected argument 'vpc_peering_connectivity' to be a dict")
        pulumi.set(__self__, "vpc_peering_connectivity", vpc_peering_connectivity)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The timestamp when the migration job resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def destination(self) -> str:
        """
        The resource name (URI) of the destination connection profile.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationDatabase")
    def destination_database(self) -> 'outputs.DatabaseTypeResponse':
        """
        The database engine type and provider of the destination.
        """
        return pulumi.get(self, "destination_database")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The migration job display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dumpPath")
    def dump_path(self) -> str:
        """
        The path to the dump file in Google Cloud Storage, in the format: (gs://[BUCKET_NAME]/[OBJECT_NAME]).
        """
        return pulumi.get(self, "dump_path")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        The duration of the migration job (in seconds). A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        If the migration job is completed, the time when it was completed.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def error(self) -> 'outputs.StatusResponse':
        """
        The error details in case of state FAILED.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        The resource labels for migration job to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name (URI) of this migration job resource, in the form of: projects/{project}/locations/{location}/migrationJobs/{migrationJob}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def phase(self) -> str:
        """
        The current migration job phase.
        """
        return pulumi.get(self, "phase")

    @property
    @pulumi.getter(name="reverseSshConnectivity")
    def reverse_ssh_connectivity(self) -> 'outputs.ReverseSshConnectivityResponse':
        """
        The details needed to communicate to the source over Reverse SSH tunnel connectivity.
        """
        return pulumi.get(self, "reverse_ssh_connectivity")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        The resource name (URI) of the source connection profile.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="sourceDatabase")
    def source_database(self) -> 'outputs.DatabaseTypeResponse':
        """
        The database engine type and provider of the source.
        """
        return pulumi.get(self, "source_database")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current migration job state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="staticIpConnectivity")
    def static_ip_connectivity(self) -> 'outputs.StaticIpConnectivityResponse':
        """
        static ip connectivity data (default, no additional details needed).
        """
        return pulumi.get(self, "static_ip_connectivity")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The migration job type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The timestamp when the migration job resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="vpcPeeringConnectivity")
    def vpc_peering_connectivity(self) -> 'outputs.VpcPeeringConnectivityResponse':
        """
        The details of the VPC network that the source database is located in.
        """
        return pulumi.get(self, "vpc_peering_connectivity")


class AwaitableGetMigrationJobResult(GetMigrationJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMigrationJobResult(
            create_time=self.create_time,
            destination=self.destination,
            destination_database=self.destination_database,
            display_name=self.display_name,
            dump_path=self.dump_path,
            duration=self.duration,
            end_time=self.end_time,
            error=self.error,
            labels=self.labels,
            name=self.name,
            phase=self.phase,
            reverse_ssh_connectivity=self.reverse_ssh_connectivity,
            source=self.source,
            source_database=self.source_database,
            state=self.state,
            static_ip_connectivity=self.static_ip_connectivity,
            type=self.type,
            update_time=self.update_time,
            vpc_peering_connectivity=self.vpc_peering_connectivity)


def get_migration_job(location: Optional[str] = None,
                      migration_job_id: Optional[str] = None,
                      project: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMigrationJobResult:
    """
    Gets details of a single migration job.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['migrationJobId'] = migration_job_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:datamigration/v1beta1:getMigrationJob', __args__, opts=opts, typ=GetMigrationJobResult).value

    return AwaitableGetMigrationJobResult(
        create_time=__ret__.create_time,
        destination=__ret__.destination,
        destination_database=__ret__.destination_database,
        display_name=__ret__.display_name,
        dump_path=__ret__.dump_path,
        duration=__ret__.duration,
        end_time=__ret__.end_time,
        error=__ret__.error,
        labels=__ret__.labels,
        name=__ret__.name,
        phase=__ret__.phase,
        reverse_ssh_connectivity=__ret__.reverse_ssh_connectivity,
        source=__ret__.source,
        source_database=__ret__.source_database,
        state=__ret__.state,
        static_ip_connectivity=__ret__.static_ip_connectivity,
        type=__ret__.type,
        update_time=__ret__.update_time,
        vpc_peering_connectivity=__ret__.vpc_peering_connectivity)


@_utilities.lift_output_func(get_migration_job)
def get_migration_job_output(location: Optional[pulumi.Input[str]] = None,
                             migration_job_id: Optional[pulumi.Input[str]] = None,
                             project: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMigrationJobResult]:
    """
    Gets details of a single migration job.
    """
    ...
