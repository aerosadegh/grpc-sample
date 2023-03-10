# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import echo_msg_pb2 as echo__msg__pb2


class EchoStub(object):
    """The echo service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayEcho = channel.unary_unary(
                '/Echo/SayEcho',
                request_serializer=echo__msg__pb2.EchoRequest.SerializeToString,
                response_deserializer=echo__msg__pb2.EchoReply.FromString,
                )
        self.Sum = channel.unary_unary(
                '/Echo/Sum',
                request_serializer=echo__msg__pb2.VectorNumber.SerializeToString,
                response_deserializer=echo__msg__pb2.ValueNumber.FromString,
                )


class EchoServicer(object):
    """The echo service definition.
    """

    def SayEcho(self, request, context):
        """Sends a message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sum(self, request, context):
        """Sends a number
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EchoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayEcho': grpc.unary_unary_rpc_method_handler(
                    servicer.SayEcho,
                    request_deserializer=echo__msg__pb2.EchoRequest.FromString,
                    response_serializer=echo__msg__pb2.EchoReply.SerializeToString,
            ),
            'Sum': grpc.unary_unary_rpc_method_handler(
                    servicer.Sum,
                    request_deserializer=echo__msg__pb2.VectorNumber.FromString,
                    response_serializer=echo__msg__pb2.ValueNumber.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Echo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Echo(object):
    """The echo service definition.
    """

    @staticmethod
    def SayEcho(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Echo/SayEcho',
            echo__msg__pb2.EchoRequest.SerializeToString,
            echo__msg__pb2.EchoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Echo/Sum',
            echo__msg__pb2.VectorNumber.SerializeToString,
            echo__msg__pb2.ValueNumber.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
