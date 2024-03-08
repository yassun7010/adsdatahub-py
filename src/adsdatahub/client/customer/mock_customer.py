import datetime
from types import NoneType
from typing import Any, TypeVar

from typing_extensions import override

import adsdatahub
from adsdatahub.client.customer.customer import CustomerClient
from adsdatahub.client.parameters import PythonParameterType
from adsdatahub.client.query_result import QueryResult
from adsdatahub.exceptions import AdsDataHubMockDataTypeError, AdsDataHubMockMethodError
from adsdatahub.types import CustomerId

GenericResponse = TypeVar("GenericResponse")


class MockCustomerClient(CustomerClient):
    def __init__(
        self,
        client: adsdatahub.MockClient,
        customer_id: CustomerId,
    ):
        self._client = client
        self.customer_id = customer_id
        self._store: list[tuple[str, Any]] = []

    def inject_query_response(self, response: QueryResult | Exception) -> None:
        self._store.append(("query", response))

    def inject_validate_response(self, response: None | Exception = None) -> None:
        self._store.append(("validate", response))

    def _provide_response(
        self, expected_method: str, expected_response_type: type[GenericResponse]
    ) -> GenericResponse:
        method, response = self._store.pop(0)

        if method != expected_method:
            raise AdsDataHubMockMethodError(method, expected_method)

        if isinstance(response, Exception):
            raise response

        if isinstance(response, expected_response_type):
            raise AdsDataHubMockDataTypeError(type(response), expected_response_type)

        return response

    def query(
        self,
        query_text: str,
        /,
        parameters: dict[str, PythonParameterType] | None = None,
        *,
        start_date: str | datetime.date,
        end_date: str | datetime.date,
        dest_table: str,
    ) -> QueryResult:
        return self._provide_response("query", QueryResult)

    @override
    def validate(
        self,
        query_text: str,
        /,
        parameters: dict[str, PythonParameterType] | None = None,
    ) -> None:
        return self._provide_response("validate", NoneType)
