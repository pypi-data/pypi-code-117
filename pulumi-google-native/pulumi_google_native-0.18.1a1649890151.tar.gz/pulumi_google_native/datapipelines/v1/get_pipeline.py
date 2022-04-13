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
    'GetPipelineResult',
    'AwaitableGetPipelineResult',
    'get_pipeline',
    'get_pipeline_output',
]

@pulumi.output_type
class GetPipelineResult:
    def __init__(__self__, create_time=None, display_name=None, job_count=None, last_update_time=None, name=None, pipeline_sources=None, schedule_info=None, scheduler_service_account_email=None, state=None, type=None, workload=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if job_count and not isinstance(job_count, int):
            raise TypeError("Expected argument 'job_count' to be a int")
        pulumi.set(__self__, "job_count", job_count)
        if last_update_time and not isinstance(last_update_time, str):
            raise TypeError("Expected argument 'last_update_time' to be a str")
        pulumi.set(__self__, "last_update_time", last_update_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pipeline_sources and not isinstance(pipeline_sources, dict):
            raise TypeError("Expected argument 'pipeline_sources' to be a dict")
        pulumi.set(__self__, "pipeline_sources", pipeline_sources)
        if schedule_info and not isinstance(schedule_info, dict):
            raise TypeError("Expected argument 'schedule_info' to be a dict")
        pulumi.set(__self__, "schedule_info", schedule_info)
        if scheduler_service_account_email and not isinstance(scheduler_service_account_email, str):
            raise TypeError("Expected argument 'scheduler_service_account_email' to be a str")
        pulumi.set(__self__, "scheduler_service_account_email", scheduler_service_account_email)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if workload and not isinstance(workload, dict):
            raise TypeError("Expected argument 'workload' to be a dict")
        pulumi.set(__self__, "workload", workload)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Immutable. The timestamp when the pipeline was initially created. Set by the Data Pipelines service.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the pipeline. It can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), and underscores (_).
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="jobCount")
    def job_count(self) -> int:
        """
        Number of jobs.
        """
        return pulumi.get(self, "job_count")

    @property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> str:
        """
        Immutable. The timestamp when the pipeline was last modified. Set by the Data Pipelines service.
        """
        return pulumi.get(self, "last_update_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The pipeline name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/pipelines/PIPELINE_ID`. * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), and periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). * `LOCATION_ID` is the canonical ID for the pipeline's location. The list of available locations can be obtained by calling `google.cloud.location.Locations.ListLocations`. Note that the Data Pipelines service is not available in all regions. It depends on Cloud Scheduler, an App Engine application, so it's only available in [App Engine regions](https://cloud.google.com/about/locations#region). * `PIPELINE_ID` is the ID of the pipeline. Must be unique for the selected project and location.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pipelineSources")
    def pipeline_sources(self) -> Mapping[str, str]:
        """
        Immutable. The sources of the pipeline (for example, Dataplex). The keys and values are set by the corresponding sources during pipeline creation.
        """
        return pulumi.get(self, "pipeline_sources")

    @property
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(self) -> 'outputs.GoogleCloudDatapipelinesV1ScheduleSpecResponse':
        """
        Internal scheduling information for a pipeline. If this information is provided, periodic jobs will be created per the schedule. If not, users are responsible for creating jobs externally.
        """
        return pulumi.get(self, "schedule_info")

    @property
    @pulumi.getter(name="schedulerServiceAccountEmail")
    def scheduler_service_account_email(self) -> str:
        """
        Optional. A service account email to be used with the Cloud Scheduler job. If not specified, the default compute engine service account will be used.
        """
        return pulumi.get(self, "scheduler_service_account_email")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the pipeline. When the pipeline is created, the state is set to 'PIPELINE_STATE_ACTIVE' by default. State changes can be requested by setting the state to stopping, paused, or resuming. State cannot be changed through UpdatePipeline requests.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the pipeline. This field affects the scheduling of the pipeline and the type of metrics to show for the pipeline.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def workload(self) -> 'outputs.GoogleCloudDatapipelinesV1WorkloadResponse':
        """
        Workload information for creating new jobs.
        """
        return pulumi.get(self, "workload")


class AwaitableGetPipelineResult(GetPipelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPipelineResult(
            create_time=self.create_time,
            display_name=self.display_name,
            job_count=self.job_count,
            last_update_time=self.last_update_time,
            name=self.name,
            pipeline_sources=self.pipeline_sources,
            schedule_info=self.schedule_info,
            scheduler_service_account_email=self.scheduler_service_account_email,
            state=self.state,
            type=self.type,
            workload=self.workload)


def get_pipeline(location: Optional[str] = None,
                 pipeline_id: Optional[str] = None,
                 project: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPipelineResult:
    """
    Looks up a single pipeline. Returns a "NOT_FOUND" error if no such pipeline exists. Returns a "FORBIDDEN" error if the caller doesn't have permission to access it.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['pipelineId'] = pipeline_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:datapipelines/v1:getPipeline', __args__, opts=opts, typ=GetPipelineResult).value

    return AwaitableGetPipelineResult(
        create_time=__ret__.create_time,
        display_name=__ret__.display_name,
        job_count=__ret__.job_count,
        last_update_time=__ret__.last_update_time,
        name=__ret__.name,
        pipeline_sources=__ret__.pipeline_sources,
        schedule_info=__ret__.schedule_info,
        scheduler_service_account_email=__ret__.scheduler_service_account_email,
        state=__ret__.state,
        type=__ret__.type,
        workload=__ret__.workload)


@_utilities.lift_output_func(get_pipeline)
def get_pipeline_output(location: Optional[pulumi.Input[str]] = None,
                        pipeline_id: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPipelineResult]:
    """
    Looks up a single pipeline. Returns a "NOT_FOUND" error if no such pipeline exists. Returns a "FORBIDDEN" error if the caller doesn't have permission to access it.
    """
    ...
