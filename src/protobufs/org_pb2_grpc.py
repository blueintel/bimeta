# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobufs import org_pb2 as org__pb2


class BimetaOrgServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBimetaOrg = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/CreateBimetaOrg',
            request_serializer=org__pb2.CreateBimetaOrgRequest.SerializeToString,
            response_deserializer=org__pb2.CreateBimetaOrgResponse.FromString,
        )
        self.ReadBimetaOrgByID = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/ReadBimetaOrgByID',
            request_serializer=org__pb2.ReadBimetaOrgByIDRequest.SerializeToString,
            response_deserializer=org__pb2.ReadBimetaOrgResponse.FromString,
        )
        self.ReadBimetaOrgByName = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/ReadBimetaOrgByName',
            request_serializer=org__pb2.ReadBimetaOrgByNameRequest.SerializeToString,
            response_deserializer=org__pb2.ReadBimetaOrgResponse.FromString,
        )
        self.UpdateBimetaOrg = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/UpdateBimetaOrg',
            request_serializer=org__pb2.UpdateBimetaOrgRequest.SerializeToString,
            response_deserializer=org__pb2.UpdateBimetaOrgResponse.FromString,
        )
        self.DeleteBimetaOrgByID = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgByID',
            request_serializer=org__pb2.DeleteBimetaOrgByIDRequest.SerializeToString,
            response_deserializer=org__pb2.BimetaOrgEmpty.FromString,
        )
        self.DeleteBimetaOrgByName = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgByName',
            request_serializer=org__pb2.DeleteBimetaOrgByNameRequest.SerializeToString,
            response_deserializer=org__pb2.BimetaOrgEmpty.FromString,
        )
        self.ListBimetaOrgsByClass = channel.unary_stream(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/ListBimetaOrgsByClass',
            request_serializer=org__pb2.ListBimetaOrgsByClassRequest.SerializeToString,
            response_deserializer=org__pb2.ListBimetaOrgsResponse.FromString,
        )
        self.CreateBimetaOrgTag = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/CreateBimetaOrgTag',
            request_serializer=org__pb2.CreateBimetaOrgTagRequest.SerializeToString,
            response_deserializer=org__pb2.CreateBimetaOrgTagResponse.FromString,
        )
        self.DeleteBimetaOrgTag = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgTag',
            request_serializer=org__pb2.DeleteBimetaOrgTagRequest.SerializeToString,
            response_deserializer=org__pb2.BimetaOrgTagEmpty.FromString,
        )
        self.ListBimetaOrgTag = channel.unary_stream(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/ListBimetaOrgTag',
            request_serializer=org__pb2.ListBimetaOrgTagRequest.SerializeToString,
            response_deserializer=org__pb2.ListBimetaOrgTagResponse.FromString,
        )
        self.CreateBimetaOrgConfig = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/CreateBimetaOrgConfig',
            request_serializer=org__pb2.CreateBimetaOrgConfigRequest.SerializeToString,
            response_deserializer=org__pb2.CreateBimetaOrgConfigResponse.FromString,
        )
        self.UpdateBimetaOrgConfig = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/UpdateBimetaOrgConfig',
            request_serializer=org__pb2.UpdateBimetaOrgConfigRequest.SerializeToString,
            response_deserializer=org__pb2.UpdateBimetaOrgConfigResponse.FromString,
        )
        self.ReadBimetaOrgConfig = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/ReadBimetaOrgConfig',
            request_serializer=org__pb2.ReadBimetaOrgConfigRequest.SerializeToString,
            response_deserializer=org__pb2.ReadBimetaOrgConfigResponse.FromString,
        )
        self.DeleteBimetaOrgConfig = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgConfig',
            request_serializer=org__pb2.DeleteBimetaOrgConfigRequest.SerializeToString,
            response_deserializer=org__pb2.BimetaOrgConfigEmpty.FromString,
        )
        self.CreateBimetaOrgCIDR = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/CreateBimetaOrgCIDR',
            request_serializer=org__pb2.CreateBimetaOrgCIDRRequest.SerializeToString,
            response_deserializer=org__pb2.CreateBimetaOrgCIDRResponse.FromString,
        )
        self.DeleteBimetaOrgCIDR = channel.unary_unary(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgCIDR',
            request_serializer=org__pb2.DeleteBimetaOrgCIDRRequest.SerializeToString,
            response_deserializer=org__pb2.BimetaOrgCIDREmpty.FromString,
        )
        self.ListBimetaOrgCIDR = channel.unary_stream(
            '/blueintel.badapi.bimetaorg.BimetaOrgService/ListBimetaOrgCIDR',
            request_serializer=org__pb2.ListBimetaOrgCIDRRequest.SerializeToString,
            response_deserializer=org__pb2.ListBimetaOrgCIDRResponse.FromString,
        )


class BimetaOrgServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateBimetaOrg(self, request, context):
        """CreateBimetaOrg creates a new bimeta org record. The new id for the org
        is returned in the response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadBimetaOrgByID(self, request, context):
        """ReadBimetaOrgByID reads a BimetaOrg using the passed in id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadBimetaOrgByName(self, request, context):
        """ReadBimetaOrgByName reads a BimetaOrg using the passed in name
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBimetaOrg(self, request, context):
        """UpdateBimetaOrg updates the org identified by the passed in id. Can be used to
        rename the org and/or change the class of the org as well as the comment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBimetaOrgByID(self, request, context):
        """DeleteBimetaOrgByID deletes the org using the passed in id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBimetaOrgByName(self, request, context):
        """DeleteBimetaOrgByName deletes the org using the passed in name
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBimetaOrgsByClass(self, request, context):
        """ListBimetaOrgsByClass lists all BimetaOrgs for a specific org class.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBimetaOrgTag(self, request, context):
        """CreateBimetaOrgTag creates a new bimeta org tag record.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBimetaOrgTag(self, request, context):
        """DeleteBimetaOrgTag deletes a bimeta org tag record.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBimetaOrgTag(self, request, context):
        """ListBimetaOrgTag lists all BimetaOrgTags for a specific org.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBimetaOrgConfig(self, request, context):
        """CreateBimetaOrgConfig creates a new bimeta org config record.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBimetaOrgConfig(self, request, context):
        """UpdateBimetaOrgConfig updates a bimeta org config record.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadBimetaOrgConfig(self, request, context):
        """ReadBimetaOrgConfig reads config info
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBimetaOrgConfig(self, request, context):
        """DeleteBimetaOrgConfig deletes a bimeta org config record.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBimetaOrgCIDR(self, request, context):
        """CreateBimetaOrgCIDR creates a new bimeta org cidr record.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBimetaOrgCIDR(self, request, context):
        """DeleteBimetaOrgCIDR deletes a bimeta org cidr record.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBimetaOrgCIDR(self, request, context):
        """ListBimetaOrgCIDR lists all BimetaOrgIPs for a specific org.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BimetaOrgServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreateBimetaOrg': grpc.unary_unary_rpc_method_handler(
            servicer.CreateBimetaOrg,
            request_deserializer=org__pb2.CreateBimetaOrgRequest.FromString,
            response_serializer=org__pb2.CreateBimetaOrgResponse.SerializeToString,
        ),
        'ReadBimetaOrgByID': grpc.unary_unary_rpc_method_handler(
            servicer.ReadBimetaOrgByID,
            request_deserializer=org__pb2.ReadBimetaOrgByIDRequest.FromString,
            response_serializer=org__pb2.ReadBimetaOrgResponse.SerializeToString,
        ),
        'ReadBimetaOrgByName': grpc.unary_unary_rpc_method_handler(
            servicer.ReadBimetaOrgByName,
            request_deserializer=org__pb2.ReadBimetaOrgByNameRequest.FromString,
            response_serializer=org__pb2.ReadBimetaOrgResponse.SerializeToString,
        ),
        'UpdateBimetaOrg': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateBimetaOrg,
            request_deserializer=org__pb2.UpdateBimetaOrgRequest.FromString,
            response_serializer=org__pb2.UpdateBimetaOrgResponse.SerializeToString,
        ),
        'DeleteBimetaOrgByID': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBimetaOrgByID,
            request_deserializer=org__pb2.DeleteBimetaOrgByIDRequest.FromString,
            response_serializer=org__pb2.BimetaOrgEmpty.SerializeToString,
        ),
        'DeleteBimetaOrgByName': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBimetaOrgByName,
            request_deserializer=org__pb2.DeleteBimetaOrgByNameRequest.FromString,
            response_serializer=org__pb2.BimetaOrgEmpty.SerializeToString,
        ),
        'ListBimetaOrgsByClass': grpc.unary_stream_rpc_method_handler(
            servicer.ListBimetaOrgsByClass,
            request_deserializer=org__pb2.ListBimetaOrgsByClassRequest.FromString,
            response_serializer=org__pb2.ListBimetaOrgsResponse.SerializeToString,
        ),
        'CreateBimetaOrgTag': grpc.unary_unary_rpc_method_handler(
            servicer.CreateBimetaOrgTag,
            request_deserializer=org__pb2.CreateBimetaOrgTagRequest.FromString,
            response_serializer=org__pb2.CreateBimetaOrgTagResponse.SerializeToString,
        ),
        'DeleteBimetaOrgTag': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBimetaOrgTag,
            request_deserializer=org__pb2.DeleteBimetaOrgTagRequest.FromString,
            response_serializer=org__pb2.BimetaOrgTagEmpty.SerializeToString,
        ),
        'ListBimetaOrgTag': grpc.unary_stream_rpc_method_handler(
            servicer.ListBimetaOrgTag,
            request_deserializer=org__pb2.ListBimetaOrgTagRequest.FromString,
            response_serializer=org__pb2.ListBimetaOrgTagResponse.SerializeToString,
        ),
        'CreateBimetaOrgConfig': grpc.unary_unary_rpc_method_handler(
            servicer.CreateBimetaOrgConfig,
            request_deserializer=org__pb2.CreateBimetaOrgConfigRequest.FromString,
            response_serializer=org__pb2.CreateBimetaOrgConfigResponse.SerializeToString,
        ),
        'UpdateBimetaOrgConfig': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateBimetaOrgConfig,
            request_deserializer=org__pb2.UpdateBimetaOrgConfigRequest.FromString,
            response_serializer=org__pb2.UpdateBimetaOrgConfigResponse.SerializeToString,
        ),
        'ReadBimetaOrgConfig': grpc.unary_unary_rpc_method_handler(
            servicer.ReadBimetaOrgConfig,
            request_deserializer=org__pb2.ReadBimetaOrgConfigRequest.FromString,
            response_serializer=org__pb2.ReadBimetaOrgConfigResponse.SerializeToString,
        ),
        'DeleteBimetaOrgConfig': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBimetaOrgConfig,
            request_deserializer=org__pb2.DeleteBimetaOrgConfigRequest.FromString,
            response_serializer=org__pb2.BimetaOrgConfigEmpty.SerializeToString,
        ),
        'CreateBimetaOrgCIDR': grpc.unary_unary_rpc_method_handler(
            servicer.CreateBimetaOrgCIDR,
            request_deserializer=org__pb2.CreateBimetaOrgCIDRRequest.FromString,
            response_serializer=org__pb2.CreateBimetaOrgCIDRResponse.SerializeToString,
        ),
        'DeleteBimetaOrgCIDR': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBimetaOrgCIDR,
            request_deserializer=org__pb2.DeleteBimetaOrgCIDRRequest.FromString,
            response_serializer=org__pb2.BimetaOrgCIDREmpty.SerializeToString,
        ),
        'ListBimetaOrgCIDR': grpc.unary_stream_rpc_method_handler(
            servicer.ListBimetaOrgCIDR,
            request_deserializer=org__pb2.ListBimetaOrgCIDRRequest.FromString,
            response_serializer=org__pb2.ListBimetaOrgCIDRResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'blueintel.badapi.bimetaorg.BimetaOrgService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class BimetaOrgService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateBimetaOrg(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/CreateBimetaOrg',
                                             org__pb2.CreateBimetaOrgRequest.SerializeToString,
                                             org__pb2.CreateBimetaOrgResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadBimetaOrgByID(request,
                          target,
                          options=(),
                          channel_credentials=None,
                          call_credentials=None,
                          insecure=False,
                          compression=None,
                          wait_for_ready=None,
                          timeout=None,
                          metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/ReadBimetaOrgByID',
                                             org__pb2.ReadBimetaOrgByIDRequest.SerializeToString,
                                             org__pb2.ReadBimetaOrgResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadBimetaOrgByName(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/ReadBimetaOrgByName',
                                             org__pb2.ReadBimetaOrgByNameRequest.SerializeToString,
                                             org__pb2.ReadBimetaOrgResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBimetaOrg(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/UpdateBimetaOrg',
                                             org__pb2.UpdateBimetaOrgRequest.SerializeToString,
                                             org__pb2.UpdateBimetaOrgResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBimetaOrgByID(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgByID',
                                             org__pb2.DeleteBimetaOrgByIDRequest.SerializeToString,
                                             org__pb2.BimetaOrgEmpty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBimetaOrgByName(request,
                              target,
                              options=(),
                              channel_credentials=None,
                              call_credentials=None,
                              insecure=False,
                              compression=None,
                              wait_for_ready=None,
                              timeout=None,
                              metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgByName',
                                             org__pb2.DeleteBimetaOrgByNameRequest.SerializeToString,
                                             org__pb2.BimetaOrgEmpty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBimetaOrgsByClass(request,
                              target,
                              options=(),
                              channel_credentials=None,
                              call_credentials=None,
                              insecure=False,
                              compression=None,
                              wait_for_ready=None,
                              timeout=None,
                              metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/ListBimetaOrgsByClass',
                                              org__pb2.ListBimetaOrgsByClassRequest.SerializeToString,
                                              org__pb2.ListBimetaOrgsResponse.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateBimetaOrgTag(request,
                           target,
                           options=(),
                           channel_credentials=None,
                           call_credentials=None,
                           insecure=False,
                           compression=None,
                           wait_for_ready=None,
                           timeout=None,
                           metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/CreateBimetaOrgTag',
                                             org__pb2.CreateBimetaOrgTagRequest.SerializeToString,
                                             org__pb2.CreateBimetaOrgTagResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBimetaOrgTag(request,
                           target,
                           options=(),
                           channel_credentials=None,
                           call_credentials=None,
                           insecure=False,
                           compression=None,
                           wait_for_ready=None,
                           timeout=None,
                           metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgTag',
                                             org__pb2.DeleteBimetaOrgTagRequest.SerializeToString,
                                             org__pb2.BimetaOrgTagEmpty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBimetaOrgTag(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/ListBimetaOrgTag',
                                              org__pb2.ListBimetaOrgTagRequest.SerializeToString,
                                              org__pb2.ListBimetaOrgTagResponse.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateBimetaOrgConfig(request,
                              target,
                              options=(),
                              channel_credentials=None,
                              call_credentials=None,
                              insecure=False,
                              compression=None,
                              wait_for_ready=None,
                              timeout=None,
                              metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/CreateBimetaOrgConfig',
                                             org__pb2.CreateBimetaOrgConfigRequest.SerializeToString,
                                             org__pb2.CreateBimetaOrgConfigResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBimetaOrgConfig(request,
                              target,
                              options=(),
                              channel_credentials=None,
                              call_credentials=None,
                              insecure=False,
                              compression=None,
                              wait_for_ready=None,
                              timeout=None,
                              metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/UpdateBimetaOrgConfig',
                                             org__pb2.UpdateBimetaOrgConfigRequest.SerializeToString,
                                             org__pb2.UpdateBimetaOrgConfigResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadBimetaOrgConfig(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/ReadBimetaOrgConfig',
                                             org__pb2.ReadBimetaOrgConfigRequest.SerializeToString,
                                             org__pb2.ReadBimetaOrgConfigResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBimetaOrgConfig(request,
                              target,
                              options=(),
                              channel_credentials=None,
                              call_credentials=None,
                              insecure=False,
                              compression=None,
                              wait_for_ready=None,
                              timeout=None,
                              metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgConfig',
                                             org__pb2.DeleteBimetaOrgConfigRequest.SerializeToString,
                                             org__pb2.BimetaOrgConfigEmpty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateBimetaOrgCIDR(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/CreateBimetaOrgCIDR',
                                             org__pb2.CreateBimetaOrgCIDRRequest.SerializeToString,
                                             org__pb2.CreateBimetaOrgCIDRResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBimetaOrgCIDR(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/DeleteBimetaOrgCIDR',
                                             org__pb2.DeleteBimetaOrgCIDRRequest.SerializeToString,
                                             org__pb2.BimetaOrgCIDREmpty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBimetaOrgCIDR(request,
                          target,
                          options=(),
                          channel_credentials=None,
                          call_credentials=None,
                          insecure=False,
                          compression=None,
                          wait_for_ready=None,
                          timeout=None,
                          metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueintel.badapi.bimetaorg.BimetaOrgService/ListBimetaOrgCIDR',
                                              org__pb2.ListBimetaOrgCIDRRequest.SerializeToString,
                                              org__pb2.ListBimetaOrgCIDRResponse.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
