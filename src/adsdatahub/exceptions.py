import json
from abc import abstractmethod
from typing import Any

import httpx
from typing_extensions import override

from adsdatahub.types import OperationId


class AdsDataHubException(Exception):
    """Base exception for adsdatahub."""

    @property
    @abstractmethod
    def message(self) -> str:
        """Return the exception message."""
        ...

    def __str__(self) -> str:
        return self.message


class AdsDataHubError(AdsDataHubException):
    """Base error for adsdatahub."""


class AdsDataHubResponseStatusCodeError(AdsDataHubError):
    """Response status code error for adsdatahub."""

    def __init__(self, response: httpx.Response) -> None:
        self.response = response
        if response.headers.get("content-type") == "application/json":
            self.response_body = response.json()
        else:
            self.response_body = response.content.decode("utf-8")

    @property
    @override
    def message(self) -> str:
        return f"Response Status Code Error {self.response}: {self.response_body}"


class AdsDataHubUnimplementedError(AdsDataHubResponseStatusCodeError):
    """
    このメソッドがサーバーでサポートされていないため、google.rpc.Code.UNIMPLEMENTED を返した場合のエラー。

    See: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/delete?hl=ja
    """

    def __init__(self, response: httpx.Response) -> None:
        super().__init__(response)


class AdsDataHubUnavailableError(AdsDataHubResponseStatusCodeError):
    """
    このメソッドがサーバーで利用できないため、google.rpc.Code.UNAVAILABLE を返した場合のエラー。

    See: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/delete?hl=ja
    """

    def __init__(self, response: httpx.Response) -> None:
        super().__init__(response)


class AdsDataHubMockDataTypeError(AdsDataHubError):
    """Mock data type error for adsdatahub."""

    def __init__(self, response_type: type, expected_type: type) -> None:
        self.response_type = response_type
        self.expected_type = expected_type

    @property
    @override
    def message(self) -> str:
        return f"Mock Data Type Error {self.response_type.__name__}: expected {self.expected_type.__name__}"


class AdsDataHubDestinationTableInfoNotFound(AdsDataHubError):
    def __init__(self, operation_id: OperationId) -> None:
        self.operation_id = operation_id

    @property
    @override
    def message(self) -> str:
        return f"Destination Table Info Not Found: operation_id={self.operation_id}"


class AdsDataHubResponseBodyHasError(AdsDataHubError):
    def __init__(self, response: httpx.Response, error: dict[str, Any]) -> None:
        self.response = response
        self.error = error

    @property
    @override
    def message(self) -> str:
        return f"ResponseBody has error: {json.dumps(self.error, ensure_ascii=False)}"
