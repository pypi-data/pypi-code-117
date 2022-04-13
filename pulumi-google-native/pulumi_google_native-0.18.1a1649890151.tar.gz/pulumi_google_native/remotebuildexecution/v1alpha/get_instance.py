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
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(__self__, feature_policy=None, location=None, logging_enabled=None, name=None, state=None):
        if feature_policy and not isinstance(feature_policy, dict):
            raise TypeError("Expected argument 'feature_policy' to be a dict")
        pulumi.set(__self__, "feature_policy", feature_policy)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if logging_enabled and not isinstance(logging_enabled, bool):
            raise TypeError("Expected argument 'logging_enabled' to be a bool")
        pulumi.set(__self__, "logging_enabled", logging_enabled)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="featurePolicy")
    def feature_policy(self) -> 'outputs.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyResponse':
        """
        The policy to define whether or not RBE features can be used or how they can be used.
        """
        return pulumi.get(self, "feature_policy")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location is a GCP region. Currently only `us-central1` is supported.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="loggingEnabled")
    def logging_enabled(self) -> bool:
        """
        Whether stack driver logging is enabled for the instance.
        """
        return pulumi.get(self, "logging_enabled")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Instance resource name formatted as: `projects/[PROJECT_ID]/instances/[INSTANCE_ID]`. Name should not be populated when creating an instance since it is provided in the `instance_id` field.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the instance.
        """
        return pulumi.get(self, "state")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            feature_policy=self.feature_policy,
            location=self.location,
            logging_enabled=self.logging_enabled,
            name=self.name,
            state=self.state)


def get_instance(instance_id: Optional[str] = None,
                 project: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Returns the specified instance.
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:remotebuildexecution/v1alpha:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        feature_policy=__ret__.feature_policy,
        location=__ret__.location,
        logging_enabled=__ret__.logging_enabled,
        name=__ret__.name,
        state=__ret__.state)


@_utilities.lift_output_func(get_instance)
def get_instance_output(instance_id: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Returns the specified instance.
    """
    ...
