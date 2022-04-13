# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AggregationAuthorizationArgs', 'AggregationAuthorization']

@pulumi.input_type
class AggregationAuthorizationArgs:
    def __init__(__self__, *,
                 authorized_account_id: pulumi.Input[str],
                 authorized_aws_region: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AggregationAuthorizationTagArgs']]]] = None):
        """
        The set of arguments for constructing a AggregationAuthorization resource.
        :param pulumi.Input[str] authorized_account_id: The 12-digit account ID of the account authorized to aggregate data.
        :param pulumi.Input[str] authorized_aws_region: The region authorized to collect aggregated data.
        :param pulumi.Input[Sequence[pulumi.Input['AggregationAuthorizationTagArgs']]] tags: The tags for the AggregationAuthorization.
        """
        pulumi.set(__self__, "authorized_account_id", authorized_account_id)
        pulumi.set(__self__, "authorized_aws_region", authorized_aws_region)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="authorizedAccountId")
    def authorized_account_id(self) -> pulumi.Input[str]:
        """
        The 12-digit account ID of the account authorized to aggregate data.
        """
        return pulumi.get(self, "authorized_account_id")

    @authorized_account_id.setter
    def authorized_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "authorized_account_id", value)

    @property
    @pulumi.getter(name="authorizedAwsRegion")
    def authorized_aws_region(self) -> pulumi.Input[str]:
        """
        The region authorized to collect aggregated data.
        """
        return pulumi.get(self, "authorized_aws_region")

    @authorized_aws_region.setter
    def authorized_aws_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "authorized_aws_region", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AggregationAuthorizationTagArgs']]]]:
        """
        The tags for the AggregationAuthorization.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AggregationAuthorizationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class AggregationAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorized_account_id: Optional[pulumi.Input[str]] = None,
                 authorized_aws_region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AggregationAuthorizationTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Config::AggregationAuthorization

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorized_account_id: The 12-digit account ID of the account authorized to aggregate data.
        :param pulumi.Input[str] authorized_aws_region: The region authorized to collect aggregated data.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AggregationAuthorizationTagArgs']]]] tags: The tags for the AggregationAuthorization.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AggregationAuthorizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Config::AggregationAuthorization

        :param str resource_name: The name of the resource.
        :param AggregationAuthorizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AggregationAuthorizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorized_account_id: Optional[pulumi.Input[str]] = None,
                 authorized_aws_region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AggregationAuthorizationTagArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AggregationAuthorizationArgs.__new__(AggregationAuthorizationArgs)

            if authorized_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'authorized_account_id'")
            __props__.__dict__["authorized_account_id"] = authorized_account_id
            if authorized_aws_region is None and not opts.urn:
                raise TypeError("Missing required property 'authorized_aws_region'")
            __props__.__dict__["authorized_aws_region"] = authorized_aws_region
            __props__.__dict__["tags"] = tags
            __props__.__dict__["aggregation_authorization_arn"] = None
        super(AggregationAuthorization, __self__).__init__(
            'aws-native:configuration:AggregationAuthorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AggregationAuthorization':
        """
        Get an existing AggregationAuthorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AggregationAuthorizationArgs.__new__(AggregationAuthorizationArgs)

        __props__.__dict__["aggregation_authorization_arn"] = None
        __props__.__dict__["authorized_account_id"] = None
        __props__.__dict__["authorized_aws_region"] = None
        __props__.__dict__["tags"] = None
        return AggregationAuthorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aggregationAuthorizationArn")
    def aggregation_authorization_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the AggregationAuthorization.
        """
        return pulumi.get(self, "aggregation_authorization_arn")

    @property
    @pulumi.getter(name="authorizedAccountId")
    def authorized_account_id(self) -> pulumi.Output[str]:
        """
        The 12-digit account ID of the account authorized to aggregate data.
        """
        return pulumi.get(self, "authorized_account_id")

    @property
    @pulumi.getter(name="authorizedAwsRegion")
    def authorized_aws_region(self) -> pulumi.Output[str]:
        """
        The region authorized to collect aggregated data.
        """
        return pulumi.get(self, "authorized_aws_region")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AggregationAuthorizationTag']]]:
        """
        The tags for the AggregationAuthorization.
        """
        return pulumi.get(self, "tags")

