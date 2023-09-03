#!/bin/bash

python3 -m grpc_tools.protoc -I ../../../protobufs --python_out=. --grpc_python_out=. ../../../protobufs/user.proto

protol \
  --create-package \
  --in-place \
  --python-out . \
  protoc --proto-path=../../../protobufs user.proto


