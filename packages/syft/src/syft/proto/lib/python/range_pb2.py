# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/range.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cproto/lib/python/range.proto\x12\x0fsyft.lib.python\x1a%proto/core/common/common_object.proto"U\n\x05Range\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0c\n\x04stop\x18\x02 \x01(\x03\x12\x0c\n\x04step\x18\x03 \x01(\x03\x12!\n\x02id\x18\x04 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "proto.lib.python.range_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _RANGE._serialized_start = 88
    _RANGE._serialized_end = 173
# @@protoc_insertion_point(module_scope)