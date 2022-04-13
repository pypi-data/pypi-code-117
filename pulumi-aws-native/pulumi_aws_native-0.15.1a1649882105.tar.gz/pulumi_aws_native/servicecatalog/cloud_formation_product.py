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

__all__ = ['CloudFormationProductArgs', 'CloudFormationProduct']

@pulumi.input_type
class CloudFormationProductArgs:
    def __init__(__self__, *,
                 owner: pulumi.Input[str],
                 provisioning_artifact_parameters: pulumi.Input[Sequence[pulumi.Input['CloudFormationProductProvisioningArtifactPropertiesArgs']]],
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distributor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 replace_provisioning_artifacts: Optional[pulumi.Input[bool]] = None,
                 support_description: Optional[pulumi.Input[str]] = None,
                 support_email: Optional[pulumi.Input[str]] = None,
                 support_url: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CloudFormationProductTagArgs']]]] = None):
        """
        The set of arguments for constructing a CloudFormationProduct resource.
        """
        pulumi.set(__self__, "owner", owner)
        pulumi.set(__self__, "provisioning_artifact_parameters", provisioning_artifact_parameters)
        if accept_language is not None:
            pulumi.set(__self__, "accept_language", accept_language)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if distributor is not None:
            pulumi.set(__self__, "distributor", distributor)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if replace_provisioning_artifacts is not None:
            pulumi.set(__self__, "replace_provisioning_artifacts", replace_provisioning_artifacts)
        if support_description is not None:
            pulumi.set(__self__, "support_description", support_description)
        if support_email is not None:
            pulumi.set(__self__, "support_email", support_email)
        if support_url is not None:
            pulumi.set(__self__, "support_url", support_url)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Input[str]:
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: pulumi.Input[str]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter(name="provisioningArtifactParameters")
    def provisioning_artifact_parameters(self) -> pulumi.Input[Sequence[pulumi.Input['CloudFormationProductProvisioningArtifactPropertiesArgs']]]:
        return pulumi.get(self, "provisioning_artifact_parameters")

    @provisioning_artifact_parameters.setter
    def provisioning_artifact_parameters(self, value: pulumi.Input[Sequence[pulumi.Input['CloudFormationProductProvisioningArtifactPropertiesArgs']]]):
        pulumi.set(self, "provisioning_artifact_parameters", value)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "accept_language")

    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accept_language", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def distributor(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "distributor")

    @distributor.setter
    def distributor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "distributor", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="replaceProvisioningArtifacts")
    def replace_provisioning_artifacts(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "replace_provisioning_artifacts")

    @replace_provisioning_artifacts.setter
    def replace_provisioning_artifacts(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace_provisioning_artifacts", value)

    @property
    @pulumi.getter(name="supportDescription")
    def support_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "support_description")

    @support_description.setter
    def support_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "support_description", value)

    @property
    @pulumi.getter(name="supportEmail")
    def support_email(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "support_email")

    @support_email.setter
    def support_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "support_email", value)

    @property
    @pulumi.getter(name="supportUrl")
    def support_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "support_url")

    @support_url.setter
    def support_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "support_url", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CloudFormationProductTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CloudFormationProductTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""CloudFormationProduct is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class CloudFormationProduct(pulumi.CustomResource):
    warnings.warn("""CloudFormationProduct is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distributor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 provisioning_artifact_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudFormationProductProvisioningArtifactPropertiesArgs']]]]] = None,
                 replace_provisioning_artifacts: Optional[pulumi.Input[bool]] = None,
                 support_description: Optional[pulumi.Input[str]] = None,
                 support_email: Optional[pulumi.Input[str]] = None,
                 support_url: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudFormationProductTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ServiceCatalog::CloudFormationProduct

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudFormationProductArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ServiceCatalog::CloudFormationProduct

        :param str resource_name: The name of the resource.
        :param CloudFormationProductArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudFormationProductArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distributor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 provisioning_artifact_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudFormationProductProvisioningArtifactPropertiesArgs']]]]] = None,
                 replace_provisioning_artifacts: Optional[pulumi.Input[bool]] = None,
                 support_description: Optional[pulumi.Input[str]] = None,
                 support_email: Optional[pulumi.Input[str]] = None,
                 support_url: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudFormationProductTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""CloudFormationProduct is deprecated: CloudFormationProduct is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudFormationProductArgs.__new__(CloudFormationProductArgs)

            __props__.__dict__["accept_language"] = accept_language
            __props__.__dict__["description"] = description
            __props__.__dict__["distributor"] = distributor
            __props__.__dict__["name"] = name
            if owner is None and not opts.urn:
                raise TypeError("Missing required property 'owner'")
            __props__.__dict__["owner"] = owner
            if provisioning_artifact_parameters is None and not opts.urn:
                raise TypeError("Missing required property 'provisioning_artifact_parameters'")
            __props__.__dict__["provisioning_artifact_parameters"] = provisioning_artifact_parameters
            __props__.__dict__["replace_provisioning_artifacts"] = replace_provisioning_artifacts
            __props__.__dict__["support_description"] = support_description
            __props__.__dict__["support_email"] = support_email
            __props__.__dict__["support_url"] = support_url
            __props__.__dict__["tags"] = tags
            __props__.__dict__["product_name"] = None
            __props__.__dict__["provisioning_artifact_ids"] = None
            __props__.__dict__["provisioning_artifact_names"] = None
        super(CloudFormationProduct, __self__).__init__(
            'aws-native:servicecatalog:CloudFormationProduct',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CloudFormationProduct':
        """
        Get an existing CloudFormationProduct resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CloudFormationProductArgs.__new__(CloudFormationProductArgs)

        __props__.__dict__["accept_language"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["distributor"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner"] = None
        __props__.__dict__["product_name"] = None
        __props__.__dict__["provisioning_artifact_ids"] = None
        __props__.__dict__["provisioning_artifact_names"] = None
        __props__.__dict__["provisioning_artifact_parameters"] = None
        __props__.__dict__["replace_provisioning_artifacts"] = None
        __props__.__dict__["support_description"] = None
        __props__.__dict__["support_email"] = None
        __props__.__dict__["support_url"] = None
        __props__.__dict__["tags"] = None
        return CloudFormationProduct(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def distributor(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "distributor")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter(name="provisioningArtifactIds")
    def provisioning_artifact_ids(self) -> pulumi.Output[str]:
        return pulumi.get(self, "provisioning_artifact_ids")

    @property
    @pulumi.getter(name="provisioningArtifactNames")
    def provisioning_artifact_names(self) -> pulumi.Output[str]:
        return pulumi.get(self, "provisioning_artifact_names")

    @property
    @pulumi.getter(name="provisioningArtifactParameters")
    def provisioning_artifact_parameters(self) -> pulumi.Output[Sequence['outputs.CloudFormationProductProvisioningArtifactProperties']]:
        return pulumi.get(self, "provisioning_artifact_parameters")

    @property
    @pulumi.getter(name="replaceProvisioningArtifacts")
    def replace_provisioning_artifacts(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "replace_provisioning_artifacts")

    @property
    @pulumi.getter(name="supportDescription")
    def support_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "support_description")

    @property
    @pulumi.getter(name="supportEmail")
    def support_email(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "support_email")

    @property
    @pulumi.getter(name="supportUrl")
    def support_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "support_url")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CloudFormationProductTag']]]:
        return pulumi.get(self, "tags")

