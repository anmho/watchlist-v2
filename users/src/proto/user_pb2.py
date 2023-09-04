"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x1a\x1bgoogle/protobuf/empty.proto"!\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05email\x18\x02 \x01(\t"F\n\x11CreateUserRequest\x12\r\n\x05email\x18\x01 \x01(\t\x12\x15\n\x08password\x18\x03 \x01(\tH\x00\x88\x01\x01B\x0b\n\t_password")\n\x12CreateUserResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b2\x05.User" \n\x0fReadUserRequest\x12\r\n\x05email\x18\x01 \x01(\t"\'\n\x10ReadUserResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b2\x05.User"0\n\x11UpdateUserRequest\x12\x1b\n\x0cupdated_user\x18\x01 \x01(\x0b2\x05.User"1\n\x12UpdateUserResponse\x12\x1b\n\x0cupdated_user\x18\x01 \x01(\x0b2\x05.User""\n\x11DeleteUserRequest\x12\r\n\x05email\x18\x01 \x01(\t"6\n\x12DeleteUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xe0\x01\n\x05Users\x125\n\nCreateUser\x12\x12.CreateUserRequest\x1a\x13.CreateUserResponse\x12/\n\x08ReadUser\x12\x10.ReadUserRequest\x1a\x11.ReadUserResponse\x125\n\nUpdateUser\x12\x12.UpdateUserRequest\x1a\x13.UpdateUserResponse\x128\n\nDeleteUser\x12\x12.DeleteUserRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_USER']._serialized_start = 43
    _globals['_USER']._serialized_end = 76
    _globals['_CREATEUSERREQUEST']._serialized_start = 78
    _globals['_CREATEUSERREQUEST']._serialized_end = 148
    _globals['_CREATEUSERRESPONSE']._serialized_start = 150
    _globals['_CREATEUSERRESPONSE']._serialized_end = 191
    _globals['_READUSERREQUEST']._serialized_start = 193
    _globals['_READUSERREQUEST']._serialized_end = 225
    _globals['_READUSERRESPONSE']._serialized_start = 227
    _globals['_READUSERRESPONSE']._serialized_end = 266
    _globals['_UPDATEUSERREQUEST']._serialized_start = 268
    _globals['_UPDATEUSERREQUEST']._serialized_end = 316
    _globals['_UPDATEUSERRESPONSE']._serialized_start = 318
    _globals['_UPDATEUSERRESPONSE']._serialized_end = 367
    _globals['_DELETEUSERREQUEST']._serialized_start = 369
    _globals['_DELETEUSERREQUEST']._serialized_end = 403
    _globals['_DELETEUSERRESPONSE']._serialized_start = 405
    _globals['_DELETEUSERRESPONSE']._serialized_end = 459
    _globals['_USERS']._serialized_start = 462
    _globals['_USERS']._serialized_end = 686