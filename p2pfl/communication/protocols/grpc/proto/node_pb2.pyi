"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
compile command:
python -m grpc_tools.protoc -I=p2pfl/proto --python_out=p2pfl/proto --grpc_python_out=p2pfl/proto p2pfl/proto/node.proto --mypy_out=p2pfl/proto
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class RootMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    CMD_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    WEIGHTS_FIELD_NUMBER: builtins.int
    source: builtins.str
    round: builtins.int
    cmd: builtins.str
    @property
    def message(self) -> global___Message: ...
    @property
    def weights(self) -> global___Weights: ...
    def __init__(
        self,
        *,
        source: builtins.str = ...,
        round: builtins.int | None = ...,
        cmd: builtins.str = ...,
        message: global___Message | None = ...,
        weights: global___Weights | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "_round",
            b"_round",
            "message",
            b"message",
            "payload_type",
            b"payload_type",
            "round",
            b"round",
            "weights",
            b"weights",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "_round",
            b"_round",
            "cmd",
            b"cmd",
            "message",
            b"message",
            "payload_type",
            b"payload_type",
            "round",
            b"round",
            "source",
            b"source",
            "weights",
            b"weights",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_round", b"_round"]) -> typing.Literal["round"] | None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing.Literal["payload_type", b"payload_type"]
    ) -> typing.Literal["message", "weights"] | None: ...

global___RootMessage = RootMessage

@typing.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TTL_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    ttl: builtins.int
    hash: builtins.int
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        ttl: builtins.int = ...,
        hash: builtins.int = ...,
        args: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["args", b"args", "hash", b"hash", "ttl", b"ttl"]) -> None: ...

global___Message = Message

@typing.final
class Weights(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WEIGHTS_FIELD_NUMBER: builtins.int
    CONTRIBUTORS_FIELD_NUMBER: builtins.int
    NUM_SAMPLES_FIELD_NUMBER: builtins.int
    weights: builtins.bytes
    num_samples: builtins.int
    @property
    def contributors(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        weights: builtins.bytes = ...,
        contributors: collections.abc.Iterable[builtins.str] | None = ...,
        num_samples: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "contributors", b"contributors", "num_samples", b"num_samples", "weights", b"weights"
        ],
    ) -> None: ...

global___Weights = Weights

@typing.final
class HandShakeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDR_FIELD_NUMBER: builtins.int
    addr: builtins.str
    def __init__(
        self,
        *,
        addr: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["addr", b"addr"]) -> None: ...

global___HandShakeRequest = HandShakeRequest

@typing.final
class ResponseMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_FIELD_NUMBER: builtins.int
    error: builtins.str
    def __init__(
        self,
        *,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_error", b"_error", "error", b"error"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...

global___ResponseMessage = ResponseMessage
