# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import badapiuser_pb2 as badapiuser__pb2


class BadAPIUserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/blueintel.badapi.badapiuser.BadAPIUserService/CreateUser',
                request_serializer=badapiuser__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=badapiuser__pb2.CreateUserResponse.FromString,
                )
        self.ReadUserByAPIKey = channel.unary_unary(
                '/blueintel.badapi.badapiuser.BadAPIUserService/ReadUserByAPIKey',
                request_serializer=badapiuser__pb2.ReadUserByAPIKeyRequest.SerializeToString,
                response_deserializer=badapiuser__pb2.ReadUserResponse.FromString,
                )
        self.ReadUserByID = channel.unary_unary(
                '/blueintel.badapi.badapiuser.BadAPIUserService/ReadUserByID',
                request_serializer=badapiuser__pb2.ReadUserByIDRequest.SerializeToString,
                response_deserializer=badapiuser__pb2.ReadUserResponse.FromString,
                )
        self.ReadUserByEmail = channel.unary_unary(
                '/blueintel.badapi.badapiuser.BadAPIUserService/ReadUserByEmail',
                request_serializer=badapiuser__pb2.ReadUserByEmailRequest.SerializeToString,
                response_deserializer=badapiuser__pb2.ReadUserResponse.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/blueintel.badapi.badapiuser.BadAPIUserService/UpdateUser',
                request_serializer=badapiuser__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=badapiuser__pb2.UpdateUserResponse.FromString,
                )
        self.DeleteUserByID = channel.unary_unary(
                '/blueintel.badapi.badapiuser.BadAPIUserService/DeleteUserByID',
                request_serializer=badapiuser__pb2.DeleteUserByIDRequest.SerializeToString,
                response_deserializer=badapiuser__pb2.BadAPIUserEmpty.FromString,
                )
        self.DeleteUserByEmail = channel.unary_unary(
                '/blueintel.badapi.badapiuser.BadAPIUserService/DeleteUserByEmail',
                request_serializer=badapiuser__pb2.DeleteUserByEmailRequest.SerializeToString,
                response_deserializer=badapiuser__pb2.BadAPIUserEmpty.FromString,
                )
        self.ListUsers = channel.unary_stream(
                '/blueintel.badapi.badapiuser.BadAPIUserService/ListUsers',
                request_serializer=badapiuser__pb2.ListUsersRequest.SerializeToString,
                response_deserializer=badapiuser__pb2.ListUsersResponse.FromString,
                )
        self.ListUsersByDomain = channel.unary_stream(
                '/blueintel.badapi.badapiuser.BadAPIUserService/ListUsersByDomain',
                request_serializer=badapiuser__pb2.ListUsersByDomainRequest.SerializeToString,
                response_deserializer=badapiuser__pb2.ListUsersResponse.FromString,
                )


class BadAPIUserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadUserByAPIKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadUserByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadUserByEmail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """UpdateUser updates a User identified by the passed in id. Only updated fields need to be passed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUserByID(self, request, context):
        """DeleteUserByID deletes a User using the passed in id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUserByEmail(self, request, context):
        """DeleteUserByEmail deletes a User using the passed in email
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsers(self, request, context):
        """ListUsers lists all Users for a specific org.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsersByDomain(self, request, context):
        """ListUsersByEmail searches for user by email domain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BadAPIUserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=badapiuser__pb2.CreateUserRequest.FromString,
                    response_serializer=badapiuser__pb2.CreateUserResponse.SerializeToString,
            ),
            'ReadUserByAPIKey': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadUserByAPIKey,
                    request_deserializer=badapiuser__pb2.ReadUserByAPIKeyRequest.FromString,
                    response_serializer=badapiuser__pb2.ReadUserResponse.SerializeToString,
            ),
            'ReadUserByID': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadUserByID,
                    request_deserializer=badapiuser__pb2.ReadUserByIDRequest.FromString,
                    response_serializer=badapiuser__pb2.ReadUserResponse.SerializeToString,
            ),
            'ReadUserByEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadUserByEmail,
                    request_deserializer=badapiuser__pb2.ReadUserByEmailRequest.FromString,
                    response_serializer=badapiuser__pb2.ReadUserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=badapiuser__pb2.UpdateUserRequest.FromString,
                    response_serializer=badapiuser__pb2.UpdateUserResponse.SerializeToString,
            ),
            'DeleteUserByID': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUserByID,
                    request_deserializer=badapiuser__pb2.DeleteUserByIDRequest.FromString,
                    response_serializer=badapiuser__pb2.BadAPIUserEmpty.SerializeToString,
            ),
            'DeleteUserByEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUserByEmail,
                    request_deserializer=badapiuser__pb2.DeleteUserByEmailRequest.FromString,
                    response_serializer=badapiuser__pb2.BadAPIUserEmpty.SerializeToString,
            ),
            'ListUsers': grpc.unary_stream_rpc_method_handler(
                    servicer.ListUsers,
                    request_deserializer=badapiuser__pb2.ListUsersRequest.FromString,
                    response_serializer=badapiuser__pb2.ListUsersResponse.SerializeToString,
            ),
            'ListUsersByDomain': grpc.unary_stream_rpc_method_handler(
                    servicer.ListUsersByDomain,
                    request_deserializer=badapiuser__pb2.ListUsersByDomainRequest.FromString,
                    response_serializer=badapiuser__pb2.ListUsersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueintel.badapi.badapiuser.BadAPIUserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BadAPIUserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.badapiuser.BadAPIUserService/CreateUser',
            badapiuser__pb2.CreateUserRequest.SerializeToString,
            badapiuser__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadUserByAPIKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.badapiuser.BadAPIUserService/ReadUserByAPIKey',
            badapiuser__pb2.ReadUserByAPIKeyRequest.SerializeToString,
            badapiuser__pb2.ReadUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadUserByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.badapiuser.BadAPIUserService/ReadUserByID',
            badapiuser__pb2.ReadUserByIDRequest.SerializeToString,
            badapiuser__pb2.ReadUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadUserByEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.badapiuser.BadAPIUserService/ReadUserByEmail',
            badapiuser__pb2.ReadUserByEmailRequest.SerializeToString,
            badapiuser__pb2.ReadUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.badapiuser.BadAPIUserService/UpdateUser',
            badapiuser__pb2.UpdateUserRequest.SerializeToString,
            badapiuser__pb2.UpdateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUserByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.badapiuser.BadAPIUserService/DeleteUserByID',
            badapiuser__pb2.DeleteUserByIDRequest.SerializeToString,
            badapiuser__pb2.BadAPIUserEmpty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUserByEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.badapiuser.BadAPIUserService/DeleteUserByEmail',
            badapiuser__pb2.DeleteUserByEmailRequest.SerializeToString,
            badapiuser__pb2.BadAPIUserEmpty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueintel.badapi.badapiuser.BadAPIUserService/ListUsers',
            badapiuser__pb2.ListUsersRequest.SerializeToString,
            badapiuser__pb2.ListUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsersByDomain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueintel.badapi.badapiuser.BadAPIUserService/ListUsersByDomain',
            badapiuser__pb2.ListUsersByDomainRequest.SerializeToString,
            badapiuser__pb2.ListUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
