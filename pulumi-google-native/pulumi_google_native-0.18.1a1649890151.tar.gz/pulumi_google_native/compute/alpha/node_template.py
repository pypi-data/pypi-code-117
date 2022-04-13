# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['NodeTemplateArgs', 'NodeTemplate']

@pulumi.input_type
class NodeTemplateArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 accelerators: Optional[pulumi.Input[Sequence[pulumi.Input['AcceleratorConfigArgs']]]] = None,
                 cpu_overcommit_type: Optional[pulumi.Input['NodeTemplateCpuOvercommitType']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input['LocalDiskArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_type: Optional[pulumi.Input[str]] = None,
                 node_type_flexibility: Optional[pulumi.Input['NodeTemplateNodeTypeFlexibilityArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 server_binding: Optional[pulumi.Input['ServerBindingArgs']] = None):
        """
        The set of arguments for constructing a NodeTemplate resource.
        :param pulumi.Input['NodeTemplateCpuOvercommitType'] cpu_overcommit_type: CPU overcommit.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] name: The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] node_affinity_labels: Labels to use for node affinity, which will be used in instance scheduling.
        :param pulumi.Input[str] node_type: The node type to use for nodes group that are created from this template.
        :param pulumi.Input['NodeTemplateNodeTypeFlexibilityArgs'] node_type_flexibility: The flexible properties of the desired node type. Node groups that use this node template will create nodes of a type that matches these properties. This field is mutually exclusive with the node_type property; you can only define one or the other, but not both.
        :param pulumi.Input[str] request_id: An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        :param pulumi.Input['ServerBindingArgs'] server_binding: Sets the binding properties for the physical server. Valid values include: - *[Default]* RESTART_NODE_ON_ANY_SERVER: Restarts VMs on any available physical server - RESTART_NODE_ON_MINIMAL_SERVER: Restarts VMs on the same physical server whenever possible See Sole-tenant node options for more information.
        """
        pulumi.set(__self__, "region", region)
        if accelerators is not None:
            pulumi.set(__self__, "accelerators", accelerators)
        if cpu_overcommit_type is not None:
            pulumi.set(__self__, "cpu_overcommit_type", cpu_overcommit_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disks is not None:
            pulumi.set(__self__, "disks", disks)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_affinity_labels is not None:
            pulumi.set(__self__, "node_affinity_labels", node_affinity_labels)
        if node_type is not None:
            pulumi.set(__self__, "node_type", node_type)
        if node_type_flexibility is not None:
            pulumi.set(__self__, "node_type_flexibility", node_type_flexibility)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if server_binding is not None:
            pulumi.set(__self__, "server_binding", server_binding)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AcceleratorConfigArgs']]]]:
        return pulumi.get(self, "accelerators")

    @accelerators.setter
    def accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AcceleratorConfigArgs']]]]):
        pulumi.set(self, "accelerators", value)

    @property
    @pulumi.getter(name="cpuOvercommitType")
    def cpu_overcommit_type(self) -> Optional[pulumi.Input['NodeTemplateCpuOvercommitType']]:
        """
        CPU overcommit.
        """
        return pulumi.get(self, "cpu_overcommit_type")

    @cpu_overcommit_type.setter
    def cpu_overcommit_type(self, value: Optional[pulumi.Input['NodeTemplateCpuOvercommitType']]):
        pulumi.set(self, "cpu_overcommit_type", value)

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
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalDiskArgs']]]]:
        return pulumi.get(self, "disks")

    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalDiskArgs']]]]):
        pulumi.set(self, "disks", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeAffinityLabels")
    def node_affinity_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels to use for node affinity, which will be used in instance scheduling.
        """
        return pulumi.get(self, "node_affinity_labels")

    @node_affinity_labels.setter
    def node_affinity_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "node_affinity_labels", value)

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[str]]:
        """
        The node type to use for nodes group that are created from this template.
        """
        return pulumi.get(self, "node_type")

    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_type", value)

    @property
    @pulumi.getter(name="nodeTypeFlexibility")
    def node_type_flexibility(self) -> Optional[pulumi.Input['NodeTemplateNodeTypeFlexibilityArgs']]:
        """
        The flexible properties of the desired node type. Node groups that use this node template will create nodes of a type that matches these properties. This field is mutually exclusive with the node_type property; you can only define one or the other, but not both.
        """
        return pulumi.get(self, "node_type_flexibility")

    @node_type_flexibility.setter
    def node_type_flexibility(self, value: Optional[pulumi.Input['NodeTemplateNodeTypeFlexibilityArgs']]):
        pulumi.set(self, "node_type_flexibility", value)

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
    @pulumi.getter(name="serverBinding")
    def server_binding(self) -> Optional[pulumi.Input['ServerBindingArgs']]:
        """
        Sets the binding properties for the physical server. Valid values include: - *[Default]* RESTART_NODE_ON_ANY_SERVER: Restarts VMs on any available physical server - RESTART_NODE_ON_MINIMAL_SERVER: Restarts VMs on the same physical server whenever possible See Sole-tenant node options for more information.
        """
        return pulumi.get(self, "server_binding")

    @server_binding.setter
    def server_binding(self, value: Optional[pulumi.Input['ServerBindingArgs']]):
        pulumi.set(self, "server_binding", value)


class NodeTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AcceleratorConfigArgs']]]]] = None,
                 cpu_overcommit_type: Optional[pulumi.Input['NodeTemplateCpuOvercommitType']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalDiskArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_type: Optional[pulumi.Input[str]] = None,
                 node_type_flexibility: Optional[pulumi.Input[pulumi.InputType['NodeTemplateNodeTypeFlexibilityArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 server_binding: Optional[pulumi.Input[pulumi.InputType['ServerBindingArgs']]] = None,
                 __props__=None):
        """
        Creates a NodeTemplate resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['NodeTemplateCpuOvercommitType'] cpu_overcommit_type: CPU overcommit.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] name: The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] node_affinity_labels: Labels to use for node affinity, which will be used in instance scheduling.
        :param pulumi.Input[str] node_type: The node type to use for nodes group that are created from this template.
        :param pulumi.Input[pulumi.InputType['NodeTemplateNodeTypeFlexibilityArgs']] node_type_flexibility: The flexible properties of the desired node type. Node groups that use this node template will create nodes of a type that matches these properties. This field is mutually exclusive with the node_type property; you can only define one or the other, but not both.
        :param pulumi.Input[str] request_id: An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        :param pulumi.Input[pulumi.InputType['ServerBindingArgs']] server_binding: Sets the binding properties for the physical server. Valid values include: - *[Default]* RESTART_NODE_ON_ANY_SERVER: Restarts VMs on any available physical server - RESTART_NODE_ON_MINIMAL_SERVER: Restarts VMs on the same physical server whenever possible See Sole-tenant node options for more information.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NodeTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a NodeTemplate resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param NodeTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NodeTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AcceleratorConfigArgs']]]]] = None,
                 cpu_overcommit_type: Optional[pulumi.Input['NodeTemplateCpuOvercommitType']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocalDiskArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_type: Optional[pulumi.Input[str]] = None,
                 node_type_flexibility: Optional[pulumi.Input[pulumi.InputType['NodeTemplateNodeTypeFlexibilityArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 server_binding: Optional[pulumi.Input[pulumi.InputType['ServerBindingArgs']]] = None,
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
            __props__ = NodeTemplateArgs.__new__(NodeTemplateArgs)

            __props__.__dict__["accelerators"] = accelerators
            __props__.__dict__["cpu_overcommit_type"] = cpu_overcommit_type
            __props__.__dict__["description"] = description
            __props__.__dict__["disks"] = disks
            __props__.__dict__["name"] = name
            __props__.__dict__["node_affinity_labels"] = node_affinity_labels
            __props__.__dict__["node_type"] = node_type
            __props__.__dict__["node_type_flexibility"] = node_type_flexibility
            __props__.__dict__["project"] = project
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["server_binding"] = server_binding
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["self_link_with_id"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_message"] = None
        super(NodeTemplate, __self__).__init__(
            'google-native:compute/alpha:NodeTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NodeTemplate':
        """
        Get an existing NodeTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NodeTemplateArgs.__new__(NodeTemplateArgs)

        __props__.__dict__["accelerators"] = None
        __props__.__dict__["cpu_overcommit_type"] = None
        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["disks"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["node_affinity_labels"] = None
        __props__.__dict__["node_type"] = None
        __props__.__dict__["node_type_flexibility"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["self_link_with_id"] = None
        __props__.__dict__["server_binding"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_message"] = None
        return NodeTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def accelerators(self) -> pulumi.Output[Sequence['outputs.AcceleratorConfigResponse']]:
        return pulumi.get(self, "accelerators")

    @property
    @pulumi.getter(name="cpuOvercommitType")
    def cpu_overcommit_type(self) -> pulumi.Output[str]:
        """
        CPU overcommit.
        """
        return pulumi.get(self, "cpu_overcommit_type")

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
    @pulumi.getter
    def disks(self) -> pulumi.Output[Sequence['outputs.LocalDiskResponse']]:
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The type of the resource. Always compute#nodeTemplate for node templates.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeAffinityLabels")
    def node_affinity_labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels to use for node affinity, which will be used in instance scheduling.
        """
        return pulumi.get(self, "node_affinity_labels")

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[str]:
        """
        The node type to use for nodes group that are created from this template.
        """
        return pulumi.get(self, "node_type")

    @property
    @pulumi.getter(name="nodeTypeFlexibility")
    def node_type_flexibility(self) -> pulumi.Output['outputs.NodeTemplateNodeTypeFlexibilityResponse']:
        """
        The flexible properties of the desired node type. Node groups that use this node template will create nodes of a type that matches these properties. This field is mutually exclusive with the node_type property; you can only define one or the other, but not both.
        """
        return pulumi.get(self, "node_type_flexibility")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The name of the region where the node template resides, such as us-central1.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[str]:
        """
        Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter(name="serverBinding")
    def server_binding(self) -> pulumi.Output['outputs.ServerBindingResponse']:
        """
        Sets the binding properties for the physical server. Valid values include: - *[Default]* RESTART_NODE_ON_ANY_SERVER: Restarts VMs on any available physical server - RESTART_NODE_ON_MINIMAL_SERVER: Restarts VMs on the same physical server whenever possible See Sole-tenant node options for more information.
        """
        return pulumi.get(self, "server_binding")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the node template. One of the following values: CREATING, READY, and DELETING.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        An optional, human-readable explanation of the status.
        """
        return pulumi.get(self, "status_message")

