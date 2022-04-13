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
    'GetNodegroupResult',
    'AwaitableGetNodegroupResult',
    'get_nodegroup',
    'get_nodegroup_output',
]

@pulumi.output_type
class GetNodegroupResult:
    def __init__(__self__, arn=None, id=None, labels=None, launch_template=None, release_version=None, scaling_config=None, tags=None, taints=None, update_config=None, version=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if launch_template and not isinstance(launch_template, dict):
            raise TypeError("Expected argument 'launch_template' to be a dict")
        pulumi.set(__self__, "launch_template", launch_template)
        if release_version and not isinstance(release_version, str):
            raise TypeError("Expected argument 'release_version' to be a str")
        pulumi.set(__self__, "release_version", release_version)
        if scaling_config and not isinstance(scaling_config, dict):
            raise TypeError("Expected argument 'scaling_config' to be a dict")
        pulumi.set(__self__, "scaling_config", scaling_config)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if taints and not isinstance(taints, list):
            raise TypeError("Expected argument 'taints' to be a list")
        pulumi.set(__self__, "taints", taints)
        if update_config and not isinstance(update_config, dict):
            raise TypeError("Expected argument 'update_config' to be a dict")
        pulumi.set(__self__, "update_config", update_config)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Any]:
        """
        The Kubernetes labels to be applied to the nodes in the node group when they are created.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> Optional['outputs.NodegroupLaunchTemplateSpecification']:
        """
        An object representing a node group's launch template specification.
        """
        return pulumi.get(self, "launch_template")

    @property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> Optional[str]:
        """
        The AMI version of the Amazon EKS-optimized AMI to use with your node group.
        """
        return pulumi.get(self, "release_version")

    @property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> Optional['outputs.NodegroupScalingConfig']:
        """
        The scaling configuration details for the Auto Scaling group that is created for your node group.
        """
        return pulumi.get(self, "scaling_config")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        The metadata, as key-value pairs, to apply to the node group to assist with categorization and organization. Follows same schema as Labels for consistency.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def taints(self) -> Optional[Sequence['outputs.NodegroupTaint']]:
        """
        The Kubernetes taints to be applied to the nodes in the node group when they are created.
        """
        return pulumi.get(self, "taints")

    @property
    @pulumi.getter(name="updateConfig")
    def update_config(self) -> Optional['outputs.NodegroupUpdateConfig']:
        """
        The node group update configuration.
        """
        return pulumi.get(self, "update_config")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The Kubernetes version to use for your managed nodes.
        """
        return pulumi.get(self, "version")


class AwaitableGetNodegroupResult(GetNodegroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNodegroupResult(
            arn=self.arn,
            id=self.id,
            labels=self.labels,
            launch_template=self.launch_template,
            release_version=self.release_version,
            scaling_config=self.scaling_config,
            tags=self.tags,
            taints=self.taints,
            update_config=self.update_config,
            version=self.version)


def get_nodegroup(id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNodegroupResult:
    """
    Resource schema for AWS::EKS::Nodegroup
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:eks:getNodegroup', __args__, opts=opts, typ=GetNodegroupResult).value

    return AwaitableGetNodegroupResult(
        arn=__ret__.arn,
        id=__ret__.id,
        labels=__ret__.labels,
        launch_template=__ret__.launch_template,
        release_version=__ret__.release_version,
        scaling_config=__ret__.scaling_config,
        tags=__ret__.tags,
        taints=__ret__.taints,
        update_config=__ret__.update_config,
        version=__ret__.version)


@_utilities.lift_output_func(get_nodegroup)
def get_nodegroup_output(id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNodegroupResult]:
    """
    Resource schema for AWS::EKS::Nodegroup
    """
    ...
