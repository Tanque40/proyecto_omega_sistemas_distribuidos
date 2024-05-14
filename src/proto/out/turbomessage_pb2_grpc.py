# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src.proto import turbomessage_pb2 as src_dot_proto_dot_turbomessage__pb2


class AuthenticatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.new_user = channel.unary_unary(
                '/turbomessage.Authenticator/new_user',
                request_serializer=src_dot_proto_dot_turbomessage__pb2.New_User_Data.SerializeToString,
                response_deserializer=src_dot_proto_dot_turbomessage__pb2.Status.FromString,
                )
        self.authenticate = channel.unary_unary(
                '/turbomessage.Authenticator/authenticate',
                request_serializer=src_dot_proto_dot_turbomessage__pb2.User_Data.SerializeToString,
                response_deserializer=src_dot_proto_dot_turbomessage__pb2.Status.FromString,
                )


class AuthenticatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def new_user(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def authenticate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthenticatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'new_user': grpc.unary_unary_rpc_method_handler(
                    servicer.new_user,
                    request_deserializer=src_dot_proto_dot_turbomessage__pb2.New_User_Data.FromString,
                    response_serializer=src_dot_proto_dot_turbomessage__pb2.Status.SerializeToString,
            ),
            'authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.authenticate,
                    request_deserializer=src_dot_proto_dot_turbomessage__pb2.User_Data.FromString,
                    response_serializer=src_dot_proto_dot_turbomessage__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'turbomessage.Authenticator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Authenticator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def new_user(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/turbomessage.Authenticator/new_user',
            src_dot_proto_dot_turbomessage__pb2.New_User_Data.SerializeToString,
            src_dot_proto_dot_turbomessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/turbomessage.Authenticator/authenticate',
            src_dot_proto_dot_turbomessage__pb2.User_Data.SerializeToString,
            src_dot_proto_dot_turbomessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class EmailServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send_email = channel.unary_unary(
                '/turbomessage.EmailServer/send_email',
                request_serializer=src_dot_proto_dot_turbomessage__pb2.Email_Data.SerializeToString,
                response_deserializer=src_dot_proto_dot_turbomessage__pb2.Status.FromString,
                )
        self.recive_emails = channel.unary_stream(
                '/turbomessage.EmailServer/recive_emails',
                request_serializer=src_dot_proto_dot_turbomessage__pb2.User_Email.SerializeToString,
                response_deserializer=src_dot_proto_dot_turbomessage__pb2.Email_Response.FromString,
                )
        self.mark_as_read = channel.unary_unary(
                '/turbomessage.EmailServer/mark_as_read',
                request_serializer=src_dot_proto_dot_turbomessage__pb2.Email_Data.SerializeToString,
                response_deserializer=src_dot_proto_dot_turbomessage__pb2.Status.FromString,
                )


class EmailServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def send_email(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recive_emails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mark_as_read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmailServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'send_email': grpc.unary_unary_rpc_method_handler(
                    servicer.send_email,
                    request_deserializer=src_dot_proto_dot_turbomessage__pb2.Email_Data.FromString,
                    response_serializer=src_dot_proto_dot_turbomessage__pb2.Status.SerializeToString,
            ),
            'recive_emails': grpc.unary_stream_rpc_method_handler(
                    servicer.recive_emails,
                    request_deserializer=src_dot_proto_dot_turbomessage__pb2.User_Email.FromString,
                    response_serializer=src_dot_proto_dot_turbomessage__pb2.Email_Response.SerializeToString,
            ),
            'mark_as_read': grpc.unary_unary_rpc_method_handler(
                    servicer.mark_as_read,
                    request_deserializer=src_dot_proto_dot_turbomessage__pb2.Email_Data.FromString,
                    response_serializer=src_dot_proto_dot_turbomessage__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'turbomessage.EmailServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EmailServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def send_email(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/turbomessage.EmailServer/send_email',
            src_dot_proto_dot_turbomessage__pb2.Email_Data.SerializeToString,
            src_dot_proto_dot_turbomessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def recive_emails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/turbomessage.EmailServer/recive_emails',
            src_dot_proto_dot_turbomessage__pb2.User_Email.SerializeToString,
            src_dot_proto_dot_turbomessage__pb2.Email_Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def mark_as_read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/turbomessage.EmailServer/mark_as_read',
            src_dot_proto_dot_turbomessage__pb2.Email_Data.SerializeToString,
            src_dot_proto_dot_turbomessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)