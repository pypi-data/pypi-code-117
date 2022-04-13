# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/online_store/status_entry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tecton_proto/online_store/status_entry.proto',
  package='tecton_proto.online_store',
  syntax='proto2',
  serialized_options=b'\n\026com.tecton.onlinestoreP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,tecton_proto/online_store/status_entry.proto\x12\x19tecton_proto.online_store\"z\n\x0bStatusEntry\x12\x1f\n\x0bsource_type\x18\x01 \x01(\tR\nsourceType\x12)\n\x11raw_data_end_time\x18\x02 \x01(\x03R\x0erawDataEndTime\x12\x1f\n\x0b\x61nchor_time\x18\x03 \x01(\x03R\nanchorTimeB\x1a\n\x16\x63om.tecton.onlinestoreP\x01'
)




_STATUSENTRY = _descriptor.Descriptor(
  name='StatusEntry',
  full_name='tecton_proto.online_store.StatusEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_type', full_name='tecton_proto.online_store.StatusEntry.source_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sourceType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='raw_data_end_time', full_name='tecton_proto.online_store.StatusEntry.raw_data_end_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rawDataEndTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='anchor_time', full_name='tecton_proto.online_store.StatusEntry.anchor_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='anchorTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=197,
)

DESCRIPTOR.message_types_by_name['StatusEntry'] = _STATUSENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusEntry = _reflection.GeneratedProtocolMessageType('StatusEntry', (_message.Message,), {
  'DESCRIPTOR' : _STATUSENTRY,
  '__module__' : 'tecton_proto.online_store.status_entry_pb2'
  # @@protoc_insertion_point(class_scope:tecton_proto.online_store.StatusEntry)
  })
_sym_db.RegisterMessage(StatusEntry)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
