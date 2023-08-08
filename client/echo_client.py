import logging
from random import randint

import grpc
from protos import echo_msg_pb2, echo_msg_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to send echo ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        # call  SayEcho
        stub = echo_msg_pb2_grpc.EchoStub(channel)
        response = stub.SayEcho(echo_msg_pb2.EchoRequest(message="hello grpc!"))
        print("Echo client received: " + response.rmessage)

        # call  Sum
        stub = echo_msg_pb2_grpc.EchoStub(channel)
        vector = [randint(5, 20) for _ in range(5)]
        response = stub.Sum(echo_msg_pb2.VectorNumber(vector=vector))
    logger.info(f"Send Calculation to server for: {vector}")
    logger.info(f"Echo client received: {response.value}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s(%(name)s) %(levelname)s - %(message)s",
    )
    logger = logging.getLogger(__file__.strip("\\/.py"))
    run()
