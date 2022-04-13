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

__all__ = ['ConfigRuleArgs', 'ConfigRule']

@pulumi.input_type
class ConfigRuleArgs:
    def __init__(__self__, *,
                 source: pulumi.Input['ConfigRuleSourceArgs'],
                 compliance_type: Optional[pulumi.Input[str]] = None,
                 config_rule_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 input_parameters: Optional[Any] = None,
                 maximum_execution_frequency: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input['ConfigRuleScopeArgs']] = None):
        """
        The set of arguments for constructing a ConfigRule resource.
        """
        pulumi.set(__self__, "source", source)
        if compliance_type is not None:
            pulumi.set(__self__, "compliance_type", compliance_type)
        if config_rule_name is not None:
            pulumi.set(__self__, "config_rule_name", config_rule_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if input_parameters is not None:
            pulumi.set(__self__, "input_parameters", input_parameters)
        if maximum_execution_frequency is not None:
            pulumi.set(__self__, "maximum_execution_frequency", maximum_execution_frequency)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input['ConfigRuleSourceArgs']:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input['ConfigRuleSourceArgs']):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="complianceType")
    def compliance_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "compliance_type")

    @compliance_type.setter
    def compliance_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compliance_type", value)

    @property
    @pulumi.getter(name="configRuleName")
    def config_rule_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "config_rule_name")

    @config_rule_name.setter
    def config_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_rule_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[Any]:
        return pulumi.get(self, "input_parameters")

    @input_parameters.setter
    def input_parameters(self, value: Optional[Any]):
        pulumi.set(self, "input_parameters", value)

    @property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "maximum_execution_frequency")

    @maximum_execution_frequency.setter
    def maximum_execution_frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "maximum_execution_frequency", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input['ConfigRuleScopeArgs']]:
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input['ConfigRuleScopeArgs']]):
        pulumi.set(self, "scope", value)


warnings.warn("""ConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ConfigRule(pulumi.CustomResource):
    warnings.warn("""ConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compliance_type: Optional[pulumi.Input[str]] = None,
                 config_rule_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 input_parameters: Optional[Any] = None,
                 maximum_execution_frequency: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['ConfigRuleScopeArgs']]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ConfigRuleSourceArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Config::ConfigRule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Config::ConfigRule

        :param str resource_name: The name of the resource.
        :param ConfigRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compliance_type: Optional[pulumi.Input[str]] = None,
                 config_rule_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 input_parameters: Optional[Any] = None,
                 maximum_execution_frequency: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['ConfigRuleScopeArgs']]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ConfigRuleSourceArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""ConfigRule is deprecated: ConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigRuleArgs.__new__(ConfigRuleArgs)

            __props__.__dict__["compliance_type"] = compliance_type
            __props__.__dict__["config_rule_name"] = config_rule_name
            __props__.__dict__["description"] = description
            __props__.__dict__["input_parameters"] = input_parameters
            __props__.__dict__["maximum_execution_frequency"] = maximum_execution_frequency
            __props__.__dict__["scope"] = scope
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["arn"] = None
            __props__.__dict__["config_rule_id"] = None
        super(ConfigRule, __self__).__init__(
            'aws-native:configuration:ConfigRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfigRule':
        """
        Get an existing ConfigRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigRuleArgs.__new__(ConfigRuleArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["compliance_type"] = None
        __props__.__dict__["config_rule_id"] = None
        __props__.__dict__["config_rule_name"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["input_parameters"] = None
        __props__.__dict__["maximum_execution_frequency"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["source"] = None
        return ConfigRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="complianceType")
    def compliance_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "compliance_type")

    @property
    @pulumi.getter(name="configRuleId")
    def config_rule_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "config_rule_id")

    @property
    @pulumi.getter(name="configRuleName")
    def config_rule_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "config_rule_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "input_parameters")

    @property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "maximum_execution_frequency")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional['outputs.ConfigRuleScope']]:
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output['outputs.ConfigRuleSource']:
        return pulumi.get(self, "source")

