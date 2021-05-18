# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='github.proto',
  package='blueintel.badapi.github',
  syntax='proto3',
  serialized_options=b'Z\n.;githubpb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cgithub.proto\x12\x17\x62lueintel.badapi.github\"M\n\x04\x46ile\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\x13\n\x0b\x66ileVersion\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x0f\n\x07matches\x18\x04 \x03(\t\"y\n\x05\x41lert\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x0f\n\x07RepoURL\x18\x03 \x01(\t\x12\x10\n\x08Keywords\x18\x05 \x03(\t\x12\x11\n\tTimestamp\x18\x06 \x01(\t\x12.\n\x07Matches\x18\x07 \x03(\x0b\x32\x1d.blueintel.badapi.github.File\"T\n\x11ListAlertsRequest\x12\x0b\n\x03org\x18\x01 \x01(\t\x12\x0e\n\x06viewed\x18\x02 \x01(\x08\x12\x11\n\tstartdate\x18\x03 \x01(\t\x12\x0f\n\x07\x65nddate\x18\x04 \x01(\t2m\n\rGithubService\x12\\\n\nListAlerts\x12*.blueintel.badapi.github.ListAlertsRequest\x1a\x1e.blueintel.badapi.github.Alert\"\x00\x30\x01\x42\x0cZ\n.;githubpbb\x06proto3'
)




_FILE = _descriptor.Descriptor(
  name='File',
  full_name='blueintel.badapi.github.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='blueintel.badapi.github.File.file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileVersion', full_name='blueintel.badapi.github.File.fileVersion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='blueintel.badapi.github.File.timestamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matches', full_name='blueintel.badapi.github.File.matches', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=118,
)


_ALERT = _descriptor.Descriptor(
  name='Alert',
  full_name='blueintel.badapi.github.Alert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='blueintel.badapi.github.Alert.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RepoURL', full_name='blueintel.badapi.github.Alert.RepoURL', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Keywords', full_name='blueintel.badapi.github.Alert.Keywords', index=2,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='blueintel.badapi.github.Alert.Timestamp', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Matches', full_name='blueintel.badapi.github.Alert.Matches', index=4,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=241,
)


_LISTALERTSREQUEST = _descriptor.Descriptor(
  name='ListAlertsRequest',
  full_name='blueintel.badapi.github.ListAlertsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='blueintel.badapi.github.ListAlertsRequest.org', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='viewed', full_name='blueintel.badapi.github.ListAlertsRequest.viewed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startdate', full_name='blueintel.badapi.github.ListAlertsRequest.startdate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enddate', full_name='blueintel.badapi.github.ListAlertsRequest.enddate', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=327,
)

_ALERT.fields_by_name['Matches'].message_type = _FILE
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Alert'] = _ALERT
DESCRIPTOR.message_types_by_name['ListAlertsRequest'] = _LISTALERTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'github_pb2'
  # @@protoc_insertion_point(class_scope:blueintel.badapi.github.File)
  })
_sym_db.RegisterMessage(File)

Alert = _reflection.GeneratedProtocolMessageType('Alert', (_message.Message,), {
  'DESCRIPTOR' : _ALERT,
  '__module__' : 'github_pb2'
  # @@protoc_insertion_point(class_scope:blueintel.badapi.github.Alert)
  })
_sym_db.RegisterMessage(Alert)

ListAlertsRequest = _reflection.GeneratedProtocolMessageType('ListAlertsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTALERTSREQUEST,
  '__module__' : 'github_pb2'
  # @@protoc_insertion_point(class_scope:blueintel.badapi.github.ListAlertsRequest)
  })
_sym_db.RegisterMessage(ListAlertsRequest)


DESCRIPTOR._options = None

_GITHUBSERVICE = _descriptor.ServiceDescriptor(
  name='GithubService',
  full_name='blueintel.badapi.github.GithubService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=329,
  serialized_end=438,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListAlerts',
    full_name='blueintel.badapi.github.GithubService.ListAlerts',
    index=0,
    containing_service=None,
    input_type=_LISTALERTSREQUEST,
    output_type=_ALERT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GITHUBSERVICE)

DESCRIPTOR.services_by_name['GithubService'] = _GITHUBSERVICE

# @@protoc_insertion_point(module_scope)