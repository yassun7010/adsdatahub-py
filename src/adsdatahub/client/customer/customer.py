import datetime
from abc import ABC, abstractmethod

import adsdatahub
from adsdatahub.client.parameters import PythonParameterType
from adsdatahub.client.query_result import QueryResult
from adsdatahub.types import CustomerId


class CustomerClient(ABC):
    def __init__(
        self,
        client: adsdatahub.Client,
        customer_id: CustomerId,
    ): ...

    @abstractmethod
    def query(
        self,
        query_text: str,
        /,
        parameters: dict[str, PythonParameterType] | None = None,
        *,
        start_date: str | datetime.date,
        end_date: str | datetime.date,
        dest_table: str,
    ) -> QueryResult: ...

    @abstractmethod
    def validate(
        self,
        query_text: str,
        /,
        parameters: dict[str, PythonParameterType] | None = None,
    ) -> None: ...
