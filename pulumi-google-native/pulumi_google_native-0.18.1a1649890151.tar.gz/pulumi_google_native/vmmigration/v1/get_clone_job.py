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
    'GetCloneJobResult',
    'AwaitableGetCloneJobResult',
    'get_clone_job',
    'get_clone_job_output',
]

@pulumi.output_type
class GetCloneJobResult:
    def __init__(__self__, compute_engine_target_details=None, create_time=None, end_time=None, error=None, name=None, state=None, state_time=None):
        if compute_engine_target_details and not isinstance(compute_engine_target_details, dict):
            raise TypeError("Expected argument 'compute_engine_target_details' to be a dict")
        pulumi.set(__self__, "compute_engine_target_details", compute_engine_target_details)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_time and not isinstance(state_time, str):
            raise TypeError("Expected argument 'state_time' to be a str")
        pulumi.set(__self__, "state_time", state_time)

    @property
    @pulumi.getter(name="computeEngineTargetDetails")
    def compute_engine_target_details(self) -> 'outputs.ComputeEngineTargetDetailsResponse':
        """
        Details of the target VM in Compute Engine.
        """
        return pulumi.get(self, "compute_engine_target_details")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time the clone job was created (as an API call, not when it was actually created in the target).
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        The time the clone job was ended.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def error(self) -> 'outputs.StatusResponse':
        """
        Provides details for the errors that led to the Clone Job's state.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the clone.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the clone job.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateTime")
    def state_time(self) -> str:
        """
        The time the state was last updated.
        """
        return pulumi.get(self, "state_time")


class AwaitableGetCloneJobResult(GetCloneJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloneJobResult(
            compute_engine_target_details=self.compute_engine_target_details,
            create_time=self.create_time,
            end_time=self.end_time,
            error=self.error,
            name=self.name,
            state=self.state,
            state_time=self.state_time)


def get_clone_job(clone_job_id: Optional[str] = None,
                  location: Optional[str] = None,
                  migrating_vm_id: Optional[str] = None,
                  project: Optional[str] = None,
                  source_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloneJobResult:
    """
    Gets details of a single CloneJob.
    """
    __args__ = dict()
    __args__['cloneJobId'] = clone_job_id
    __args__['location'] = location
    __args__['migratingVmId'] = migrating_vm_id
    __args__['project'] = project
    __args__['sourceId'] = source_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:vmmigration/v1:getCloneJob', __args__, opts=opts, typ=GetCloneJobResult).value

    return AwaitableGetCloneJobResult(
        compute_engine_target_details=__ret__.compute_engine_target_details,
        create_time=__ret__.create_time,
        end_time=__ret__.end_time,
        error=__ret__.error,
        name=__ret__.name,
        state=__ret__.state,
        state_time=__ret__.state_time)


@_utilities.lift_output_func(get_clone_job)
def get_clone_job_output(clone_job_id: Optional[pulumi.Input[str]] = None,
                         location: Optional[pulumi.Input[str]] = None,
                         migrating_vm_id: Optional[pulumi.Input[str]] = None,
                         project: Optional[pulumi.Input[Optional[str]]] = None,
                         source_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloneJobResult]:
    """
    Gets details of a single CloneJob.
    """
    ...
