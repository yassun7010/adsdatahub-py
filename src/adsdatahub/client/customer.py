import datetime
from time import sleep

import adsdatahub
from adsdatahub.client.query_result import QueryResult
from adsdatahub.types import CustomerId


class CustomerClient:
    def __init__(
        self,
        client: adsdatahub.Client,
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
        operation = self._client.restapi.resource(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=self.customer_id,
        ).start_transient(
            {
                "query": {
                    "queryText": query,
                },
                "spec": {
                    "startDate": start_date,
                    "endDate": end_date,
                },
                "destTable": dest_table,
            }
        )

        while not (
            operation := self._client.restapi.resource(
                "https://adsdatahub.googleapis.com/v1/operations/{operation_id}",
                operation_id=operation.name.operation_id,
            ).wait()
        ).done:
            sleep(3)

        return QueryResult(
            dest_table=dest_table,
            operation=operation,
            job=self._client.bigquery_client.query(f"SELECT * FROM {dest_table}"),
        )
