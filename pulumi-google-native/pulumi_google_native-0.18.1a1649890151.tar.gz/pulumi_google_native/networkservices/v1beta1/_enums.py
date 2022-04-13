# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuditLogConfigLogType',
    'EndpointPolicyType',
    'GatewayType',
    'GrpcRouteHeaderMatchType',
    'GrpcRouteMethodMatchType',
    'HttpRouteRedirectResponseCode',
    'MetadataLabelMatcherMetadataLabelMatchCriteria',
]


class AuditLogConfigLogType(str, Enum):
    """
    The log type that this config enables.
    """
    LOG_TYPE_UNSPECIFIED = "LOG_TYPE_UNSPECIFIED"
    """
    Default case. Should never be this.
    """
    ADMIN_READ = "ADMIN_READ"
    """
    Admin reads. Example: CloudIAM getIamPolicy
    """
    DATA_WRITE = "DATA_WRITE"
    """
    Data writes. Example: CloudSQL Users create
    """
    DATA_READ = "DATA_READ"
    """
    Data reads. Example: CloudSQL Users list
    """


class EndpointPolicyType(str, Enum):
    """
    Required. The type of endpoint policy. This is primarily used to validate the configuration.
    """
    ENDPOINT_POLICY_TYPE_UNSPECIFIED = "ENDPOINT_POLICY_TYPE_UNSPECIFIED"
    """
    Default value. Must not be used.
    """
    SIDECAR_PROXY = "SIDECAR_PROXY"
    """
    Represents a proxy deployed as a sidecar.
    """
    GRPC_SERVER = "GRPC_SERVER"
    """
    Represents a proxyless gRPC backend.
    """


class GatewayType(str, Enum):
    """
    Immutable. The type of the customer managed gateway.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    The type of the customer managed gateway is unspecified.
    """
    OPEN_MESH = "OPEN_MESH"
    """
    The type of the customer managed gateway is TrafficDirector Open Mesh.
    """
    SECURE_WEB_GATEWAY = "SECURE_WEB_GATEWAY"
    """
    The type of the customer managed gateway is SecureWebGateway (SWG).
    """


class GrpcRouteHeaderMatchType(str, Enum):
    """
    Optional. Specifies how to match against the value of the header. If not specified, a default value of EXACT is used.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    Unspecified.
    """
    EXACT = "EXACT"
    """
    Will only match the exact value provided.
    """
    REGULAR_EXPRESSION = "REGULAR_EXPRESSION"
    """
    Will match paths conforming to the prefix specified by value. RE2 syntax is supported.
    """


class GrpcRouteMethodMatchType(str, Enum):
    """
    Optional. Specifies how to match against the name. If not specified, a default value of "EXACT" is used.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    Unspecified.
    """
    EXACT = "EXACT"
    """
    Will only match the exact name provided.
    """
    REGULAR_EXPRESSION = "REGULAR_EXPRESSION"
    """
    Will interpret grpc_method and grpc_service as regexes. RE2 syntax is supported.
    """


class HttpRouteRedirectResponseCode(str, Enum):
    """
    The HTTP Status code to use for the redirect.
    """
    RESPONSE_CODE_UNSPECIFIED = "RESPONSE_CODE_UNSPECIFIED"
    """
    Default value
    """
    MOVED_PERMANENTLY_DEFAULT = "MOVED_PERMANENTLY_DEFAULT"
    """
    Corresponds to 301.
    """
    FOUND = "FOUND"
    """
    Corresponds to 302.
    """
    SEE_OTHER = "SEE_OTHER"
    """
    Corresponds to 303.
    """
    TEMPORARY_REDIRECT = "TEMPORARY_REDIRECT"
    """
    Corresponds to 307. In this case, the request method will be retained.
    """
    PERMANENT_REDIRECT = "PERMANENT_REDIRECT"
    """
    Corresponds to 308. In this case, the request method will be retained.
    """


class MetadataLabelMatcherMetadataLabelMatchCriteria(str, Enum):
    """
    Specifies how matching should be done. Supported values are: MATCH_ANY: At least one of the Labels specified in the matcher should match the metadata presented by xDS client. MATCH_ALL: The metadata presented by the xDS client should contain all of the labels specified here. The selection is determined based on the best match. For example, suppose there are three EndpointPolicy resources P1, P2 and P3 and if P1 has a the matcher as MATCH_ANY , P2 has MATCH_ALL , and P3 has MATCH_ALL . If a client with label connects, the config from P1 will be selected. If a client with label connects, the config from P2 will be selected. If a client with label connects, the config from P3 will be selected. If there is more than one best match, (for example, if a config P4 with selector exists and if a client with label connects), an error will be thrown.
    """
    METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED = "METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED"
    """
    Default value. Should not be used.
    """
    MATCH_ANY = "MATCH_ANY"
    """
    At least one of the Labels specified in the matcher should match the metadata presented by xDS client.
    """
    MATCH_ALL = "MATCH_ALL"
    """
    The metadata presented by the xDS client should contain all of the labels specified here.
    """
