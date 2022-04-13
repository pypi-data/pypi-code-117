# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetRegistryPolicyResult',
    'AwaitableGetRegistryPolicyResult',
    'get_registry_policy',
    'get_registry_policy_output',
]

@pulumi.output_type
class GetRegistryPolicyResult:
    def __init__(__self__, policy_text=None, registry_id=None):
        if policy_text and not isinstance(policy_text, dict):
            raise TypeError("Expected argument 'policy_text' to be a dict")
        pulumi.set(__self__, "policy_text", policy_text)
        if registry_id and not isinstance(registry_id, str):
            raise TypeError("Expected argument 'registry_id' to be a str")
        pulumi.set(__self__, "registry_id", registry_id)

    @property
    @pulumi.getter(name="policyText")
    def policy_text(self) -> Optional[Any]:
        """
        The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see Registry permissions (https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the Amazon Elastic Container Registry User Guide.
        """
        return pulumi.get(self, "policy_text")

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[str]:
        return pulumi.get(self, "registry_id")


class AwaitableGetRegistryPolicyResult(GetRegistryPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistryPolicyResult(
            policy_text=self.policy_text,
            registry_id=self.registry_id)


def get_registry_policy(registry_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistryPolicyResult:
    """
    The AWS::ECR::RegistryPolicy is used to specify permissions for another AWS account and is used when configuring cross-account replication. For more information, see Registry permissions in the Amazon Elastic Container Registry User Guide: https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html
    """
    __args__ = dict()
    __args__['registryId'] = registry_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ecr:getRegistryPolicy', __args__, opts=opts, typ=GetRegistryPolicyResult).value

    return AwaitableGetRegistryPolicyResult(
        policy_text=__ret__.policy_text,
        registry_id=__ret__.registry_id)


@_utilities.lift_output_func(get_registry_policy)
def get_registry_policy_output(registry_id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegistryPolicyResult]:
    """
    The AWS::ECR::RegistryPolicy is used to specify permissions for another AWS account and is used when configuring cross-account replication. For more information, see Registry permissions in the Amazon Elastic Container Registry User Guide: https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html
    """
    ...
