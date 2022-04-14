# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engine.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="engine.proto",
    package="pulumirpc",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x0c\x65ngine.proto\x12\tpulumirpc\x1a\x1bgoogle/protobuf/empty.proto"y\n\nLogRequest\x12(\n\x08severity\x18\x01 \x01(\x0e\x32\x16.pulumirpc.LogSeverity\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0b\n\x03urn\x18\x03 \x01(\t\x12\x10\n\x08streamId\x18\x04 \x01(\x05\x12\x11\n\tephemeral\x18\x05 \x01(\x08"\x18\n\x16GetRootResourceRequest"&\n\x17GetRootResourceResponse\x12\x0b\n\x03urn\x18\x01 \x01(\t"%\n\x16SetRootResourceRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t"\x19\n\x17SetRootResourceResponse*:\n\x0bLogSeverity\x12\t\n\x05\x44\x45\x42UG\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x32\xf8\x01\n\x06\x45ngine\x12\x36\n\x03Log\x12\x15.pulumirpc.LogRequest\x1a\x16.google.protobuf.Empty"\x00\x12Z\n\x0fGetRootResource\x12!.pulumirpc.GetRootResourceRequest\x1a".pulumirpc.GetRootResourceResponse"\x00\x12Z\n\x0fSetRootResource\x12!.pulumirpc.SetRootResourceRequest\x1a".pulumirpc.SetRootResourceResponse"\x00\x62\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
    ],
)

_LOGSEVERITY = _descriptor.EnumDescriptor(
    name="LogSeverity",
    full_name="pulumirpc.LogSeverity",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="DEBUG", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INFO", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="WARNING", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=311,
    serialized_end=369,
)
_sym_db.RegisterEnumDescriptor(_LOGSEVERITY)

LogSeverity = enum_type_wrapper.EnumTypeWrapper(_LOGSEVERITY)
DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3


_LOGREQUEST = _descriptor.Descriptor(
    name="LogRequest",
    full_name="pulumirpc.LogRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="severity",
            full_name="pulumirpc.LogRequest.severity",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="message",
            full_name="pulumirpc.LogRequest.message",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="urn",
            full_name="pulumirpc.LogRequest.urn",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="streamId",
            full_name="pulumirpc.LogRequest.streamId",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="ephemeral",
            full_name="pulumirpc.LogRequest.ephemeral",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=56,
    serialized_end=177,
)


_GETROOTRESOURCEREQUEST = _descriptor.Descriptor(
    name="GetRootResourceRequest",
    full_name="pulumirpc.GetRootResourceRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=179,
    serialized_end=203,
)


_GETROOTRESOURCERESPONSE = _descriptor.Descriptor(
    name="GetRootResourceResponse",
    full_name="pulumirpc.GetRootResourceResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="urn",
            full_name="pulumirpc.GetRootResourceResponse.urn",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=205,
    serialized_end=243,
)


_SETROOTRESOURCEREQUEST = _descriptor.Descriptor(
    name="SetRootResourceRequest",
    full_name="pulumirpc.SetRootResourceRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="urn",
            full_name="pulumirpc.SetRootResourceRequest.urn",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=245,
    serialized_end=282,
)


_SETROOTRESOURCERESPONSE = _descriptor.Descriptor(
    name="SetRootResourceResponse",
    full_name="pulumirpc.SetRootResourceResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=284,
    serialized_end=309,
)

_LOGREQUEST.fields_by_name["severity"].enum_type = _LOGSEVERITY
DESCRIPTOR.message_types_by_name["LogRequest"] = _LOGREQUEST
DESCRIPTOR.message_types_by_name["GetRootResourceRequest"] = _GETROOTRESOURCEREQUEST
DESCRIPTOR.message_types_by_name["GetRootResourceResponse"] = _GETROOTRESOURCERESPONSE
DESCRIPTOR.message_types_by_name["SetRootResourceRequest"] = _SETROOTRESOURCEREQUEST
DESCRIPTOR.message_types_by_name["SetRootResourceResponse"] = _SETROOTRESOURCERESPONSE
DESCRIPTOR.enum_types_by_name["LogSeverity"] = _LOGSEVERITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogRequest = _reflection.GeneratedProtocolMessageType(
    "LogRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOGREQUEST,
        "__module__": "engine_pb2"
        # @@protoc_insertion_point(class_scope:pulumirpc.LogRequest)
    },
)
_sym_db.RegisterMessage(LogRequest)

GetRootResourceRequest = _reflection.GeneratedProtocolMessageType(
    "GetRootResourceRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETROOTRESOURCEREQUEST,
        "__module__": "engine_pb2"
        # @@protoc_insertion_point(class_scope:pulumirpc.GetRootResourceRequest)
    },
)
_sym_db.RegisterMessage(GetRootResourceRequest)

GetRootResourceResponse = _reflection.GeneratedProtocolMessageType(
    "GetRootResourceResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETROOTRESOURCERESPONSE,
        "__module__": "engine_pb2"
        # @@protoc_insertion_point(class_scope:pulumirpc.GetRootResourceResponse)
    },
)
_sym_db.RegisterMessage(GetRootResourceResponse)

SetRootResourceRequest = _reflection.GeneratedProtocolMessageType(
    "SetRootResourceRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETROOTRESOURCEREQUEST,
        "__module__": "engine_pb2"
        # @@protoc_insertion_point(class_scope:pulumirpc.SetRootResourceRequest)
    },
)
_sym_db.RegisterMessage(SetRootResourceRequest)

SetRootResourceResponse = _reflection.GeneratedProtocolMessageType(
    "SetRootResourceResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETROOTRESOURCERESPONSE,
        "__module__": "engine_pb2"
        # @@protoc_insertion_point(class_scope:pulumirpc.SetRootResourceResponse)
    },
)
_sym_db.RegisterMessage(SetRootResourceResponse)


_ENGINE = _descriptor.ServiceDescriptor(
    name="Engine",
    full_name="pulumirpc.Engine",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=372,
    serialized_end=620,
    methods=[
        _descriptor.MethodDescriptor(
            name="Log",
            full_name="pulumirpc.Engine.Log",
            index=0,
            containing_service=None,
            input_type=_LOGREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="GetRootResource",
            full_name="pulumirpc.Engine.GetRootResource",
            index=1,
            containing_service=None,
            input_type=_GETROOTRESOURCEREQUEST,
            output_type=_GETROOTRESOURCERESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="SetRootResource",
            full_name="pulumirpc.Engine.SetRootResource",
            index=2,
            containing_service=None,
            input_type=_SETROOTRESOURCEREQUEST,
            output_type=_SETROOTRESOURCERESPONSE,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_ENGINE)

DESCRIPTOR.services_by_name["Engine"] = _ENGINE

# @@protoc_insertion_point(module_scope)
