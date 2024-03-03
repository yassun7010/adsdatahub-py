import datetime

import adsdatahub
from adsdatahub.client.customer import CustomerClient
from adsdatahub.client.query_result import QueryResult
from adsdatahub.types import CustomerId


class MockCustomerClient(CustomerClient):
    def __init__(
        self,
        client: adsdatahub.MockClient,
        customer_id: CustomerId,
    ):
        self._client = client
        self.customer_id = customer_id

    def query(
        self,
        query: str,
        /,
        parameters: dict[str, str] | None = None,
        *,
        start_date: str | datetime.date,
        end_date: str | datetime.date,
        dest_table: str,
    ) -> QueryResult:
        raise NotImplementedError()
