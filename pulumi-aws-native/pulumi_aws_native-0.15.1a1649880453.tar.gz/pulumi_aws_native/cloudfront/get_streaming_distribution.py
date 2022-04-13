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
    'GetStreamingDistributionResult',
    'AwaitableGetStreamingDistributionResult',
    'get_streaming_distribution',
    'get_streaming_distribution_output',
]

@pulumi.output_type
class GetStreamingDistributionResult:
    def __init__(__self__, domain_name=None, id=None, streaming_distribution_config=None, tags=None):
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if streaming_distribution_config and not isinstance(streaming_distribution_config, dict):
            raise TypeError("Expected argument 'streaming_distribution_config' to be a dict")
        pulumi.set(__self__, "streaming_distribution_config", streaming_distribution_config)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="streamingDistributionConfig")
    def streaming_distribution_config(self) -> Optional['outputs.StreamingDistributionConfig']:
        return pulumi.get(self, "streaming_distribution_config")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.StreamingDistributionTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetStreamingDistributionResult(GetStreamingDistributionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamingDistributionResult(
            domain_name=self.domain_name,
            id=self.id,
            streaming_distribution_config=self.streaming_distribution_config,
            tags=self.tags)


def get_streaming_distribution(id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStreamingDistributionResult:
    """
    Resource Type definition for AWS::CloudFront::StreamingDistribution
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:cloudfront:getStreamingDistribution', __args__, opts=opts, typ=GetStreamingDistributionResult).value

    return AwaitableGetStreamingDistributionResult(
        domain_name=__ret__.domain_name,
        id=__ret__.id,
        streaming_distribution_config=__ret__.streaming_distribution_config,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_streaming_distribution)
def get_streaming_distribution_output(id: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStreamingDistributionResult]:
    """
    Resource Type definition for AWS::CloudFront::StreamingDistribution
    """
    ...
