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
    'GetSecurityPolicyResult',
    'AwaitableGetSecurityPolicyResult',
    'get_security_policy',
    'get_security_policy_output',
]

@pulumi.output_type
class GetSecurityPolicyResult:
    def __init__(__self__, adaptive_protection_config=None, advanced_options_config=None, associations=None, creation_timestamp=None, ddos_protection_config=None, description=None, display_name=None, fingerprint=None, kind=None, label_fingerprint=None, labels=None, name=None, parent=None, recaptcha_options_config=None, region=None, rule_tuple_count=None, rules=None, self_link=None, self_link_with_id=None, type=None):
        if adaptive_protection_config and not isinstance(adaptive_protection_config, dict):
            raise TypeError("Expected argument 'adaptive_protection_config' to be a dict")
        pulumi.set(__self__, "adaptive_protection_config", adaptive_protection_config)
        if advanced_options_config and not isinstance(advanced_options_config, dict):
            raise TypeError("Expected argument 'advanced_options_config' to be a dict")
        pulumi.set(__self__, "advanced_options_config", advanced_options_config)
        if associations and not isinstance(associations, list):
            raise TypeError("Expected argument 'associations' to be a list")
        pulumi.set(__self__, "associations", associations)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if ddos_protection_config and not isinstance(ddos_protection_config, dict):
            raise TypeError("Expected argument 'ddos_protection_config' to be a dict")
        pulumi.set(__self__, "ddos_protection_config", ddos_protection_config)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if label_fingerprint and not isinstance(label_fingerprint, str):
            raise TypeError("Expected argument 'label_fingerprint' to be a str")
        pulumi.set(__self__, "label_fingerprint", label_fingerprint)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parent and not isinstance(parent, str):
            raise TypeError("Expected argument 'parent' to be a str")
        pulumi.set(__self__, "parent", parent)
        if recaptcha_options_config and not isinstance(recaptcha_options_config, dict):
            raise TypeError("Expected argument 'recaptcha_options_config' to be a dict")
        pulumi.set(__self__, "recaptcha_options_config", recaptcha_options_config)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if rule_tuple_count and not isinstance(rule_tuple_count, int):
            raise TypeError("Expected argument 'rule_tuple_count' to be a int")
        pulumi.set(__self__, "rule_tuple_count", rule_tuple_count)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id and not isinstance(self_link_with_id, str):
            raise TypeError("Expected argument 'self_link_with_id' to be a str")
        pulumi.set(__self__, "self_link_with_id", self_link_with_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="adaptiveProtectionConfig")
    def adaptive_protection_config(self) -> 'outputs.SecurityPolicyAdaptiveProtectionConfigResponse':
        return pulumi.get(self, "adaptive_protection_config")

    @property
    @pulumi.getter(name="advancedOptionsConfig")
    def advanced_options_config(self) -> 'outputs.SecurityPolicyAdvancedOptionsConfigResponse':
        return pulumi.get(self, "advanced_options_config")

    @property
    @pulumi.getter
    def associations(self) -> Sequence['outputs.SecurityPolicyAssociationResponse']:
        """
        A list of associations that belong to this policy.
        """
        return pulumi.get(self, "associations")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter(name="ddosProtectionConfig")
    def ddos_protection_config(self) -> 'outputs.SecurityPolicyDdosProtectionConfigResponse':
        return pulumi.get(self, "ddos_protection_config")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        User-provided name of the Organization security plicy. The name should be unique in the organization in which the security policy is created. This should only be used when SecurityPolicyType is FIREWALL. The name must be 1-63 characters long, and comply with https://www.ietf.org/rfc/rfc1035.txt. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        """
        Specifies a fingerprint for this resource, which is essentially a hash of the metadata's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make get() request to the security policy.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        [Output only] Type of the resource. Always compute#securityPolicyfor security policies
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> str:
        """
        A fingerprint for the labels being applied to this security policy, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels. To see the latest fingerprint, make get() request to the security policy.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels for this resource. These can only be added or modified by the setLabels method. Each label key/value pair must comply with RFC1035. Label values may be empty.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> str:
        """
        The parent of the security policy.
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter(name="recaptchaOptionsConfig")
    def recaptcha_options_config(self) -> 'outputs.SecurityPolicyRecaptchaOptionsConfigResponse':
        return pulumi.get(self, "recaptcha_options_config")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        URL of the region where the regional security policy resides. This field is not applicable to global security policies.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> int:
        """
        Total count of all security policy rule tuples. A security policy can not exceed a set number of tuples.
        """
        return pulumi.get(self, "rule_tuple_count")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.SecurityPolicyRuleResponse']:
        """
        A list of rules that belong to this policy. There must always be a default rule (rule with priority 2147483647 and match "*"). If no rules are provided when creating a security policy, a default rule with action "allow" will be added.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> str:
        """
        Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type indicates the intended use of the security policy. - CLOUD_ARMOR: Cloud Armor backend security policies can be configured to filter incoming HTTP requests targeting backend services. They filter requests before they hit the origin servers. - CLOUD_ARMOR_EDGE: Cloud Armor edge security policies can be configured to filter incoming HTTP requests targeting backend services (including Cloud CDN-enabled) as well as backend buckets (Cloud Storage). They filter requests before the request is served from Google's cache. - CLOUD_ARMOR_INTERNAL_SERVICE: Cloud Armor internal service policies can be configured to filter HTTP requests targeting services managed by Traffic Director in a service mesh. They filter requests before the request is served from the application. This field can be set only at resource creation time.
        """
        return pulumi.get(self, "type")


class AwaitableGetSecurityPolicyResult(GetSecurityPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityPolicyResult(
            adaptive_protection_config=self.adaptive_protection_config,
            advanced_options_config=self.advanced_options_config,
            associations=self.associations,
            creation_timestamp=self.creation_timestamp,
            ddos_protection_config=self.ddos_protection_config,
            description=self.description,
            display_name=self.display_name,
            fingerprint=self.fingerprint,
            kind=self.kind,
            label_fingerprint=self.label_fingerprint,
            labels=self.labels,
            name=self.name,
            parent=self.parent,
            recaptcha_options_config=self.recaptcha_options_config,
            region=self.region,
            rule_tuple_count=self.rule_tuple_count,
            rules=self.rules,
            self_link=self.self_link,
            self_link_with_id=self.self_link_with_id,
            type=self.type)


def get_security_policy(project: Optional[str] = None,
                        security_policy: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityPolicyResult:
    """
    List all of the ordered rules present in a single specified policy.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['securityPolicy'] = security_policy
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/beta:getSecurityPolicy', __args__, opts=opts, typ=GetSecurityPolicyResult).value

    return AwaitableGetSecurityPolicyResult(
        adaptive_protection_config=__ret__.adaptive_protection_config,
        advanced_options_config=__ret__.advanced_options_config,
        associations=__ret__.associations,
        creation_timestamp=__ret__.creation_timestamp,
        ddos_protection_config=__ret__.ddos_protection_config,
        description=__ret__.description,
        display_name=__ret__.display_name,
        fingerprint=__ret__.fingerprint,
        kind=__ret__.kind,
        label_fingerprint=__ret__.label_fingerprint,
        labels=__ret__.labels,
        name=__ret__.name,
        parent=__ret__.parent,
        recaptcha_options_config=__ret__.recaptcha_options_config,
        region=__ret__.region,
        rule_tuple_count=__ret__.rule_tuple_count,
        rules=__ret__.rules,
        self_link=__ret__.self_link,
        self_link_with_id=__ret__.self_link_with_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_security_policy)
def get_security_policy_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                               security_policy: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityPolicyResult]:
    """
    List all of the ordered rules present in a single specified policy.
    """
    ...
