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

__all__ = ['LoadBalancerArgs', 'LoadBalancer']

@pulumi.input_type
class LoadBalancerArgs:
    def __init__(__self__, *,
                 listeners: pulumi.Input[Sequence[pulumi.Input['LoadBalancerListenersArgs']]],
                 access_logging_policy: Optional[pulumi.Input['LoadBalancerAccessLoggingPolicyArgs']] = None,
                 app_cookie_stickiness_policy: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerAppCookieStickinessPolicyArgs']]]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 connection_draining_policy: Optional[pulumi.Input['LoadBalancerConnectionDrainingPolicyArgs']] = None,
                 connection_settings: Optional[pulumi.Input['LoadBalancerConnectionSettingsArgs']] = None,
                 cross_zone: Optional[pulumi.Input[bool]] = None,
                 health_check: Optional[pulumi.Input['LoadBalancerHealthCheckArgs']] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 l_b_cookie_stickiness_policy: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerLBCookieStickinessPolicyArgs']]]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerPoliciesArgs']]]] = None,
                 scheme: Optional[pulumi.Input[str]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_security_group_group_name: Optional[pulumi.Input[str]] = None,
                 source_security_group_owner_alias: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerTagArgs']]]] = None):
        """
        The set of arguments for constructing a LoadBalancer resource.
        """
        pulumi.set(__self__, "listeners", listeners)
        if access_logging_policy is not None:
            pulumi.set(__self__, "access_logging_policy", access_logging_policy)
        if app_cookie_stickiness_policy is not None:
            pulumi.set(__self__, "app_cookie_stickiness_policy", app_cookie_stickiness_policy)
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if connection_draining_policy is not None:
            pulumi.set(__self__, "connection_draining_policy", connection_draining_policy)
        if connection_settings is not None:
            pulumi.set(__self__, "connection_settings", connection_settings)
        if cross_zone is not None:
            pulumi.set(__self__, "cross_zone", cross_zone)
        if health_check is not None:
            pulumi.set(__self__, "health_check", health_check)
        if instances is not None:
            pulumi.set(__self__, "instances", instances)
        if l_b_cookie_stickiness_policy is not None:
            pulumi.set(__self__, "l_b_cookie_stickiness_policy", l_b_cookie_stickiness_policy)
        if load_balancer_name is not None:
            pulumi.set(__self__, "load_balancer_name", load_balancer_name)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if scheme is not None:
            pulumi.set(__self__, "scheme", scheme)
        if security_groups is not None:
            pulumi.set(__self__, "security_groups", security_groups)
        if source_security_group_group_name is not None:
            pulumi.set(__self__, "source_security_group_group_name", source_security_group_group_name)
        if source_security_group_owner_alias is not None:
            pulumi.set(__self__, "source_security_group_owner_alias", source_security_group_owner_alias)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def listeners(self) -> pulumi.Input[Sequence[pulumi.Input['LoadBalancerListenersArgs']]]:
        return pulumi.get(self, "listeners")

    @listeners.setter
    def listeners(self, value: pulumi.Input[Sequence[pulumi.Input['LoadBalancerListenersArgs']]]):
        pulumi.set(self, "listeners", value)

    @property
    @pulumi.getter(name="accessLoggingPolicy")
    def access_logging_policy(self) -> Optional[pulumi.Input['LoadBalancerAccessLoggingPolicyArgs']]:
        return pulumi.get(self, "access_logging_policy")

    @access_logging_policy.setter
    def access_logging_policy(self, value: Optional[pulumi.Input['LoadBalancerAccessLoggingPolicyArgs']]):
        pulumi.set(self, "access_logging_policy", value)

    @property
    @pulumi.getter(name="appCookieStickinessPolicy")
    def app_cookie_stickiness_policy(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerAppCookieStickinessPolicyArgs']]]]:
        return pulumi.get(self, "app_cookie_stickiness_policy")

    @app_cookie_stickiness_policy.setter
    def app_cookie_stickiness_policy(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerAppCookieStickinessPolicyArgs']]]]):
        pulumi.set(self, "app_cookie_stickiness_policy", value)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "availability_zones")

    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "availability_zones", value)

    @property
    @pulumi.getter(name="connectionDrainingPolicy")
    def connection_draining_policy(self) -> Optional[pulumi.Input['LoadBalancerConnectionDrainingPolicyArgs']]:
        return pulumi.get(self, "connection_draining_policy")

    @connection_draining_policy.setter
    def connection_draining_policy(self, value: Optional[pulumi.Input['LoadBalancerConnectionDrainingPolicyArgs']]):
        pulumi.set(self, "connection_draining_policy", value)

    @property
    @pulumi.getter(name="connectionSettings")
    def connection_settings(self) -> Optional[pulumi.Input['LoadBalancerConnectionSettingsArgs']]:
        return pulumi.get(self, "connection_settings")

    @connection_settings.setter
    def connection_settings(self, value: Optional[pulumi.Input['LoadBalancerConnectionSettingsArgs']]):
        pulumi.set(self, "connection_settings", value)

    @property
    @pulumi.getter(name="crossZone")
    def cross_zone(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "cross_zone")

    @cross_zone.setter
    def cross_zone(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cross_zone", value)

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input['LoadBalancerHealthCheckArgs']]:
        return pulumi.get(self, "health_check")

    @health_check.setter
    def health_check(self, value: Optional[pulumi.Input['LoadBalancerHealthCheckArgs']]):
        pulumi.set(self, "health_check", value)

    @property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "instances", value)

    @property
    @pulumi.getter(name="lBCookieStickinessPolicy")
    def l_b_cookie_stickiness_policy(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerLBCookieStickinessPolicyArgs']]]]:
        return pulumi.get(self, "l_b_cookie_stickiness_policy")

    @l_b_cookie_stickiness_policy.setter
    def l_b_cookie_stickiness_policy(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerLBCookieStickinessPolicyArgs']]]]):
        pulumi.set(self, "l_b_cookie_stickiness_policy", value)

    @property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "load_balancer_name")

    @load_balancer_name.setter
    def load_balancer_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "load_balancer_name", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerPoliciesArgs']]]]:
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerPoliciesArgs']]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scheme")

    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheme", value)

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "security_groups")

    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_groups", value)

    @property
    @pulumi.getter(name="sourceSecurityGroupGroupName")
    def source_security_group_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_security_group_group_name")

    @source_security_group_group_name.setter
    def source_security_group_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_security_group_group_name", value)

    @property
    @pulumi.getter(name="sourceSecurityGroupOwnerAlias")
    def source_security_group_owner_alias(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_security_group_owner_alias")

    @source_security_group_owner_alias.setter
    def source_security_group_owner_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_security_group_owner_alias", value)

    @property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnets", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""LoadBalancer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class LoadBalancer(pulumi.CustomResource):
    warnings.warn("""LoadBalancer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_logging_policy: Optional[pulumi.Input[pulumi.InputType['LoadBalancerAccessLoggingPolicyArgs']]] = None,
                 app_cookie_stickiness_policy: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerAppCookieStickinessPolicyArgs']]]]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 connection_draining_policy: Optional[pulumi.Input[pulumi.InputType['LoadBalancerConnectionDrainingPolicyArgs']]] = None,
                 connection_settings: Optional[pulumi.Input[pulumi.InputType['LoadBalancerConnectionSettingsArgs']]] = None,
                 cross_zone: Optional[pulumi.Input[bool]] = None,
                 health_check: Optional[pulumi.Input[pulumi.InputType['LoadBalancerHealthCheckArgs']]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 l_b_cookie_stickiness_policy: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerLBCookieStickinessPolicyArgs']]]]] = None,
                 listeners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerListenersArgs']]]]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerPoliciesArgs']]]]] = None,
                 scheme: Optional[pulumi.Input[str]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_security_group_group_name: Optional[pulumi.Input[str]] = None,
                 source_security_group_owner_alias: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ElasticLoadBalancing::LoadBalancer

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LoadBalancerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ElasticLoadBalancing::LoadBalancer

        :param str resource_name: The name of the resource.
        :param LoadBalancerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LoadBalancerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_logging_policy: Optional[pulumi.Input[pulumi.InputType['LoadBalancerAccessLoggingPolicyArgs']]] = None,
                 app_cookie_stickiness_policy: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerAppCookieStickinessPolicyArgs']]]]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 connection_draining_policy: Optional[pulumi.Input[pulumi.InputType['LoadBalancerConnectionDrainingPolicyArgs']]] = None,
                 connection_settings: Optional[pulumi.Input[pulumi.InputType['LoadBalancerConnectionSettingsArgs']]] = None,
                 cross_zone: Optional[pulumi.Input[bool]] = None,
                 health_check: Optional[pulumi.Input[pulumi.InputType['LoadBalancerHealthCheckArgs']]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 l_b_cookie_stickiness_policy: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerLBCookieStickinessPolicyArgs']]]]] = None,
                 listeners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerListenersArgs']]]]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerPoliciesArgs']]]]] = None,
                 scheme: Optional[pulumi.Input[str]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_security_group_group_name: Optional[pulumi.Input[str]] = None,
                 source_security_group_owner_alias: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""LoadBalancer is deprecated: LoadBalancer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LoadBalancerArgs.__new__(LoadBalancerArgs)

            __props__.__dict__["access_logging_policy"] = access_logging_policy
            __props__.__dict__["app_cookie_stickiness_policy"] = app_cookie_stickiness_policy
            __props__.__dict__["availability_zones"] = availability_zones
            __props__.__dict__["connection_draining_policy"] = connection_draining_policy
            __props__.__dict__["connection_settings"] = connection_settings
            __props__.__dict__["cross_zone"] = cross_zone
            __props__.__dict__["health_check"] = health_check
            __props__.__dict__["instances"] = instances
            __props__.__dict__["l_b_cookie_stickiness_policy"] = l_b_cookie_stickiness_policy
            if listeners is None and not opts.urn:
                raise TypeError("Missing required property 'listeners'")
            __props__.__dict__["listeners"] = listeners
            __props__.__dict__["load_balancer_name"] = load_balancer_name
            __props__.__dict__["policies"] = policies
            __props__.__dict__["scheme"] = scheme
            __props__.__dict__["security_groups"] = security_groups
            __props__.__dict__["source_security_group_group_name"] = source_security_group_group_name
            __props__.__dict__["source_security_group_owner_alias"] = source_security_group_owner_alias
            __props__.__dict__["subnets"] = subnets
            __props__.__dict__["tags"] = tags
            __props__.__dict__["canonical_hosted_zone_name"] = None
            __props__.__dict__["canonical_hosted_zone_name_id"] = None
            __props__.__dict__["d_ns_name"] = None
        super(LoadBalancer, __self__).__init__(
            'aws-native:elasticloadbalancing:LoadBalancer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LoadBalancer':
        """
        Get an existing LoadBalancer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LoadBalancerArgs.__new__(LoadBalancerArgs)

        __props__.__dict__["access_logging_policy"] = None
        __props__.__dict__["app_cookie_stickiness_policy"] = None
        __props__.__dict__["availability_zones"] = None
        __props__.__dict__["canonical_hosted_zone_name"] = None
        __props__.__dict__["canonical_hosted_zone_name_id"] = None
        __props__.__dict__["connection_draining_policy"] = None
        __props__.__dict__["connection_settings"] = None
        __props__.__dict__["cross_zone"] = None
        __props__.__dict__["d_ns_name"] = None
        __props__.__dict__["health_check"] = None
        __props__.__dict__["instances"] = None
        __props__.__dict__["l_b_cookie_stickiness_policy"] = None
        __props__.__dict__["listeners"] = None
        __props__.__dict__["load_balancer_name"] = None
        __props__.__dict__["policies"] = None
        __props__.__dict__["scheme"] = None
        __props__.__dict__["security_groups"] = None
        __props__.__dict__["source_security_group_group_name"] = None
        __props__.__dict__["source_security_group_owner_alias"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["tags"] = None
        return LoadBalancer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessLoggingPolicy")
    def access_logging_policy(self) -> pulumi.Output[Optional['outputs.LoadBalancerAccessLoggingPolicy']]:
        return pulumi.get(self, "access_logging_policy")

    @property
    @pulumi.getter(name="appCookieStickinessPolicy")
    def app_cookie_stickiness_policy(self) -> pulumi.Output[Optional[Sequence['outputs.LoadBalancerAppCookieStickinessPolicy']]]:
        return pulumi.get(self, "app_cookie_stickiness_policy")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="canonicalHostedZoneName")
    def canonical_hosted_zone_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "canonical_hosted_zone_name")

    @property
    @pulumi.getter(name="canonicalHostedZoneNameID")
    def canonical_hosted_zone_name_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "canonical_hosted_zone_name_id")

    @property
    @pulumi.getter(name="connectionDrainingPolicy")
    def connection_draining_policy(self) -> pulumi.Output[Optional['outputs.LoadBalancerConnectionDrainingPolicy']]:
        return pulumi.get(self, "connection_draining_policy")

    @property
    @pulumi.getter(name="connectionSettings")
    def connection_settings(self) -> pulumi.Output[Optional['outputs.LoadBalancerConnectionSettings']]:
        return pulumi.get(self, "connection_settings")

    @property
    @pulumi.getter(name="crossZone")
    def cross_zone(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "cross_zone")

    @property
    @pulumi.getter(name="dNSName")
    def d_ns_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "d_ns_name")

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Output[Optional['outputs.LoadBalancerHealthCheck']]:
        return pulumi.get(self, "health_check")

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="lBCookieStickinessPolicy")
    def l_b_cookie_stickiness_policy(self) -> pulumi.Output[Optional[Sequence['outputs.LoadBalancerLBCookieStickinessPolicy']]]:
        return pulumi.get(self, "l_b_cookie_stickiness_policy")

    @property
    @pulumi.getter
    def listeners(self) -> pulumi.Output[Sequence['outputs.LoadBalancerListeners']]:
        return pulumi.get(self, "listeners")

    @property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "load_balancer_name")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Optional[Sequence['outputs.LoadBalancerPolicies']]]:
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter
    def scheme(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "scheme")

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "security_groups")

    @property
    @pulumi.getter(name="sourceSecurityGroupGroupName")
    def source_security_group_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source_security_group_group_name")

    @property
    @pulumi.getter(name="sourceSecurityGroupOwnerAlias")
    def source_security_group_owner_alias(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source_security_group_owner_alias")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.LoadBalancerTag']]]:
        return pulumi.get(self, "tags")

