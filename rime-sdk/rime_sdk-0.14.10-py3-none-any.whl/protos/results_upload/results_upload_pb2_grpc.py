# autogenerated
# mypy: ignore-errors
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from rime_sdk.protos.results_upload import results_upload_pb2 as protos_dot_results__upload_dot_results__upload__pb2


class ResultsStoreStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VerifyProjectID = channel.unary_unary(
                '/rime.ResultsStore/VerifyProjectID',
                request_serializer=protos_dot_results__upload_dot_results__upload__pb2.VerifyProjectIDRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateProject = channel.unary_unary(
                '/rime.ResultsStore/CreateProject',
                request_serializer=protos_dot_results__upload_dot_results__upload__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=protos_dot_results__upload_dot_results__upload__pb2.CreateProjectResponse.FromString,
                )
        self.HackyEditProjectFirewallID = channel.unary_unary(
                '/rime.ResultsStore/HackyEditProjectFirewallID',
                request_serializer=protos_dot_results__upload_dot_results__upload__pb2.HackyEditProjectFirewallIDRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetTestRunResultCSV = channel.unary_stream(
                '/rime.ResultsStore/GetTestRunResultCSV',
                request_serializer=protos_dot_results__upload_dot_results__upload__pb2.GetTestRunResultCSVRequest.SerializeToString,
                response_deserializer=protos_dot_results__upload_dot_results__upload__pb2.GetTestRunResultCSVResponse.FromString,
                )
        self.UploadCTTestRuns = channel.stream_unary(
                '/rime.ResultsStore/UploadCTTestRuns',
                request_serializer=protos_dot_results__upload_dot_results__upload__pb2.Chunk.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UploadFirewallRules = channel.stream_unary(
                '/rime.ResultsStore/UploadFirewallRules',
                request_serializer=protos_dot_results__upload_dot_results__upload__pb2.UploadChunk.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ResultsStoreServicer(object):
    """Missing associated documentation comment in .proto file."""

    def VerifyProjectID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HackyEditProjectFirewallID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTestRunResultCSV(self, request, context):
        """Create a CSV for a test run result and return it row-by-row.
        We return it row-by-row with streaming because the size of the CSV
        grows unbounded with the size of the dataset and this operation can be slow.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadCTTestRuns(self, request_iterator, context):
        """V12 CT endpoints - keeping it here in same service to not break existing trial flow.
        From now on CT endpoints will be added to the CTService service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFirewallRules(self, request_iterator, context):
        """V14 Endpoint to handle uploading of Firewall rules only
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResultsStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VerifyProjectID': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyProjectID,
                    request_deserializer=protos_dot_results__upload_dot_results__upload__pb2.VerifyProjectIDRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=protos_dot_results__upload_dot_results__upload__pb2.CreateProjectRequest.FromString,
                    response_serializer=protos_dot_results__upload_dot_results__upload__pb2.CreateProjectResponse.SerializeToString,
            ),
            'HackyEditProjectFirewallID': grpc.unary_unary_rpc_method_handler(
                    servicer.HackyEditProjectFirewallID,
                    request_deserializer=protos_dot_results__upload_dot_results__upload__pb2.HackyEditProjectFirewallIDRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetTestRunResultCSV': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTestRunResultCSV,
                    request_deserializer=protos_dot_results__upload_dot_results__upload__pb2.GetTestRunResultCSVRequest.FromString,
                    response_serializer=protos_dot_results__upload_dot_results__upload__pb2.GetTestRunResultCSVResponse.SerializeToString,
            ),
            'UploadCTTestRuns': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadCTTestRuns,
                    request_deserializer=protos_dot_results__upload_dot_results__upload__pb2.Chunk.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UploadFirewallRules': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadFirewallRules,
                    request_deserializer=protos_dot_results__upload_dot_results__upload__pb2.UploadChunk.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rime.ResultsStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ResultsStore(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def VerifyProjectID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.ResultsStore/VerifyProjectID',
            protos_dot_results__upload_dot_results__upload__pb2.VerifyProjectIDRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.ResultsStore/CreateProject',
            protos_dot_results__upload_dot_results__upload__pb2.CreateProjectRequest.SerializeToString,
            protos_dot_results__upload_dot_results__upload__pb2.CreateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HackyEditProjectFirewallID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.ResultsStore/HackyEditProjectFirewallID',
            protos_dot_results__upload_dot_results__upload__pb2.HackyEditProjectFirewallIDRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTestRunResultCSV(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/rime.ResultsStore/GetTestRunResultCSV',
            protos_dot_results__upload_dot_results__upload__pb2.GetTestRunResultCSVRequest.SerializeToString,
            protos_dot_results__upload_dot_results__upload__pb2.GetTestRunResultCSVResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadCTTestRuns(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/rime.ResultsStore/UploadCTTestRuns',
            protos_dot_results__upload_dot_results__upload__pb2.Chunk.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadFirewallRules(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/rime.ResultsStore/UploadFirewallRules',
            protos_dot_results__upload_dot_results__upload__pb2.UploadChunk.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
