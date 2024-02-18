from abc import abstractmethod

import httpx
from typing_extensions import override


class AdsdatahubException(Exception):
    """Base exception for adsdatahub."""

    @property
    @abstractmethod
    def message(self) -> str:
        """Return the exception message."""
        ...

    def __str__(self) -> str:
        return self.message


class AdsdatahubError(AdsdatahubException):
    """Base error for adsdatahub."""


class ResponseStatusCodeError(AdsdatahubError):
    """Response status code error for adsdatahub."""

    def __init__(self, response: httpx.Response) -> None:
        self.response = response

    @property
    @override
    def message(self) -> str:
        return f"Response Status Code Error: {self.response}."
