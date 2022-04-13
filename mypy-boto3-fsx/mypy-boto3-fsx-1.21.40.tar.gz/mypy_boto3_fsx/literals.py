"""
Type annotations for fsx service literal definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/literals/)

Usage::

    ```python
    from mypy_boto3_fsx.literals import AdministrativeActionTypeType

    data: AdministrativeActionTypeType = "FILE_SYSTEM_ALIAS_ASSOCIATION"
    ```
"""
import sys

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdministrativeActionTypeType",
    "AliasLifecycleType",
    "AutoImportPolicyTypeType",
    "BackupLifecycleType",
    "BackupTypeType",
    "DataCompressionTypeType",
    "DataRepositoryLifecycleType",
    "DataRepositoryTaskFilterNameType",
    "DataRepositoryTaskLifecycleType",
    "DataRepositoryTaskTypeType",
    "DeleteFileSystemOpenZFSOptionType",
    "DeleteOpenZFSVolumeOptionType",
    "DescribeBackupsPaginatorName",
    "DescribeFileSystemsPaginatorName",
    "DescribeStorageVirtualMachinesPaginatorName",
    "DescribeVolumesPaginatorName",
    "DiskIopsConfigurationModeType",
    "DriveCacheTypeType",
    "EventTypeType",
    "FileSystemLifecycleType",
    "FileSystemMaintenanceOperationType",
    "FileSystemTypeType",
    "FilterNameType",
    "FlexCacheEndpointTypeType",
    "ListTagsForResourcePaginatorName",
    "LustreAccessAuditLogLevelType",
    "LustreDeploymentTypeType",
    "OntapDeploymentTypeType",
    "OntapVolumeTypeType",
    "OpenZFSCopyStrategyType",
    "OpenZFSDataCompressionTypeType",
    "OpenZFSDeploymentTypeType",
    "OpenZFSQuotaTypeType",
    "ReportFormatType",
    "ReportScopeType",
    "ResourceTypeType",
    "RestoreOpenZFSVolumeOptionType",
    "SecurityStyleType",
    "SnapshotFilterNameType",
    "SnapshotLifecycleType",
    "StatusType",
    "StorageTypeType",
    "StorageVirtualMachineFilterNameType",
    "StorageVirtualMachineLifecycleType",
    "StorageVirtualMachineRootVolumeSecurityStyleType",
    "StorageVirtualMachineSubtypeType",
    "TieringPolicyNameType",
    "VolumeFilterNameType",
    "VolumeLifecycleType",
    "VolumeTypeType",
    "WindowsAccessAuditLogLevelType",
    "WindowsDeploymentTypeType",
    "FSxServiceName",
    "ServiceName",
    "ResourceServiceName",
    "PaginatorName",
    "RegionName",
)


AdministrativeActionTypeType = Literal[
    "FILE_SYSTEM_ALIAS_ASSOCIATION",
    "FILE_SYSTEM_ALIAS_DISASSOCIATION",
    "FILE_SYSTEM_UPDATE",
    "RELEASE_NFS_V3_LOCKS",
    "SNAPSHOT_UPDATE",
    "STORAGE_OPTIMIZATION",
    "VOLUME_UPDATE",
]
AliasLifecycleType = Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
AutoImportPolicyTypeType = Literal["NEW", "NEW_CHANGED", "NEW_CHANGED_DELETED", "NONE"]
BackupLifecycleType = Literal[
    "AVAILABLE", "COPYING", "CREATING", "DELETED", "FAILED", "PENDING", "TRANSFERRING"
]
BackupTypeType = Literal["AUTOMATIC", "AWS_BACKUP", "USER_INITIATED"]
DataCompressionTypeType = Literal["LZ4", "NONE"]
DataRepositoryLifecycleType = Literal[
    "AVAILABLE", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "UPDATING"
]
DataRepositoryTaskFilterNameType = Literal[
    "data-repository-association-id", "file-system-id", "task-lifecycle"
]
DataRepositoryTaskLifecycleType = Literal[
    "CANCELED", "CANCELING", "EXECUTING", "FAILED", "PENDING", "SUCCEEDED"
]
DataRepositoryTaskTypeType = Literal["EXPORT_TO_REPOSITORY", "IMPORT_METADATA_FROM_REPOSITORY"]
DeleteFileSystemOpenZFSOptionType = Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]
DeleteOpenZFSVolumeOptionType = Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]
DescribeBackupsPaginatorName = Literal["describe_backups"]
DescribeFileSystemsPaginatorName = Literal["describe_file_systems"]
DescribeStorageVirtualMachinesPaginatorName = Literal["describe_storage_virtual_machines"]
DescribeVolumesPaginatorName = Literal["describe_volumes"]
DiskIopsConfigurationModeType = Literal["AUTOMATIC", "USER_PROVISIONED"]
DriveCacheTypeType = Literal["NONE", "READ"]
EventTypeType = Literal["CHANGED", "DELETED", "NEW"]
FileSystemLifecycleType = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "FAILED",
    "MISCONFIGURED",
    "MISCONFIGURED_UNAVAILABLE",
    "UPDATING",
]
FileSystemMaintenanceOperationType = Literal["BACKING_UP", "PATCHING"]
FileSystemTypeType = Literal["LUSTRE", "ONTAP", "OPENZFS", "WINDOWS"]
FilterNameType = Literal[
    "backup-type", "data-repository-type", "file-system-id", "file-system-type", "volume-id"
]
FlexCacheEndpointTypeType = Literal["CACHE", "NONE", "ORIGIN"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
LustreAccessAuditLogLevelType = Literal["DISABLED", "ERROR_ONLY", "WARN_ERROR", "WARN_ONLY"]
LustreDeploymentTypeType = Literal["PERSISTENT_1", "PERSISTENT_2", "SCRATCH_1", "SCRATCH_2"]
OntapDeploymentTypeType = Literal["MULTI_AZ_1", "SINGLE_AZ_1"]
OntapVolumeTypeType = Literal["DP", "LS", "RW"]
OpenZFSCopyStrategyType = Literal["CLONE", "FULL_COPY"]
OpenZFSDataCompressionTypeType = Literal["LZ4", "NONE", "ZSTD"]
OpenZFSDeploymentTypeType = Literal["SINGLE_AZ_1"]
OpenZFSQuotaTypeType = Literal["GROUP", "USER"]
ReportFormatType = Literal["REPORT_CSV_20191124"]
ReportScopeType = Literal["FAILED_FILES_ONLY"]
ResourceTypeType = Literal["FILE_SYSTEM", "VOLUME"]
RestoreOpenZFSVolumeOptionType = Literal["DELETE_CLONED_VOLUMES", "DELETE_INTERMEDIATE_SNAPSHOTS"]
SecurityStyleType = Literal["MIXED", "NTFS", "UNIX"]
SnapshotFilterNameType = Literal["file-system-id", "volume-id"]
SnapshotLifecycleType = Literal["AVAILABLE", "CREATING", "DELETING", "PENDING"]
StatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "UPDATED_OPTIMIZING"]
StorageTypeType = Literal["HDD", "SSD"]
StorageVirtualMachineFilterNameType = Literal["file-system-id"]
StorageVirtualMachineLifecycleType = Literal[
    "CREATED", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "PENDING"
]
StorageVirtualMachineRootVolumeSecurityStyleType = Literal["MIXED", "NTFS", "UNIX"]
StorageVirtualMachineSubtypeType = Literal[
    "DEFAULT", "DP_DESTINATION", "SYNC_DESTINATION", "SYNC_SOURCE"
]
TieringPolicyNameType = Literal["ALL", "AUTO", "NONE", "SNAPSHOT_ONLY"]
VolumeFilterNameType = Literal["file-system-id", "storage-virtual-machine-id"]
VolumeLifecycleType = Literal[
    "AVAILABLE", "CREATED", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "PENDING"
]
VolumeTypeType = Literal["ONTAP", "OPENZFS"]
WindowsAccessAuditLogLevelType = Literal[
    "DISABLED", "FAILURE_ONLY", "SUCCESS_AND_FAILURE", "SUCCESS_ONLY"
]
WindowsDeploymentTypeType = Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
FSxServiceName = Literal["fsx"]
ServiceName = Literal[
    "accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "alexaforbusiness",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "backup",
    "backup-gateway",
    "batch",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecommit",
    "codedeploy",
    "codeguru-reviewer",
    "codeguruprofiler",
    "codepipeline",
    "codestar",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectparticipant",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "dax",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "drs",
    "ds",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "fsx",
    "gamelift",
    "gamesparks",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "honeycode",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector2",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot1click-devices",
    "iot1click-projects",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "kafka",
    "kafkaconnect",
    "kendra",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "machinelearning",
    "macie",
    "macie2",
    "managedblockchain",
    "marketplace-catalog",
    "marketplace-entitlement",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhubstrategy",
    "mobile",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "network-firewall",
    "networkmanager",
    "nimble",
    "opensearch",
    "opsworks",
    "opsworkscm",
    "organizations",
    "outposts",
    "panorama",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "polly",
    "pricing",
    "proton",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "rekognition",
    "resiliencehub",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-runtime",
    "savingsplans",
    "schemas",
    "sdb",
    "secretsmanager",
    "securityhub",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "support",
    "swf",
    "synthetics",
    "textract",
    "timestream-query",
    "timestream-write",
    "transcribe",
    "transfer",
    "translate",
    "voice-id",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "worklink",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-web",
    "xray",
]
ResourceServiceName = Literal[
    "cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",
]
PaginatorName = Literal[
    "describe_backups",
    "describe_file_systems",
    "describe_storage_virtual_machines",
    "describe_volumes",
    "list_tags_for_resource",
]
RegionName = Literal[
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-south-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
