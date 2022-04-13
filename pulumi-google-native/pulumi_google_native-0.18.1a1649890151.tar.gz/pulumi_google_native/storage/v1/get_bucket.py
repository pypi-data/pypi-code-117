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
    'GetBucketResult',
    'AwaitableGetBucketResult',
    'get_bucket',
    'get_bucket_output',
]

@pulumi.output_type
class GetBucketResult:
    def __init__(__self__, acl=None, autoclass=None, billing=None, cors=None, default_event_based_hold=None, default_object_acl=None, encryption=None, etag=None, iam_configuration=None, kind=None, labels=None, lifecycle=None, location=None, location_type=None, logging=None, metageneration=None, name=None, owner=None, project_number=None, retention_policy=None, rpo=None, satisfies_pzs=None, self_link=None, storage_class=None, time_created=None, updated=None, versioning=None, website=None):
        if acl and not isinstance(acl, list):
            raise TypeError("Expected argument 'acl' to be a list")
        pulumi.set(__self__, "acl", acl)
        if autoclass and not isinstance(autoclass, dict):
            raise TypeError("Expected argument 'autoclass' to be a dict")
        pulumi.set(__self__, "autoclass", autoclass)
        if billing and not isinstance(billing, dict):
            raise TypeError("Expected argument 'billing' to be a dict")
        pulumi.set(__self__, "billing", billing)
        if cors and not isinstance(cors, list):
            raise TypeError("Expected argument 'cors' to be a list")
        pulumi.set(__self__, "cors", cors)
        if default_event_based_hold and not isinstance(default_event_based_hold, bool):
            raise TypeError("Expected argument 'default_event_based_hold' to be a bool")
        pulumi.set(__self__, "default_event_based_hold", default_event_based_hold)
        if default_object_acl and not isinstance(default_object_acl, list):
            raise TypeError("Expected argument 'default_object_acl' to be a list")
        pulumi.set(__self__, "default_object_acl", default_object_acl)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if iam_configuration and not isinstance(iam_configuration, dict):
            raise TypeError("Expected argument 'iam_configuration' to be a dict")
        pulumi.set(__self__, "iam_configuration", iam_configuration)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if lifecycle and not isinstance(lifecycle, dict):
            raise TypeError("Expected argument 'lifecycle' to be a dict")
        pulumi.set(__self__, "lifecycle", lifecycle)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if location_type and not isinstance(location_type, str):
            raise TypeError("Expected argument 'location_type' to be a str")
        pulumi.set(__self__, "location_type", location_type)
        if logging and not isinstance(logging, dict):
            raise TypeError("Expected argument 'logging' to be a dict")
        pulumi.set(__self__, "logging", logging)
        if metageneration and not isinstance(metageneration, str):
            raise TypeError("Expected argument 'metageneration' to be a str")
        pulumi.set(__self__, "metageneration", metageneration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner and not isinstance(owner, dict):
            raise TypeError("Expected argument 'owner' to be a dict")
        pulumi.set(__self__, "owner", owner)
        if project_number and not isinstance(project_number, str):
            raise TypeError("Expected argument 'project_number' to be a str")
        pulumi.set(__self__, "project_number", project_number)
        if retention_policy and not isinstance(retention_policy, dict):
            raise TypeError("Expected argument 'retention_policy' to be a dict")
        pulumi.set(__self__, "retention_policy", retention_policy)
        if rpo and not isinstance(rpo, str):
            raise TypeError("Expected argument 'rpo' to be a str")
        pulumi.set(__self__, "rpo", rpo)
        if satisfies_pzs and not isinstance(satisfies_pzs, bool):
            raise TypeError("Expected argument 'satisfies_pzs' to be a bool")
        pulumi.set(__self__, "satisfies_pzs", satisfies_pzs)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if storage_class and not isinstance(storage_class, str):
            raise TypeError("Expected argument 'storage_class' to be a str")
        pulumi.set(__self__, "storage_class", storage_class)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)
        if versioning and not isinstance(versioning, dict):
            raise TypeError("Expected argument 'versioning' to be a dict")
        pulumi.set(__self__, "versioning", versioning)
        if website and not isinstance(website, dict):
            raise TypeError("Expected argument 'website' to be a dict")
        pulumi.set(__self__, "website", website)

    @property
    @pulumi.getter
    def acl(self) -> Sequence['outputs.BucketAccessControlResponse']:
        """
        Access controls on the bucket.
        """
        return pulumi.get(self, "acl")

    @property
    @pulumi.getter
    def autoclass(self) -> 'outputs.BucketAutoclassResponse':
        """
        The bucket's Autoclass configuration.
        """
        return pulumi.get(self, "autoclass")

    @property
    @pulumi.getter
    def billing(self) -> 'outputs.BucketBillingResponse':
        """
        The bucket's billing configuration.
        """
        return pulumi.get(self, "billing")

    @property
    @pulumi.getter
    def cors(self) -> Sequence['outputs.BucketCorsItemResponse']:
        """
        The bucket's Cross-Origin Resource Sharing (CORS) configuration.
        """
        return pulumi.get(self, "cors")

    @property
    @pulumi.getter(name="defaultEventBasedHold")
    def default_event_based_hold(self) -> bool:
        """
        The default value for event-based hold on newly created objects in this bucket. Event-based hold is a way to retain objects indefinitely until an event occurs, signified by the hold's release. After being released, such objects will be subject to bucket-level retention (if any). One sample use case of this flag is for banks to hold loan documents for at least 3 years after loan is paid in full. Here, bucket-level retention is 3 years and the event is loan being paid in full. In this example, these objects will be held intact for any number of years until the event has occurred (event-based hold on the object is released) and then 3 more years after that. That means retention duration of the objects begins from the moment event-based hold transitioned from true to false. Objects under event-based hold cannot be deleted, overwritten or archived until the hold is removed.
        """
        return pulumi.get(self, "default_event_based_hold")

    @property
    @pulumi.getter(name="defaultObjectAcl")
    def default_object_acl(self) -> Sequence['outputs.ObjectAccessControlResponse']:
        """
        Default access controls to apply to new objects when no ACL is provided.
        """
        return pulumi.get(self, "default_object_acl")

    @property
    @pulumi.getter
    def encryption(self) -> 'outputs.BucketEncryptionResponse':
        """
        Encryption configuration for a bucket.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        HTTP 1.1 Entity tag for the bucket.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="iamConfiguration")
    def iam_configuration(self) -> 'outputs.BucketIamConfigurationResponse':
        """
        The bucket's IAM configuration.
        """
        return pulumi.get(self, "iam_configuration")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of item this is. For buckets, this is always storage#bucket.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        User-provided labels, in key/value pairs.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def lifecycle(self) -> 'outputs.BucketLifecycleResponse':
        """
        The bucket's lifecycle configuration. See lifecycle management for more information.
        """
        return pulumi.get(self, "lifecycle")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the bucket. Object data for objects in the bucket resides in physical storage within this region. Defaults to US. See the developer's guide for the authoritative list.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="locationType")
    def location_type(self) -> str:
        """
        The type of the bucket location.
        """
        return pulumi.get(self, "location_type")

    @property
    @pulumi.getter
    def logging(self) -> 'outputs.BucketLoggingResponse':
        """
        The bucket's logging configuration, which defines the destination bucket and optional name prefix for the current bucket's logs.
        """
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter
    def metageneration(self) -> str:
        """
        The metadata generation of this bucket.
        """
        return pulumi.get(self, "metageneration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the bucket.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> 'outputs.BucketOwnerResponse':
        """
        The owner of the bucket. This is always the project team's owner group.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> str:
        """
        The project number of the project the bucket belongs to.
        """
        return pulumi.get(self, "project_number")

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> 'outputs.BucketRetentionPolicyResponse':
        """
        The bucket's retention policy. The retention policy enforces a minimum retention time for all objects contained in the bucket, based on their creation time. Any attempt to overwrite or delete objects younger than the retention period will result in a PERMISSION_DENIED error. An unlocked retention policy can be modified or removed from the bucket via a storage.buckets.update operation. A locked retention policy cannot be removed or shortened in duration for the lifetime of the bucket. Attempting to remove or decrease period of a locked retention policy will result in a PERMISSION_DENIED error.
        """
        return pulumi.get(self, "retention_policy")

    @property
    @pulumi.getter
    def rpo(self) -> str:
        """
        The Recovery Point Objective (RPO) of this bucket. Set to ASYNC_TURBO to turn on Turbo Replication on a bucket.
        """
        return pulumi.get(self, "rpo")

    @property
    @pulumi.getter(name="satisfiesPZS")
    def satisfies_pzs(self) -> bool:
        """
        Reserved for future use.
        """
        return pulumi.get(self, "satisfies_pzs")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        The URI of this bucket.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> str:
        """
        The bucket's default storage class, used whenever no storageClass is specified for a newly-created object. This defines how objects in the bucket are stored and determines the SLA and the cost of storage. Values include MULTI_REGIONAL, REGIONAL, STANDARD, NEARLINE, COLDLINE, ARCHIVE, and DURABLE_REDUCED_AVAILABILITY. If this value is not specified when the bucket is created, it will default to STANDARD. For more information, see storage classes.
        """
        return pulumi.get(self, "storage_class")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The creation time of the bucket in RFC 3339 format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def updated(self) -> str:
        """
        The modification time of the bucket in RFC 3339 format.
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter
    def versioning(self) -> 'outputs.BucketVersioningResponse':
        """
        The bucket's versioning configuration.
        """
        return pulumi.get(self, "versioning")

    @property
    @pulumi.getter
    def website(self) -> 'outputs.BucketWebsiteResponse':
        """
        The bucket's website configuration, controlling how the service behaves when accessing bucket contents as a web site. See the Static Website Examples for more information.
        """
        return pulumi.get(self, "website")


class AwaitableGetBucketResult(GetBucketResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBucketResult(
            acl=self.acl,
            autoclass=self.autoclass,
            billing=self.billing,
            cors=self.cors,
            default_event_based_hold=self.default_event_based_hold,
            default_object_acl=self.default_object_acl,
            encryption=self.encryption,
            etag=self.etag,
            iam_configuration=self.iam_configuration,
            kind=self.kind,
            labels=self.labels,
            lifecycle=self.lifecycle,
            location=self.location,
            location_type=self.location_type,
            logging=self.logging,
            metageneration=self.metageneration,
            name=self.name,
            owner=self.owner,
            project_number=self.project_number,
            retention_policy=self.retention_policy,
            rpo=self.rpo,
            satisfies_pzs=self.satisfies_pzs,
            self_link=self.self_link,
            storage_class=self.storage_class,
            time_created=self.time_created,
            updated=self.updated,
            versioning=self.versioning,
            website=self.website)


def get_bucket(bucket: Optional[str] = None,
               if_metageneration_match: Optional[str] = None,
               if_metageneration_not_match: Optional[str] = None,
               projection: Optional[str] = None,
               user_project: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBucketResult:
    """
    Returns metadata for the specified bucket.
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    __args__['ifMetagenerationMatch'] = if_metageneration_match
    __args__['ifMetagenerationNotMatch'] = if_metageneration_not_match
    __args__['projection'] = projection
    __args__['userProject'] = user_project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:storage/v1:getBucket', __args__, opts=opts, typ=GetBucketResult).value

    return AwaitableGetBucketResult(
        acl=__ret__.acl,
        autoclass=__ret__.autoclass,
        billing=__ret__.billing,
        cors=__ret__.cors,
        default_event_based_hold=__ret__.default_event_based_hold,
        default_object_acl=__ret__.default_object_acl,
        encryption=__ret__.encryption,
        etag=__ret__.etag,
        iam_configuration=__ret__.iam_configuration,
        kind=__ret__.kind,
        labels=__ret__.labels,
        lifecycle=__ret__.lifecycle,
        location=__ret__.location,
        location_type=__ret__.location_type,
        logging=__ret__.logging,
        metageneration=__ret__.metageneration,
        name=__ret__.name,
        owner=__ret__.owner,
        project_number=__ret__.project_number,
        retention_policy=__ret__.retention_policy,
        rpo=__ret__.rpo,
        satisfies_pzs=__ret__.satisfies_pzs,
        self_link=__ret__.self_link,
        storage_class=__ret__.storage_class,
        time_created=__ret__.time_created,
        updated=__ret__.updated,
        versioning=__ret__.versioning,
        website=__ret__.website)


@_utilities.lift_output_func(get_bucket)
def get_bucket_output(bucket: Optional[pulumi.Input[str]] = None,
                      if_metageneration_match: Optional[pulumi.Input[Optional[str]]] = None,
                      if_metageneration_not_match: Optional[pulumi.Input[Optional[str]]] = None,
                      projection: Optional[pulumi.Input[Optional[str]]] = None,
                      user_project: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBucketResult]:
    """
    Returns metadata for the specified bucket.
    """
    ...
