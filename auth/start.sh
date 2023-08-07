#!/bin/bash


python -m src.models.create_tables

# Run the gRPC server

python main.py