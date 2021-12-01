# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/domain/service/request_handler_message.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2
from syft.proto.lib.python import dict_pb2 as proto_dot_lib_dot_python_dot_dict__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n<proto/core/node/domain/service/request_handler_message.proto\x12\x1dsyft.core.node.domain.service\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto\x1a\x1bproto/lib/python/dict.proto"\xa2\x01\n\x1bUpdateRequestHandlerMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12&\n\x07handler\x18\x03 \x01(\x0b\x32\x15.syft.lib.python.Dict\x12\x0c\n\x04keep\x18\x04 \x01(\x08"\x96\x01\n\x1cGetAllRequestHandlersMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address"\x9e\x01\n$GetAllRequestHandlersResponseMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08handlers\x18\x03 \x03(\x0b\x32\x15.syft.lib.python.Dictb\x06proto3'
)


_UPDATEREQUESTHANDLERMESSAGE = DESCRIPTOR.message_types_by_name[
    "UpdateRequestHandlerMessage"
]
_GETALLREQUESTHANDLERSMESSAGE = DESCRIPTOR.message_types_by_name[
    "GetAllRequestHandlersMessage"
]
_GETALLREQUESTHANDLERSRESPONSEMESSAGE = DESCRIPTOR.message_types_by_name[
    "GetAllRequestHandlersResponseMessage"
]
UpdateRequestHandlerMessage = _reflection.GeneratedProtocolMessageType(
    "UpdateRequestHandlerMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEREQUESTHANDLERMESSAGE,
        "__module__": "proto.core.node.domain.service.request_handler_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.domain.service.UpdateRequestHandlerMessage)
    },
)
_sym_db.RegisterMessage(UpdateRequestHandlerMessage)

GetAllRequestHandlersMessage = _reflection.GeneratedProtocolMessageType(
    "GetAllRequestHandlersMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLREQUESTHANDLERSMESSAGE,
        "__module__": "proto.core.node.domain.service.request_handler_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.domain.service.GetAllRequestHandlersMessage)
    },
)
_sym_db.RegisterMessage(GetAllRequestHandlersMessage)

GetAllRequestHandlersResponseMessage = _reflection.GeneratedProtocolMessageType(
    "GetAllRequestHandlersResponseMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLREQUESTHANDLERSRESPONSEMESSAGE,
        "__module__": "proto.core.node.domain.service.request_handler_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.domain.service.GetAllRequestHandlersResponseMessage)
    },
)
_sym_db.RegisterMessage(GetAllRequestHandlersResponseMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _UPDATEREQUESTHANDLERMESSAGE._serialized_start = 193
    _UPDATEREQUESTHANDLERMESSAGE._serialized_end = 355
    _GETALLREQUESTHANDLERSMESSAGE._serialized_start = 358
    _GETALLREQUESTHANDLERSMESSAGE._serialized_end = 508
    _GETALLREQUESTHANDLERSRESPONSEMESSAGE._serialized_start = 511
    _GETALLREQUESTHANDLERSRESPONSEMESSAGE._serialized_end = 669
# @@protoc_insertion_point(module_scope)