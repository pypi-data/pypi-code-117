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
    'GetSourceResult',
    'AwaitableGetSourceResult',
    'get_source',
    'get_source_output',
]

@pulumi.output_type
class GetSourceResult:
    def __init__(__self__, create_time=None, description=None, error=None, labels=None, name=None, update_time=None, vmware=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if vmware and not isinstance(vmware, dict):
            raise TypeError("Expected argument 'vmware' to be a dict")
        pulumi.set(__self__, "vmware", vmware)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The create time timestamp.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        User-provided description of the source.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def error(self) -> 'outputs.StatusResponse':
        """
        Provides details on the state of the Source in case of an error.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        The labels of the source.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The Source name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The update time timestamp.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def vmware(self) -> 'outputs.VmwareSourceDetailsResponse':
        """
        Vmware type source details.
        """
        return pulumi.get(self, "vmware")


class AwaitableGetSourceResult(GetSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSourceResult(
            create_time=self.create_time,
            description=self.description,
            error=self.error,
            labels=self.labels,
            name=self.name,
            update_time=self.update_time,
            vmware=self.vmware)


def get_source(location: Optional[str] = None,
               project: Optional[str] = None,
               source_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSourceResult:
    """
    Gets details of a single Source.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['sourceId'] = source_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:vmmigration/v1alpha1:getSource', __args__, opts=opts, typ=GetSourceResult).value

    return AwaitableGetSourceResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        error=__ret__.error,
        labels=__ret__.labels,
        name=__ret__.name,
        update_time=__ret__.update_time,
        vmware=__ret__.vmware)


@_utilities.lift_output_func(get_source)
def get_source_output(location: Optional[pulumi.Input[str]] = None,
                      project: Optional[pulumi.Input[Optional[str]]] = None,
                      source_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSourceResult]:
    """
    Gets details of a single Source.
    """
    ...
