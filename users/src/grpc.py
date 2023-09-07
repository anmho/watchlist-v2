# from grpc import insecure_channel
# from threading import 


from typing import Annotated
from .proto.user_pb2 import User, CreateUserRequest, CreateUserResponse
from .rest import UserCreate
from concurrent import futures
from .proto import user_pb2_grpc
from .services import users
import logging
import grpc 
from fastapi import Depends


class UserService(user_pb2_grpc.UsersServicer):
    def __init__(self, userService=users.UserService()):
        self.userService = userService
        
    def CreateUser(self, request: CreateUserRequest, context) -> CreateUserResponse:
        logging.info(self.userService)
        user = self.userService.create_user(email=request.email)
        logging.info(user)
        # return user
        return CreateUserResponse(user=user)


def serve():
    server: grpc.Server = grpc.server(futures.ThreadPoolExecutor(10))

    address = "127.0.0.1:50051"
    server.add_insecure_port(address)

    logging.info(f"Starting server on {address}...")

    # Add Servicers
    user_pb2_grpc.add_UsersServicer_to_server(UserService(), server)
    server.start()
    server.wait_for_termination()

    logging.info(f"Server shutting down...")







