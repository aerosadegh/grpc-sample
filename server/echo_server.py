import logging
from concurrent import futures

import grpc
from protos import echo_msg_pb2, echo_msg_pb2_grpc


class Echo(echo_msg_pb2_grpc.EchoServicer):
    def SayEcho(self, request, context):
      return echo_msg_pb2.EchoReply(rmessage=f"got {request.message!r}")

    def Sum(self, request: echo_msg_pb2.VectorNumber, context):
      logging.debug(f"{request.vector}")
      return echo_msg_pb2.ValueNumber(value=sum(item for item in request.vector))


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_msg_pb2_grpc.add_EchoServicer_to_server(Echo(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    serve()