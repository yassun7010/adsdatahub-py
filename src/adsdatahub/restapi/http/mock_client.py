import typing
from typing import Any

from typing_extensions import override

from adsdatahub._types import TimeoutTypes, URLTypes
from adsdatahub.exceptions import AdsDataHubMockDataTypeError
from adsdatahub.restapi._helpers import (
    GenericResponseBody,
)
from adsdatahub.restapi.http.client import HttpRequestKwargs

from .client import Client


class StoreKey(typing.NamedTuple):
    url: URLTypes
    method: str


class MockClient(Client):
    _store: dict[StoreKey, Any]

    __slots__ = ("_store",)

    @property
    def store(self) -> dict[StoreKey, Any]:
        if self._store is None:
            self._store = {}

        return self._store

    @property
    @override
    def timeout(self) -> TimeoutTypes:
        return 0

    @timeout.setter
    @override
    def timeout(self, value: TimeoutTypes) -> None:
        pass

    @typing.overload
    def request(
        self,
        method: str,
        url: URLTypes,
        response_body_type: type[GenericResponseBody],
        **kwargs: typing.Unpack[HttpRequestKwargs],
    ) -> GenericResponseBody: ...

    @typing.overload
    def request(
        self,
        method: str,
        url: URLTypes,
        response_body_type: None = None,
        **kwargs: typing.Unpack[HttpRequestKwargs],
    ) -> None: ...

    @override
    def request(
        self,
        method: str,
        url: URLTypes,
        response_body_type: typing.Optional[type[GenericResponseBody]] = None,
        **kwargs: typing.Unpack[HttpRequestKwargs],
    ) -> typing.Optional[GenericResponseBody]:
        response = self.store.pop(StoreKey(url, method))

        if isinstance(response, Exception):
            raise response

        if response_body_type is not None and not isinstance(
            response, response_body_type
        ):
            raise AdsDataHubMockDataTypeError(response.__class__, response_body_type)

        else:
            return response
