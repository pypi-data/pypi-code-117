# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAndroidAppResult',
    'AwaitableGetAndroidAppResult',
    'get_android_app',
    'get_android_app_output',
]

@pulumi.output_type
class GetAndroidAppResult:
    def __init__(__self__, api_key_id=None, app_id=None, display_name=None, name=None, package_name=None, project=None):
        if api_key_id and not isinstance(api_key_id, str):
            raise TypeError("Expected argument 'api_key_id' to be a str")
        pulumi.set(__self__, "api_key_id", api_key_id)
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if package_name and not isinstance(package_name, str):
            raise TypeError("Expected argument 'package_name' to be a str")
        pulumi.set(__self__, "package_name", package_name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> str:
        """
        The key_id of the GCP ApiKey associated with this App. If set must have no restrictions, or only have restrictions that are valid for the associated Firebase App. Cannot be set in create requests, instead an existing valid API Key will be chosen, or if no valid API Keys exist, one will be provisioned for you. Cannot be set to an empty value in update requests.
        """
        return pulumi.get(self, "api_key_id")

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> str:
        """
        Immutable. The globally unique, Firebase-assigned identifier for the `AndroidApp`. This identifier should be treated as an opaque token, as the data format is not specified.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-assigned display name for the `AndroidApp`.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the AndroidApp, in the format: projects/ PROJECT_IDENTIFIER/androidApps/APP_ID * PROJECT_IDENTIFIER: the parent Project's [`ProjectNumber`](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the `ProjectId`. * APP_ID: the globally unique, Firebase-assigned identifier for the App (see [`appId`](../projects.androidApps#AndroidApp.FIELDS.app_id)).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageName")
    def package_name(self) -> str:
        """
        Immutable. The canonical package name of the Android app as would appear in the Google Play Developer Console.
        """
        return pulumi.get(self, "package_name")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        Immutable. A user-assigned unique identifier of the parent FirebaseProject for the `AndroidApp`.
        """
        return pulumi.get(self, "project")


class AwaitableGetAndroidAppResult(GetAndroidAppResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAndroidAppResult(
            api_key_id=self.api_key_id,
            app_id=self.app_id,
            display_name=self.display_name,
            name=self.name,
            package_name=self.package_name,
            project=self.project)


def get_android_app(android_app_id: Optional[str] = None,
                    project: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAndroidAppResult:
    """
    Gets the specified AndroidApp.
    """
    __args__ = dict()
    __args__['androidAppId'] = android_app_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:firebase/v1beta1:getAndroidApp', __args__, opts=opts, typ=GetAndroidAppResult).value

    return AwaitableGetAndroidAppResult(
        api_key_id=__ret__.api_key_id,
        app_id=__ret__.app_id,
        display_name=__ret__.display_name,
        name=__ret__.name,
        package_name=__ret__.package_name,
        project=__ret__.project)


@_utilities.lift_output_func(get_android_app)
def get_android_app_output(android_app_id: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAndroidAppResult]:
    """
    Gets the specified AndroidApp.
    """
    ...
