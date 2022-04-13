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
    'GetAttestorResult',
    'AwaitableGetAttestorResult',
    'get_attestor',
    'get_attestor_output',
]

@pulumi.output_type
class GetAttestorResult:
    def __init__(__self__, description=None, etag=None, name=None, update_time=None, user_owned_grafeas_note=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if user_owned_grafeas_note and not isinstance(user_owned_grafeas_note, dict):
            raise TypeError("Expected argument 'user_owned_grafeas_note' to be a dict")
        pulumi.set(__self__, "user_owned_grafeas_note", user_owned_grafeas_note)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Optional. A checksum, returned by the server, that can be sent on update requests to ensure the attestor has an up-to-date value before attempting to update it. See https://google.aip.dev/154.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name, in the format: `projects/*/attestors/*`. This field may not be updated.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Time when the attestor was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="userOwnedGrafeasNote")
    def user_owned_grafeas_note(self) -> 'outputs.UserOwnedGrafeasNoteResponse':
        """
        This specifies how an attestation will be read, and how it will be used during policy enforcement.
        """
        return pulumi.get(self, "user_owned_grafeas_note")


class AwaitableGetAttestorResult(GetAttestorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAttestorResult(
            description=self.description,
            etag=self.etag,
            name=self.name,
            update_time=self.update_time,
            user_owned_grafeas_note=self.user_owned_grafeas_note)


def get_attestor(attestor_id: Optional[str] = None,
                 project: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAttestorResult:
    """
    Gets an attestor. Returns NOT_FOUND if the attestor does not exist.
    """
    __args__ = dict()
    __args__['attestorId'] = attestor_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:binaryauthorization/v1:getAttestor', __args__, opts=opts, typ=GetAttestorResult).value

    return AwaitableGetAttestorResult(
        description=__ret__.description,
        etag=__ret__.etag,
        name=__ret__.name,
        update_time=__ret__.update_time,
        user_owned_grafeas_note=__ret__.user_owned_grafeas_note)


@_utilities.lift_output_func(get_attestor)
def get_attestor_output(attestor_id: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAttestorResult]:
    """
    Gets an attestor. Returns NOT_FOUND if the attestor does not exist.
    """
    ...
