python -m grpc_tools.protoc -I./proto --python_out=./server/protos --pyi_out=./server/protos --grpc_python_out=./server/protos .\proto\echo_msg.proto
python -m grpc_tools.protoc -I./proto --python_out=./client/protos --pyi_out=./client/protos --grpc_python_out=./client/protos .\proto\echo_msg.proto


Write-Host "NOTE: Please Add manualy 'from .' to the relative imports of *_grpc.py files"