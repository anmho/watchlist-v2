#!/bin/bash

uvicorn main:app --reload & python3 start_grpc.py