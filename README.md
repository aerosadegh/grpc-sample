# grpc sample in python
This is a sample project of use gRPC 


### Run
#### 1. Prepare
```bash
# with poetry
poetry install 

# or with pip
pip install -r requirements.txt
```

#### 2. Server
```bash
cd server
python echo_server.py
```

#### 3. Client
```bash
cd client
python echo_client.py
```


### Use this project as template
If you want change proto files you can generate with sample code `generate.ps1` proto files in python on server and client directory
Note: you may need change `*_grpc.py` files and add `from .` before relative import(s) in them.

