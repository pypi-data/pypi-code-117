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
    'GetMulticastGroupResult',
    'AwaitableGetMulticastGroupResult',
    'get_multicast_group',
    'get_multicast_group_output',
]

@pulumi.output_type
class GetMulticastGroupResult:
    def __init__(__self__, arn=None, associate_wireless_device=None, description=None, disassociate_wireless_device=None, id=None, lo_ra_wan=None, name=None, status=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if associate_wireless_device and not isinstance(associate_wireless_device, str):
            raise TypeError("Expected argument 'associate_wireless_device' to be a str")
        pulumi.set(__self__, "associate_wireless_device", associate_wireless_device)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disassociate_wireless_device and not isinstance(disassociate_wireless_device, str):
            raise TypeError("Expected argument 'disassociate_wireless_device' to be a str")
        pulumi.set(__self__, "disassociate_wireless_device", disassociate_wireless_device)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lo_ra_wan and not isinstance(lo_ra_wan, dict):
            raise TypeError("Expected argument 'lo_ra_wan' to be a dict")
        pulumi.set(__self__, "lo_ra_wan", lo_ra_wan)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Multicast group arn. Returned after successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associateWirelessDevice")
    def associate_wireless_device(self) -> Optional[str]:
        """
        Wireless device to associate. Only for update request.
        """
        return pulumi.get(self, "associate_wireless_device")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Multicast group description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disassociateWirelessDevice")
    def disassociate_wireless_device(self) -> Optional[str]:
        """
        Wireless device to disassociate. Only for update request.
        """
        return pulumi.get(self, "disassociate_wireless_device")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Multicast group id. Returned after successful create.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="loRaWAN")
    def lo_ra_wan(self) -> Optional['outputs.MulticastGroupLoRaWAN']:
        """
        Multicast group LoRaWAN
        """
        return pulumi.get(self, "lo_ra_wan")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of Multicast group
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Multicast group status. Returned after successful read.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.MulticastGroupTag']]:
        """
        A list of key-value pairs that contain metadata for the Multicast group.
        """
        return pulumi.get(self, "tags")


class AwaitableGetMulticastGroupResult(GetMulticastGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMulticastGroupResult(
            arn=self.arn,
            associate_wireless_device=self.associate_wireless_device,
            description=self.description,
            disassociate_wireless_device=self.disassociate_wireless_device,
            id=self.id,
            lo_ra_wan=self.lo_ra_wan,
            name=self.name,
            status=self.status,
            tags=self.tags)


def get_multicast_group(id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMulticastGroupResult:
    """
    Create and manage Multicast groups.


    :param str id: Multicast group id. Returned after successful create.
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iotwireless:getMulticastGroup', __args__, opts=opts, typ=GetMulticastGroupResult).value

    return AwaitableGetMulticastGroupResult(
        arn=__ret__.arn,
        associate_wireless_device=__ret__.associate_wireless_device,
        description=__ret__.description,
        disassociate_wireless_device=__ret__.disassociate_wireless_device,
        id=__ret__.id,
        lo_ra_wan=__ret__.lo_ra_wan,
        name=__ret__.name,
        status=__ret__.status,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_multicast_group)
def get_multicast_group_output(id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMulticastGroupResult]:
    """
    Create and manage Multicast groups.


    :param str id: Multicast group id. Returned after successful create.
    """
    ...
