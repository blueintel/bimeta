# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import github_pb2 as github__pb2


class GithubServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAlerts = channel.unary_stream(
                '/blueintel.badapi.github.GithubService/ListAlerts',
                request_serializer=github__pb2.ListAlertsRequest.SerializeToString,
                response_deserializer=github__pb2.Alert.FromString,
                )


class GithubServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListAlerts(self, request, context):
        """rpc ListRepos(ListReposRequest) returns (stream ListReposResponse) {};
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GithubServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListAlerts': grpc.unary_stream_rpc_method_handler(
                    servicer.ListAlerts,
                    request_deserializer=github__pb2.ListAlertsRequest.FromString,
                    response_serializer=github__pb2.Alert.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueintel.badapi.github.GithubService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GithubService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListAlerts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueintel.badapi.github.GithubService/ListAlerts',
            github__pb2.ListAlertsRequest.SerializeToString,
            github__pb2.Alert.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
