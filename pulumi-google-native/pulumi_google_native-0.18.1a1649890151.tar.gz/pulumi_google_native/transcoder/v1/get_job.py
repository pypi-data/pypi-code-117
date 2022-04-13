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
    'GetJobResult',
    'AwaitableGetJobResult',
    'get_job',
    'get_job_output',
]

@pulumi.output_type
class GetJobResult:
    def __init__(__self__, config=None, create_time=None, end_time=None, error=None, input_uri=None, name=None, output_uri=None, start_time=None, state=None, template_id=None, ttl_after_completion_days=None):
        if config and not isinstance(config, dict):
            raise TypeError("Expected argument 'config' to be a dict")
        pulumi.set(__self__, "config", config)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if input_uri and not isinstance(input_uri, str):
            raise TypeError("Expected argument 'input_uri' to be a str")
        pulumi.set(__self__, "input_uri", input_uri)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if output_uri and not isinstance(output_uri, str):
            raise TypeError("Expected argument 'output_uri' to be a str")
        pulumi.set(__self__, "output_uri", output_uri)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if template_id and not isinstance(template_id, str):
            raise TypeError("Expected argument 'template_id' to be a str")
        pulumi.set(__self__, "template_id", template_id)
        if ttl_after_completion_days and not isinstance(ttl_after_completion_days, int):
            raise TypeError("Expected argument 'ttl_after_completion_days' to be a int")
        pulumi.set(__self__, "ttl_after_completion_days", ttl_after_completion_days)

    @property
    @pulumi.getter
    def config(self) -> 'outputs.JobConfigResponse':
        """
        The configuration for this job.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time the job was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        The time the transcoding finished.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def error(self) -> 'outputs.StatusResponse':
        """
        An error object that describes the reason for the failure. This property is always present when `state` is `FAILED`.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter(name="inputUri")
    def input_uri(self) -> str:
        """
        Input only. Specify the `input_uri` to populate empty `uri` fields in each element of `Job.config.inputs` or `JobTemplate.config.inputs` when using template. URI of the media. Input files must be at least 5 seconds in duration and stored in Cloud Storage (for example, `gs://bucket/inputs/file.mp4`). See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).
        """
        return pulumi.get(self, "input_uri")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the job. Format: `projects/{project_number}/locations/{location}/jobs/{job}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputUri")
    def output_uri(self) -> str:
        """
        Input only. Specify the `output_uri` to populate an empty `Job.config.output.uri` or `JobTemplate.config.output.uri` when using template. URI for the output file(s). For example, `gs://my-bucket/outputs/`. See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).
        """
        return pulumi.get(self, "output_uri")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        The time the transcoding started.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the job.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> str:
        """
        Input only. Specify the `template_id` to use for populating `Job.config`. The default is `preset/web-hd`. Preset Transcoder templates: - `preset/{preset_id}` - User defined JobTemplate: `{job_template_id}`
        """
        return pulumi.get(self, "template_id")

    @property
    @pulumi.getter(name="ttlAfterCompletionDays")
    def ttl_after_completion_days(self) -> int:
        """
        Job time to live value in days, which will be effective after job completion. Job should be deleted automatically after the given TTL. Enter a value between 1 and 90. The default is 30.
        """
        return pulumi.get(self, "ttl_after_completion_days")


class AwaitableGetJobResult(GetJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobResult(
            config=self.config,
            create_time=self.create_time,
            end_time=self.end_time,
            error=self.error,
            input_uri=self.input_uri,
            name=self.name,
            output_uri=self.output_uri,
            start_time=self.start_time,
            state=self.state,
            template_id=self.template_id,
            ttl_after_completion_days=self.ttl_after_completion_days)


def get_job(job_id: Optional[str] = None,
            location: Optional[str] = None,
            project: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobResult:
    """
    Returns the job data.
    """
    __args__ = dict()
    __args__['jobId'] = job_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:transcoder/v1:getJob', __args__, opts=opts, typ=GetJobResult).value

    return AwaitableGetJobResult(
        config=__ret__.config,
        create_time=__ret__.create_time,
        end_time=__ret__.end_time,
        error=__ret__.error,
        input_uri=__ret__.input_uri,
        name=__ret__.name,
        output_uri=__ret__.output_uri,
        start_time=__ret__.start_time,
        state=__ret__.state,
        template_id=__ret__.template_id,
        ttl_after_completion_days=__ret__.ttl_after_completion_days)


@_utilities.lift_output_func(get_job)
def get_job_output(job_id: Optional[pulumi.Input[str]] = None,
                   location: Optional[pulumi.Input[str]] = None,
                   project: Optional[pulumi.Input[Optional[str]]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJobResult]:
    """
    Returns the job data.
    """
    ...
