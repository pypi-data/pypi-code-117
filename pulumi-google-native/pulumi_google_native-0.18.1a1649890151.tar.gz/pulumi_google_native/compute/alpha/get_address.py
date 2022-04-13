# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAddressResult',
    'AwaitableGetAddressResult',
    'get_address',
    'get_address_output',
]

@pulumi.output_type
class GetAddressResult:
    def __init__(__self__, address=None, address_type=None, creation_timestamp=None, description=None, ip_version=None, ipv6_endpoint_type=None, kind=None, label_fingerprint=None, labels=None, name=None, network=None, network_tier=None, prefix_length=None, purpose=None, region=None, self_link=None, self_link_with_id=None, status=None, subnetwork=None, users=None):
        if address and not isinstance(address, str):
            raise TypeError("Expected argument 'address' to be a str")
        pulumi.set(__self__, "address", address)
        if address_type and not isinstance(address_type, str):
            raise TypeError("Expected argument 'address_type' to be a str")
        pulumi.set(__self__, "address_type", address_type)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if ip_version and not isinstance(ip_version, str):
            raise TypeError("Expected argument 'ip_version' to be a str")
        pulumi.set(__self__, "ip_version", ip_version)
        if ipv6_endpoint_type and not isinstance(ipv6_endpoint_type, str):
            raise TypeError("Expected argument 'ipv6_endpoint_type' to be a str")
        pulumi.set(__self__, "ipv6_endpoint_type", ipv6_endpoint_type)
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
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if network_tier and not isinstance(network_tier, str):
            raise TypeError("Expected argument 'network_tier' to be a str")
        pulumi.set(__self__, "network_tier", network_tier)
        if prefix_length and not isinstance(prefix_length, int):
            raise TypeError("Expected argument 'prefix_length' to be a int")
        pulumi.set(__self__, "prefix_length", prefix_length)
        if purpose and not isinstance(purpose, str):
            raise TypeError("Expected argument 'purpose' to be a str")
        pulumi.set(__self__, "purpose", purpose)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id and not isinstance(self_link_with_id, str):
            raise TypeError("Expected argument 'self_link_with_id' to be a str")
        pulumi.set(__self__, "self_link_with_id", self_link_with_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subnetwork and not isinstance(subnetwork, str):
            raise TypeError("Expected argument 'subnetwork' to be a str")
        pulumi.set(__self__, "subnetwork", subnetwork)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter
    def address(self) -> str:
        """
        The static IP address represented by this resource.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="addressType")
    def address_type(self) -> str:
        """
        The type of address to reserve, either INTERNAL or EXTERNAL. If unspecified, defaults to EXTERNAL.
        """
        return pulumi.get(self, "address_type")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of this resource. Provide this field when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> str:
        """
        The IP version that will be used by this address. Valid options are IPV4 or IPV6. This can only be specified for a global address.
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter(name="ipv6EndpointType")
    def ipv6_endpoint_type(self) -> str:
        """
        The endpoint type of this address, which should be VM. This is used for deciding which endpoint this address will be assigned to during the IPv6 external IP address reservation.
        """
        return pulumi.get(self, "ipv6_endpoint_type")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#address for addresses.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> str:
        """
        A fingerprint for the labels being applied to this Address, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve an Address.
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
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        The URL of the network in which to reserve the address. This field can only be used with INTERNAL type with the VPC_PEERING purpose.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> str:
        """
        This signifies the networking tier used for configuring this address and can only take the following values: PREMIUM or STANDARD. Internal IP addresses are always Premium Tier; global external IP addresses are always Premium Tier; regional external IP addresses can be either Standard or Premium Tier. If this field is not specified, it is assumed to be PREMIUM.
        """
        return pulumi.get(self, "network_tier")

    @property
    @pulumi.getter(name="prefixLength")
    def prefix_length(self) -> int:
        """
        The prefix length if the resource represents an IP range.
        """
        return pulumi.get(self, "prefix_length")

    @property
    @pulumi.getter
    def purpose(self) -> str:
        """
        The purpose of this resource, which can be one of the following values: - GCE_ENDPOINT for addresses that are used by VM instances, alias IP ranges, load balancers, and similar resources. - DNS_RESOLVER for a DNS resolver address in a subnetwork for a Cloud DNS inbound forwarder IP addresses (regional internal IP address in a subnet of a VPC network) - VPC_PEERING for global internal IP addresses used for private services access allocated ranges. - NAT_AUTO for the regional external IP addresses used by Cloud NAT when allocating addresses using automatic NAT IP address allocation. - IPSEC_INTERCONNECT for addresses created from a private IP range that are reserved for a VLAN attachment in an *IPsec-encrypted Cloud Interconnect* configuration. These addresses are regional resources. Not currently available publicly. - `SHARED_LOADBALANCER_VIP` for an internal IP address that is assigned to multiple internal forwarding rules. - `PRIVATE_SERVICE_CONNECT` for a private network address that is used to configure Private Service Connect. Only global internal addresses can use this purpose. 
        """
        return pulumi.get(self, "purpose")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The URL of the region where a regional address resides. For regional addresses, you must specify the region as a path parameter in the HTTP request URL. *This field is not applicable to global addresses.*
        """
        return pulumi.get(self, "region")

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
    def status(self) -> str:
        """
        The status of the address, which can be one of RESERVING, RESERVED, or IN_USE. An address that is RESERVING is currently in the process of being reserved. A RESERVED address is currently reserved and available to use. An IN_USE address is currently being used by another resource and is not available.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subnetwork(self) -> str:
        """
        The URL of the subnetwork in which to reserve the address. If an IP address is specified, it must be within the subnetwork's IP range. This field can only be used with INTERNAL type with a GCE_ENDPOINT or DNS_RESOLVER purpose.
        """
        return pulumi.get(self, "subnetwork")

    @property
    @pulumi.getter
    def users(self) -> Sequence[str]:
        """
        The URLs of the resources that are using this address.
        """
        return pulumi.get(self, "users")


class AwaitableGetAddressResult(GetAddressResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddressResult(
            address=self.address,
            address_type=self.address_type,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            ip_version=self.ip_version,
            ipv6_endpoint_type=self.ipv6_endpoint_type,
            kind=self.kind,
            label_fingerprint=self.label_fingerprint,
            labels=self.labels,
            name=self.name,
            network=self.network,
            network_tier=self.network_tier,
            prefix_length=self.prefix_length,
            purpose=self.purpose,
            region=self.region,
            self_link=self.self_link,
            self_link_with_id=self.self_link_with_id,
            status=self.status,
            subnetwork=self.subnetwork,
            users=self.users)


def get_address(address: Optional[str] = None,
                project: Optional[str] = None,
                region: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAddressResult:
    """
    Returns the specified address resource.
    """
    __args__ = dict()
    __args__['address'] = address
    __args__['project'] = project
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/alpha:getAddress', __args__, opts=opts, typ=GetAddressResult).value

    return AwaitableGetAddressResult(
        address=__ret__.address,
        address_type=__ret__.address_type,
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        ip_version=__ret__.ip_version,
        ipv6_endpoint_type=__ret__.ipv6_endpoint_type,
        kind=__ret__.kind,
        label_fingerprint=__ret__.label_fingerprint,
        labels=__ret__.labels,
        name=__ret__.name,
        network=__ret__.network,
        network_tier=__ret__.network_tier,
        prefix_length=__ret__.prefix_length,
        purpose=__ret__.purpose,
        region=__ret__.region,
        self_link=__ret__.self_link,
        self_link_with_id=__ret__.self_link_with_id,
        status=__ret__.status,
        subnetwork=__ret__.subnetwork,
        users=__ret__.users)


@_utilities.lift_output_func(get_address)
def get_address_output(address: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       region: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAddressResult]:
    """
    Returns the specified address resource.
    """
    ...
