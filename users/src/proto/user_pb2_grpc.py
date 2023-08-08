"""Client and server classes corresponding to protobuf-defined services."""
import app_grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import user_pb2 as user__pb2

class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary('/UserService/CreateUser', request_serializer=user__pb2.CreateUserRequest.SerializeToString, response_deserializer=user__pb2.CreateUserResponse.FromString)
        self.ReadUser = channel.unary_unary('/UserService/ReadUser', request_serializer=user__pb2.ReadUserRequest.SerializeToString, response_deserializer=user__pb2.ReadUserResponse.FromString)
        self.UpdateUser = channel.unary_unary('/UserService/UpdateUser', request_serializer=user__pb2.UpdateUserRequest.SerializeToString, response_deserializer=user__pb2.UpdateUserResponse.FromString)
        self.DeleteUser = channel.unary_unary('/UserService/DeleteUser', request_serializer=user__pb2.DeleteUserRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString)

class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(app_grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(app_grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(app_grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(app_grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateUser': app_grpc.unary_unary_rpc_method_handler(servicer.CreateUser, request_deserializer=user__pb2.CreateUserRequest.FromString, response_serializer=user__pb2.CreateUserResponse.SerializeToString), 'ReadUser': app_grpc.unary_unary_rpc_method_handler(servicer.ReadUser, request_deserializer=user__pb2.ReadUserRequest.FromString, response_serializer=user__pb2.ReadUserResponse.SerializeToString), 'UpdateUser': app_grpc.unary_unary_rpc_method_handler(servicer.UpdateUser, request_deserializer=user__pb2.UpdateUserRequest.FromString, response_serializer=user__pb2.UpdateUserResponse.SerializeToString), 'DeleteUser': app_grpc.unary_unary_rpc_method_handler(servicer.DeleteUser, request_deserializer=user__pb2.DeleteUserRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString)}
    generic_handler = app_grpc.method_handlers_generic_handler('UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return app_grpc.experimental.unary_unary(request, target, '/UserService/CreateUser', user__pb2.CreateUserRequest.SerializeToString, user__pb2.CreateUserResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return app_grpc.experimental.unary_unary(request, target, '/UserService/ReadUser', user__pb2.ReadUserRequest.SerializeToString, user__pb2.ReadUserResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return app_grpc.experimental.unary_unary(request, target, '/UserService/UpdateUser', user__pb2.UpdateUserRequest.SerializeToString, user__pb2.UpdateUserResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return app_grpc.experimental.unary_unary(request, target, '/UserService/DeleteUser', user__pb2.DeleteUserRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)