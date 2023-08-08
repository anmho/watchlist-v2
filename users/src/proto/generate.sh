#!/bin/bash
# python3 -m grpc_tools.protoc -I ../protobufs --python_out=./src/protos --pyi_out=./src/protos --grpc_python_out=./src/protos ../protobufs/user.proto 

python3 -m grpc_tools.protoc -I ../../../protobufs --python_out=. --grpc_python_out=. ../../../protobufs/user.proto

# sed -i '' 's/^\(import [^ ]*_pb2\) as \([^ ]*__pb2\)/from . \1 as \2/' ./src/protos/*_pb2_grpc.py


protol \
  --create-package \
  --in-place \
  --python-out . \
  protoc --proto-path=../../../protobufs user.proto


