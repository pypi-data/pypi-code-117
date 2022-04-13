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
    'GetSamplingRuleResult',
    'AwaitableGetSamplingRuleResult',
    'get_sampling_rule',
    'get_sampling_rule_output',
]

@pulumi.output_type
class GetSamplingRuleResult:
    def __init__(__self__, rule_arn=None, rule_name=None, sampling_rule=None, sampling_rule_record=None, sampling_rule_update=None, tags=None):
        if rule_arn and not isinstance(rule_arn, str):
            raise TypeError("Expected argument 'rule_arn' to be a str")
        pulumi.set(__self__, "rule_arn", rule_arn)
        if rule_name and not isinstance(rule_name, str):
            raise TypeError("Expected argument 'rule_name' to be a str")
        pulumi.set(__self__, "rule_name", rule_name)
        if sampling_rule and not isinstance(sampling_rule, dict):
            raise TypeError("Expected argument 'sampling_rule' to be a dict")
        pulumi.set(__self__, "sampling_rule", sampling_rule)
        if sampling_rule_record and not isinstance(sampling_rule_record, dict):
            raise TypeError("Expected argument 'sampling_rule_record' to be a dict")
        pulumi.set(__self__, "sampling_rule_record", sampling_rule_record)
        if sampling_rule_update and not isinstance(sampling_rule_update, dict):
            raise TypeError("Expected argument 'sampling_rule_update' to be a dict")
        pulumi.set(__self__, "sampling_rule_update", sampling_rule_update)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="ruleARN")
    def rule_arn(self) -> Optional[str]:
        return pulumi.get(self, "rule_arn")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[str]:
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter(name="samplingRule")
    def sampling_rule(self) -> Optional['outputs.SamplingRule']:
        return pulumi.get(self, "sampling_rule")

    @property
    @pulumi.getter(name="samplingRuleRecord")
    def sampling_rule_record(self) -> Optional['outputs.SamplingRuleRecord']:
        return pulumi.get(self, "sampling_rule_record")

    @property
    @pulumi.getter(name="samplingRuleUpdate")
    def sampling_rule_update(self) -> Optional['outputs.SamplingRuleUpdate']:
        return pulumi.get(self, "sampling_rule_update")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TagsItemProperties']]:
        return pulumi.get(self, "tags")


class AwaitableGetSamplingRuleResult(GetSamplingRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSamplingRuleResult(
            rule_arn=self.rule_arn,
            rule_name=self.rule_name,
            sampling_rule=self.sampling_rule,
            sampling_rule_record=self.sampling_rule_record,
            sampling_rule_update=self.sampling_rule_update,
            tags=self.tags)


def get_sampling_rule(rule_arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSamplingRuleResult:
    """
    This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.
    """
    __args__ = dict()
    __args__['ruleARN'] = rule_arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:xray:getSamplingRule', __args__, opts=opts, typ=GetSamplingRuleResult).value

    return AwaitableGetSamplingRuleResult(
        rule_arn=__ret__.rule_arn,
        rule_name=__ret__.rule_name,
        sampling_rule=__ret__.sampling_rule,
        sampling_rule_record=__ret__.sampling_rule_record,
        sampling_rule_update=__ret__.sampling_rule_update,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_sampling_rule)
def get_sampling_rule_output(rule_arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSamplingRuleResult]:
    """
    This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.
    """
    ...
