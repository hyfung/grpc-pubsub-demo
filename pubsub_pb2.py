# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pubsub.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpubsub.proto\" \n\x10SubscribeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x07Message\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"9\n\x0fPublishResponse\x12&\n\x06status\x18\x01 \x01(\x0e\x32\x16.PublishResponseStatus*=\n\x15PublishResponseStatus\x12\x08\n\x04VOID\x10\x00\x12\x0b\n\x07SUCCEED\x10\x01\x12\r\n\tNOT_FOUND\x10\x02\x32[\n\x06PubSub\x12*\n\tSubscribe\x12\x11.SubscribeRequest\x1a\x08.Message0\x01\x12%\n\x07Publish\x12\x08.Message\x1a\x10.PublishResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pubsub_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PUBLISHRESPONSESTATUS']._serialized_start=148
  _globals['_PUBLISHRESPONSESTATUS']._serialized_end=209
  _globals['_SUBSCRIBEREQUEST']._serialized_start=16
  _globals['_SUBSCRIBEREQUEST']._serialized_end=48
  _globals['_MESSAGE']._serialized_start=50
  _globals['_MESSAGE']._serialized_end=87
  _globals['_PUBLISHRESPONSE']._serialized_start=89
  _globals['_PUBLISHRESPONSE']._serialized_end=146
  _globals['_PUBSUB']._serialized_start=211
  _globals['_PUBSUB']._serialized_end=302
# @@protoc_insertion_point(module_scope)