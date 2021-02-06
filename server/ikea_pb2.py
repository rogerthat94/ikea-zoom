# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ikea.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ikea.proto',
  package='sandwich',
  syntax='proto3',
  serialized_options=_b('\n\017edu.cmu.cs.ikeaB\006Protos'),
  serialized_pb=_b('\n\nikea.proto\x12\x08sandwich\"\x88\x02\n\x05State\x12\x14\n\x0cupdate_count\x18\x01 \x01(\x03\x12\"\n\x04step\x18\x02 \x01(\x0e\x32\x14.sandwich.State.Step\x12\x1e\n\x16\x66rames_with_one_buckle\x18\x03 \x01(\x05\x12\x1f\n\x17\x66rames_with_two_buckles\x18\x04 \x01(\x05\"\x83\x01\n\x04Step\x12\t\n\x05START\x10\x00\x12\x0b\n\x07NOTHING\x10\x01\x12\x08\n\x04\x42\x41SE\x10\x02\x12\x08\n\x04PIPE\x10\x03\x12\t\n\x05SHADE\x10\x04\x12\n\n\x06\x42UCKLE\x10\x05\x12\x10\n\x0c\x42LACK_CIRCLE\x10\x06\x12\x0e\n\nSHADE_BASE\x10\x07\x12\x08\n\x04\x42ULB\x10\x08\x12\x0c\n\x08\x42ULB_TOP\x10\t\"\x9a\x01\n\x0eToServerExtras\x12\x38\n\x0bzoom_status\x18\x01 \x01(\x0e\x32#.sandwich.ToServerExtras.ZoomStatus\x12\x1e\n\x05state\x18\x02 \x01(\x0b\x32\x0f.sandwich.State\".\n\nZoomStatus\x12\x0b\n\x07NO_CALL\x10\x00\x12\t\n\x05START\x10\x01\x12\x08\n\x04STOP\x10\x02\"\xc9\x01\n\x0eToClientExtras\x12\x34\n\tzoom_info\x18\x01 \x01(\x0b\x32!.sandwich.ToClientExtras.ZoomInfo\x12\x1e\n\x05state\x18\x03 \x01(\x0b\x32\x0f.sandwich.State\x1a\x61\n\x08ZoomInfo\x12\x0f\n\x07\x61pp_key\x18\x01 \x01(\t\x12\x12\n\napp_secret\x18\x02 \x01(\t\x12\x16\n\x0emeeting_number\x18\x03 \x01(\t\x12\x18\n\x10meeting_password\x18\x04 \x01(\tB\x19\n\x0f\x65\x64u.cmu.cs.ikeaB\x06Protosb\x06proto3')
)



_STATE_STEP = _descriptor.EnumDescriptor(
  name='Step',
  full_name='sandwich.State.Step',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTHING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BASE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PIPE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHADE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUCKLE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACK_CIRCLE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHADE_BASE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BULB', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BULB_TOP', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=158,
  serialized_end=289,
)
_sym_db.RegisterEnumDescriptor(_STATE_STEP)

_TOSERVEREXTRAS_ZOOMSTATUS = _descriptor.EnumDescriptor(
  name='ZoomStatus',
  full_name='sandwich.ToServerExtras.ZoomStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CALL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=400,
  serialized_end=446,
)
_sym_db.RegisterEnumDescriptor(_TOSERVEREXTRAS_ZOOMSTATUS)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='sandwich.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_count', full_name='sandwich.State.update_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='sandwich.State.step', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frames_with_one_buckle', full_name='sandwich.State.frames_with_one_buckle', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frames_with_two_buckles', full_name='sandwich.State.frames_with_two_buckles', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATE_STEP,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=289,
)


_TOSERVEREXTRAS = _descriptor.Descriptor(
  name='ToServerExtras',
  full_name='sandwich.ToServerExtras',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zoom_status', full_name='sandwich.ToServerExtras.zoom_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='sandwich.ToServerExtras.state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TOSERVEREXTRAS_ZOOMSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=446,
)


_TOCLIENTEXTRAS_ZOOMINFO = _descriptor.Descriptor(
  name='ZoomInfo',
  full_name='sandwich.ToClientExtras.ZoomInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_key', full_name='sandwich.ToClientExtras.ZoomInfo.app_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_secret', full_name='sandwich.ToClientExtras.ZoomInfo.app_secret', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meeting_number', full_name='sandwich.ToClientExtras.ZoomInfo.meeting_number', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meeting_password', full_name='sandwich.ToClientExtras.ZoomInfo.meeting_password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=553,
  serialized_end=650,
)

_TOCLIENTEXTRAS = _descriptor.Descriptor(
  name='ToClientExtras',
  full_name='sandwich.ToClientExtras',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zoom_info', full_name='sandwich.ToClientExtras.zoom_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='sandwich.ToClientExtras.state', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TOCLIENTEXTRAS_ZOOMINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=449,
  serialized_end=650,
)

_STATE.fields_by_name['step'].enum_type = _STATE_STEP
_STATE_STEP.containing_type = _STATE
_TOSERVEREXTRAS.fields_by_name['zoom_status'].enum_type = _TOSERVEREXTRAS_ZOOMSTATUS
_TOSERVEREXTRAS.fields_by_name['state'].message_type = _STATE
_TOSERVEREXTRAS_ZOOMSTATUS.containing_type = _TOSERVEREXTRAS
_TOCLIENTEXTRAS_ZOOMINFO.containing_type = _TOCLIENTEXTRAS
_TOCLIENTEXTRAS.fields_by_name['zoom_info'].message_type = _TOCLIENTEXTRAS_ZOOMINFO
_TOCLIENTEXTRAS.fields_by_name['state'].message_type = _STATE
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['ToServerExtras'] = _TOSERVEREXTRAS
DESCRIPTOR.message_types_by_name['ToClientExtras'] = _TOCLIENTEXTRAS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
  'DESCRIPTOR' : _STATE,
  '__module__' : 'ikea_pb2'
  # @@protoc_insertion_point(class_scope:sandwich.State)
  })
_sym_db.RegisterMessage(State)

ToServerExtras = _reflection.GeneratedProtocolMessageType('ToServerExtras', (_message.Message,), {
  'DESCRIPTOR' : _TOSERVEREXTRAS,
  '__module__' : 'ikea_pb2'
  # @@protoc_insertion_point(class_scope:sandwich.ToServerExtras)
  })
_sym_db.RegisterMessage(ToServerExtras)

ToClientExtras = _reflection.GeneratedProtocolMessageType('ToClientExtras', (_message.Message,), {

  'ZoomInfo' : _reflection.GeneratedProtocolMessageType('ZoomInfo', (_message.Message,), {
    'DESCRIPTOR' : _TOCLIENTEXTRAS_ZOOMINFO,
    '__module__' : 'ikea_pb2'
    # @@protoc_insertion_point(class_scope:sandwich.ToClientExtras.ZoomInfo)
    })
  ,
  'DESCRIPTOR' : _TOCLIENTEXTRAS,
  '__module__' : 'ikea_pb2'
  # @@protoc_insertion_point(class_scope:sandwich.ToClientExtras)
  })
_sym_db.RegisterMessage(ToClientExtras)
_sym_db.RegisterMessage(ToClientExtras.ZoomInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
