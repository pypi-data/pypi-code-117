# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['MachineImageArgs', 'MachineImage']

@pulumi.input_type
class MachineImageArgs:
    def __init__(__self__, *,
                 source_instance: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 guest_flush: Optional[pulumi.Input[bool]] = None,
                 machine_image_encryption_key: Optional[pulumi.Input['CustomerEncryptionKeyArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 saved_disks: Optional[pulumi.Input[Sequence[pulumi.Input['SavedDiskArgs']]]] = None,
                 source_disk_encryption_keys: Optional[pulumi.Input[Sequence[pulumi.Input['SourceDiskEncryptionKeyArgs']]]] = None,
                 storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MachineImage resource.
        :param pulumi.Input[str] source_instance: The source instance used to create the machine image. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance 
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[bool] guest_flush: [Input Only] Whether to attempt an application consistent machine image by informing the OS to prepare for the snapshot process.
        :param pulumi.Input['CustomerEncryptionKeyArgs'] machine_image_encryption_key: Encrypts the machine image using a customer-supplied encryption key. After you encrypt a machine image using a customer-supplied key, you must provide the same key if you use the machine image later. For example, you must provide the encryption key when you create an instance from the encrypted machine image in a future request. Customer-supplied encryption keys do not protect access to metadata of the machine image. If you do not provide an encryption key when creating the machine image, then the machine image will be encrypted using an automatically generated key and you do not need to provide a key to use the machine image later.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] request_id: An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[Sequence[pulumi.Input['SavedDiskArgs']]] saved_disks: An array of Machine Image specific properties for disks attached to the source instance
        :param pulumi.Input[Sequence[pulumi.Input['SourceDiskEncryptionKeyArgs']]] source_disk_encryption_keys: [Input Only] The customer-supplied encryption key of the disks attached to the source instance. Required if the source disk is protected by a customer-supplied encryption key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_locations: The regional or multi-regional Cloud Storage bucket location where the machine image is stored.
        """
        pulumi.set(__self__, "source_instance", source_instance)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if guest_flush is not None:
            pulumi.set(__self__, "guest_flush", guest_flush)
        if machine_image_encryption_key is not None:
            pulumi.set(__self__, "machine_image_encryption_key", machine_image_encryption_key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if saved_disks is not None:
            pulumi.set(__self__, "saved_disks", saved_disks)
        if source_disk_encryption_keys is not None:
            pulumi.set(__self__, "source_disk_encryption_keys", source_disk_encryption_keys)
        if storage_locations is not None:
            pulumi.set(__self__, "storage_locations", storage_locations)

    @property
    @pulumi.getter(name="sourceInstance")
    def source_instance(self) -> pulumi.Input[str]:
        """
        The source instance used to create the machine image. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance 
        """
        return pulumi.get(self, "source_instance")

    @source_instance.setter
    def source_instance(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_instance", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> Optional[pulumi.Input[bool]]:
        """
        [Input Only] Whether to attempt an application consistent machine image by informing the OS to prepare for the snapshot process.
        """
        return pulumi.get(self, "guest_flush")

    @guest_flush.setter
    def guest_flush(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "guest_flush", value)

    @property
    @pulumi.getter(name="machineImageEncryptionKey")
    def machine_image_encryption_key(self) -> Optional[pulumi.Input['CustomerEncryptionKeyArgs']]:
        """
        Encrypts the machine image using a customer-supplied encryption key. After you encrypt a machine image using a customer-supplied key, you must provide the same key if you use the machine image later. For example, you must provide the encryption key when you create an instance from the encrypted machine image in a future request. Customer-supplied encryption keys do not protect access to metadata of the machine image. If you do not provide an encryption key when creating the machine image, then the machine image will be encrypted using an automatically generated key and you do not need to provide a key to use the machine image later.
        """
        return pulumi.get(self, "machine_image_encryption_key")

    @machine_image_encryption_key.setter
    def machine_image_encryption_key(self, value: Optional[pulumi.Input['CustomerEncryptionKeyArgs']]):
        pulumi.set(self, "machine_image_encryption_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter(name="savedDisks")
    def saved_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SavedDiskArgs']]]]:
        """
        An array of Machine Image specific properties for disks attached to the source instance
        """
        return pulumi.get(self, "saved_disks")

    @saved_disks.setter
    def saved_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SavedDiskArgs']]]]):
        pulumi.set(self, "saved_disks", value)

    @property
    @pulumi.getter(name="sourceDiskEncryptionKeys")
    def source_disk_encryption_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SourceDiskEncryptionKeyArgs']]]]:
        """
        [Input Only] The customer-supplied encryption key of the disks attached to the source instance. Required if the source disk is protected by a customer-supplied encryption key.
        """
        return pulumi.get(self, "source_disk_encryption_keys")

    @source_disk_encryption_keys.setter
    def source_disk_encryption_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SourceDiskEncryptionKeyArgs']]]]):
        pulumi.set(self, "source_disk_encryption_keys", value)

    @property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The regional or multi-regional Cloud Storage bucket location where the machine image is stored.
        """
        return pulumi.get(self, "storage_locations")

    @storage_locations.setter
    def storage_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "storage_locations", value)


class MachineImage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 guest_flush: Optional[pulumi.Input[bool]] = None,
                 machine_image_encryption_key: Optional[pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 saved_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SavedDiskArgs']]]]] = None,
                 source_disk_encryption_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourceDiskEncryptionKeyArgs']]]]] = None,
                 source_instance: Optional[pulumi.Input[str]] = None,
                 storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Creates a machine image in the specified project using the data that is included in the request. If you are creating a new machine image to update an existing instance, your new machine image should use the same network or, if applicable, the same subnetwork as the original instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[bool] guest_flush: [Input Only] Whether to attempt an application consistent machine image by informing the OS to prepare for the snapshot process.
        :param pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']] machine_image_encryption_key: Encrypts the machine image using a customer-supplied encryption key. After you encrypt a machine image using a customer-supplied key, you must provide the same key if you use the machine image later. For example, you must provide the encryption key when you create an instance from the encrypted machine image in a future request. Customer-supplied encryption keys do not protect access to metadata of the machine image. If you do not provide an encryption key when creating the machine image, then the machine image will be encrypted using an automatically generated key and you do not need to provide a key to use the machine image later.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] request_id: An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SavedDiskArgs']]]] saved_disks: An array of Machine Image specific properties for disks attached to the source instance
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourceDiskEncryptionKeyArgs']]]] source_disk_encryption_keys: [Input Only] The customer-supplied encryption key of the disks attached to the source instance. Required if the source disk is protected by a customer-supplied encryption key.
        :param pulumi.Input[str] source_instance: The source instance used to create the machine image. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance 
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_locations: The regional or multi-regional Cloud Storage bucket location where the machine image is stored.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MachineImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a machine image in the specified project using the data that is included in the request. If you are creating a new machine image to update an existing instance, your new machine image should use the same network or, if applicable, the same subnetwork as the original instance.

        :param str resource_name: The name of the resource.
        :param MachineImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MachineImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 guest_flush: Optional[pulumi.Input[bool]] = None,
                 machine_image_encryption_key: Optional[pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 saved_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SavedDiskArgs']]]]] = None,
                 source_disk_encryption_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SourceDiskEncryptionKeyArgs']]]]] = None,
                 source_instance: Optional[pulumi.Input[str]] = None,
                 storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = MachineImageArgs.__new__(MachineImageArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["guest_flush"] = guest_flush
            __props__.__dict__["machine_image_encryption_key"] = machine_image_encryption_key
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["saved_disks"] = saved_disks
            __props__.__dict__["source_disk_encryption_keys"] = source_disk_encryption_keys
            if source_instance is None and not opts.urn:
                raise TypeError("Missing required property 'source_instance'")
            __props__.__dict__["source_instance"] = source_instance
            __props__.__dict__["storage_locations"] = storage_locations
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["instance_properties"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["satisfies_pzs"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["source_instance_properties"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["total_storage_bytes"] = None
        super(MachineImage, __self__).__init__(
            'google-native:compute/beta:MachineImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MachineImage':
        """
        Get an existing MachineImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MachineImageArgs.__new__(MachineImageArgs)

        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["guest_flush"] = None
        __props__.__dict__["instance_properties"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["machine_image_encryption_key"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["satisfies_pzs"] = None
        __props__.__dict__["saved_disks"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["source_disk_encryption_keys"] = None
        __props__.__dict__["source_instance"] = None
        __props__.__dict__["source_instance_properties"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["storage_locations"] = None
        __props__.__dict__["total_storage_bytes"] = None
        return MachineImage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        The creation timestamp for this machine image in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> pulumi.Output[bool]:
        """
        [Input Only] Whether to attempt an application consistent machine image by informing the OS to prepare for the snapshot process.
        """
        return pulumi.get(self, "guest_flush")

    @property
    @pulumi.getter(name="instanceProperties")
    def instance_properties(self) -> pulumi.Output['outputs.InstancePropertiesResponse']:
        """
        Properties of source instance
        """
        return pulumi.get(self, "instance_properties")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The resource type, which is always compute#machineImage for machine image.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="machineImageEncryptionKey")
    def machine_image_encryption_key(self) -> pulumi.Output['outputs.CustomerEncryptionKeyResponse']:
        """
        Encrypts the machine image using a customer-supplied encryption key. After you encrypt a machine image using a customer-supplied key, you must provide the same key if you use the machine image later. For example, you must provide the encryption key when you create an instance from the encrypted machine image in a future request. Customer-supplied encryption keys do not protect access to metadata of the machine image. If you do not provide an encryption key when creating the machine image, then the machine image will be encrypted using an automatically generated key and you do not need to provide a key to use the machine image later.
        """
        return pulumi.get(self, "machine_image_encryption_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> pulumi.Output[bool]:
        """
        Reserved for future use.
        """
        return pulumi.get(self, "satisfies_pzs")

    @property
    @pulumi.getter(name="savedDisks")
    def saved_disks(self) -> pulumi.Output[Sequence['outputs.SavedDiskResponse']]:
        """
        An array of Machine Image specific properties for disks attached to the source instance
        """
        return pulumi.get(self, "saved_disks")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URL for this machine image. The server defines this URL.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sourceDiskEncryptionKeys")
    def source_disk_encryption_keys(self) -> pulumi.Output[Sequence['outputs.SourceDiskEncryptionKeyResponse']]:
        """
        [Input Only] The customer-supplied encryption key of the disks attached to the source instance. Required if the source disk is protected by a customer-supplied encryption key.
        """
        return pulumi.get(self, "source_disk_encryption_keys")

    @property
    @pulumi.getter(name="sourceInstance")
    def source_instance(self) -> pulumi.Output[str]:
        """
        The source instance used to create the machine image. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance 
        """
        return pulumi.get(self, "source_instance")

    @property
    @pulumi.getter(name="sourceInstanceProperties")
    def source_instance_properties(self) -> pulumi.Output['outputs.SourceInstancePropertiesResponse']:
        """
        DEPRECATED: Please use instance_properties instead for source instance related properties. New properties will not be added to this field.
        """
        return pulumi.get(self, "source_instance_properties")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the machine image. One of the following values: INVALID, CREATING, READY, DELETING, and UPLOADING.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> pulumi.Output[Sequence[str]]:
        """
        The regional or multi-regional Cloud Storage bucket location where the machine image is stored.
        """
        return pulumi.get(self, "storage_locations")

    @property
    @pulumi.getter(name="totalStorageBytes")
    def total_storage_bytes(self) -> pulumi.Output[str]:
        """
        Total size of the storage used by the machine image.
        """
        return pulumi.get(self, "total_storage_bytes")

