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

__all__ = ['SnapshotArgs', 'Snapshot']

@pulumi.input_type
class SnapshotArgs:
    def __init__(__self__, *,
                 chain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location_hint: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 snapshot_encryption_key: Optional[pulumi.Input['CustomerEncryptionKeyArgs']] = None,
                 source_disk: Optional[pulumi.Input[str]] = None,
                 source_disk_encryption_key: Optional[pulumi.Input['CustomerEncryptionKeyArgs']] = None,
                 storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Snapshot resource.
        :param pulumi.Input[str] chain_name: Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
        :param pulumi.Input[str] location_hint: An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] request_id: An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        :param pulumi.Input['CustomerEncryptionKeyArgs'] snapshot_encryption_key: Encrypts the snapshot using a customer-supplied encryption key. After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request. Customer-supplied encryption keys do not protect access to metadata of the snapshot. If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
        :param pulumi.Input[str] source_disk: The source disk used to create this snapshot.
        :param pulumi.Input['CustomerEncryptionKeyArgs'] source_disk_encryption_key: The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_locations: Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
        """
        if chain_name is not None:
            pulumi.set(__self__, "chain_name", chain_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location_hint is not None:
            pulumi.set(__self__, "location_hint", location_hint)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if snapshot_encryption_key is not None:
            pulumi.set(__self__, "snapshot_encryption_key", snapshot_encryption_key)
        if source_disk is not None:
            pulumi.set(__self__, "source_disk", source_disk)
        if source_disk_encryption_key is not None:
            pulumi.set(__self__, "source_disk_encryption_key", source_disk_encryption_key)
        if storage_locations is not None:
            pulumi.set(__self__, "storage_locations", storage_locations)

    @property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
        """
        return pulumi.get(self, "chain_name")

    @chain_name.setter
    def chain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "chain_name", value)

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
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="locationHint")
    def location_hint(self) -> Optional[pulumi.Input[str]]:
        """
        An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
        """
        return pulumi.get(self, "location_hint")

    @location_hint.setter
    def location_hint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location_hint", value)

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
    @pulumi.getter(name="snapshotEncryptionKey")
    def snapshot_encryption_key(self) -> Optional[pulumi.Input['CustomerEncryptionKeyArgs']]:
        """
        Encrypts the snapshot using a customer-supplied encryption key. After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request. Customer-supplied encryption keys do not protect access to metadata of the snapshot. If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
        """
        return pulumi.get(self, "snapshot_encryption_key")

    @snapshot_encryption_key.setter
    def snapshot_encryption_key(self, value: Optional[pulumi.Input['CustomerEncryptionKeyArgs']]):
        pulumi.set(self, "snapshot_encryption_key", value)

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> Optional[pulumi.Input[str]]:
        """
        The source disk used to create this snapshot.
        """
        return pulumi.get(self, "source_disk")

    @source_disk.setter
    def source_disk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_disk", value)

    @property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(self) -> Optional[pulumi.Input['CustomerEncryptionKeyArgs']]:
        """
        The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
        """
        return pulumi.get(self, "source_disk_encryption_key")

    @source_disk_encryption_key.setter
    def source_disk_encryption_key(self, value: Optional[pulumi.Input['CustomerEncryptionKeyArgs']]):
        pulumi.set(self, "source_disk_encryption_key", value)

    @property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
        """
        return pulumi.get(self, "storage_locations")

    @storage_locations.setter
    def storage_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "storage_locations", value)


class Snapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 chain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location_hint: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 snapshot_encryption_key: Optional[pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']]] = None,
                 source_disk: Optional[pulumi.Input[str]] = None,
                 source_disk_encryption_key: Optional[pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']]] = None,
                 storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Creates a snapshot in the specified project using the data included in the request. For regular snapshot creation, consider using this method instead of disks.createSnapshot, as this method supports more features, such as creating snapshots in a project different from the source disk project.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] chain_name: Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
        :param pulumi.Input[str] location_hint: An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] request_id: An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']] snapshot_encryption_key: Encrypts the snapshot using a customer-supplied encryption key. After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request. Customer-supplied encryption keys do not protect access to metadata of the snapshot. If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
        :param pulumi.Input[str] source_disk: The source disk used to create this snapshot.
        :param pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']] source_disk_encryption_key: The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_locations: Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SnapshotArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a snapshot in the specified project using the data included in the request. For regular snapshot creation, consider using this method instead of disks.createSnapshot, as this method supports more features, such as creating snapshots in a project different from the source disk project.

        :param str resource_name: The name of the resource.
        :param SnapshotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SnapshotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 chain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location_hint: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 snapshot_encryption_key: Optional[pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']]] = None,
                 source_disk: Optional[pulumi.Input[str]] = None,
                 source_disk_encryption_key: Optional[pulumi.Input[pulumi.InputType['CustomerEncryptionKeyArgs']]] = None,
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
            __props__ = SnapshotArgs.__new__(SnapshotArgs)

            __props__.__dict__["chain_name"] = chain_name
            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location_hint"] = location_hint
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["snapshot_encryption_key"] = snapshot_encryption_key
            __props__.__dict__["source_disk"] = source_disk
            __props__.__dict__["source_disk_encryption_key"] = source_disk_encryption_key
            __props__.__dict__["storage_locations"] = storage_locations
            __props__.__dict__["auto_created"] = None
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["disk_size_gb"] = None
            __props__.__dict__["download_bytes"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["label_fingerprint"] = None
            __props__.__dict__["license_codes"] = None
            __props__.__dict__["licenses"] = None
            __props__.__dict__["satisfies_pzs"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["source_disk_id"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["storage_bytes"] = None
            __props__.__dict__["storage_bytes_status"] = None
        super(Snapshot, __self__).__init__(
            'google-native:compute/v1:Snapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Snapshot':
        """
        Get an existing Snapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SnapshotArgs.__new__(SnapshotArgs)

        __props__.__dict__["auto_created"] = None
        __props__.__dict__["chain_name"] = None
        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["disk_size_gb"] = None
        __props__.__dict__["download_bytes"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["label_fingerprint"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["license_codes"] = None
        __props__.__dict__["licenses"] = None
        __props__.__dict__["location_hint"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["satisfies_pzs"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["snapshot_encryption_key"] = None
        __props__.__dict__["source_disk"] = None
        __props__.__dict__["source_disk_encryption_key"] = None
        __props__.__dict__["source_disk_id"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["storage_bytes"] = None
        __props__.__dict__["storage_bytes_status"] = None
        __props__.__dict__["storage_locations"] = None
        return Snapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoCreated")
    def auto_created(self) -> pulumi.Output[bool]:
        """
        Set to true if snapshots are automatically created by applying resource policy on the target disk.
        """
        return pulumi.get(self, "auto_created")

    @property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> pulumi.Output[str]:
        """
        Creates the new snapshot in the snapshot chain labeled with the specified name. The chain name must be 1-63 characters long and comply with RFC1035. This is an uncommon option only for advanced service owners who needs to create separate snapshot chains, for example, for chargeback tracking. When you describe your snapshot resource, this field is visible only if it has a non-empty value.
        """
        return pulumi.get(self, "chain_name")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
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
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> pulumi.Output[str]:
        """
        Size of the source disk, specified in GB.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="downloadBytes")
    def download_bytes(self) -> pulumi.Output[str]:
        """
        Number of bytes downloaded to restore a snapshot to a disk.
        """
        return pulumi.get(self, "download_bytes")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Type of the resource. Always compute#snapshot for Snapshot resources.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[str]:
        """
        A fingerprint for the labels being applied to this snapshot, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a snapshot.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels to apply to this snapshot. These can be later modified by the setLabels method. Label values may be empty.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="licenseCodes")
    def license_codes(self) -> pulumi.Output[Sequence[str]]:
        """
        Integer license codes indicating which licenses are attached to this snapshot.
        """
        return pulumi.get(self, "license_codes")

    @property
    @pulumi.getter
    def licenses(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses attached (such as a Windows image).
        """
        return pulumi.get(self, "licenses")

    @property
    @pulumi.getter(name="locationHint")
    def location_hint(self) -> pulumi.Output[str]:
        """
        An opaque location hint used to place the snapshot close to other resources. This field is for use by internal tools that use the public API.
        """
        return pulumi.get(self, "location_hint")

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
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="snapshotEncryptionKey")
    def snapshot_encryption_key(self) -> pulumi.Output['outputs.CustomerEncryptionKeyResponse']:
        """
        Encrypts the snapshot using a customer-supplied encryption key. After you encrypt a snapshot using a customer-supplied key, you must provide the same key if you use the snapshot later. For example, you must provide the encryption key when you create a disk from the encrypted snapshot in a future request. Customer-supplied encryption keys do not protect access to metadata of the snapshot. If you do not provide an encryption key when creating the snapshot, then the snapshot will be encrypted using an automatically generated key and you do not need to provide a key to use the snapshot later.
        """
        return pulumi.get(self, "snapshot_encryption_key")

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> pulumi.Output[str]:
        """
        The source disk used to create this snapshot.
        """
        return pulumi.get(self, "source_disk")

    @property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(self) -> pulumi.Output['outputs.CustomerEncryptionKeyResponse']:
        """
        The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.
        """
        return pulumi.get(self, "source_disk_encryption_key")

    @property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> pulumi.Output[str]:
        """
        The ID value of the disk used to create this snapshot. This value may be used to determine whether the snapshot was taken from the current or a previous instance of a given disk name.
        """
        return pulumi.get(self, "source_disk_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the snapshot. This can be CREATING, DELETING, FAILED, READY, or UPLOADING.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageBytes")
    def storage_bytes(self) -> pulumi.Output[str]:
        """
        A size of the storage used by the snapshot. As snapshots share storage, this number is expected to change with snapshot creation/deletion.
        """
        return pulumi.get(self, "storage_bytes")

    @property
    @pulumi.getter(name="storageBytesStatus")
    def storage_bytes_status(self) -> pulumi.Output[str]:
        """
        An indicator whether storageBytes is in a stable state or it is being adjusted as a result of shared storage reallocation. This status can either be UPDATING, meaning the size of the snapshot is being updated, or UP_TO_DATE, meaning the size of the snapshot is up-to-date.
        """
        return pulumi.get(self, "storage_bytes_status")

    @property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> pulumi.Output[Sequence[str]]:
        """
        Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
        """
        return pulumi.get(self, "storage_locations")

