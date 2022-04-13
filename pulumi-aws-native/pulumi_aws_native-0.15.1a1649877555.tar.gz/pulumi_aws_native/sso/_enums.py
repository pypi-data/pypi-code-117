# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AssignmentPrincipalType',
    'AssignmentTargetType',
]


class AssignmentPrincipalType(str, Enum):
    """
    The assignee's type, user/group
    """
    USER = "USER"
    GROUP = "GROUP"


class AssignmentTargetType(str, Enum):
    """
    The type of resource to be provsioned to, only aws account now
    """
    AWS_ACCOUNT = "AWS_ACCOUNT"
