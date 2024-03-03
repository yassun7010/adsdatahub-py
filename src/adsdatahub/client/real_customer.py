import datetime
from time import sleep

from typing_extensions import override

import adsdatahub
from adsdatahub.client.customer import CustomerClient
from adsdatahub.client.query_result import QueryResult
from adsdatahub.restapi.resources.analysis_queries.validate import (
    AnalysisQueriesValidateResponseBodyModel,
)
from adsdatahub.types import CustomerId


class RealCustomerClient(CustomerClient):
    def __init__(
        self,
        client: adsdatahub.RealClient,
        customer_id: CustomerId,
    ):
        self._client = client
        self.customer_id = customer_id

    @override
    def query(
        self,
        query_text: str,
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
                    "queryText": query_text,
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

    @override
    def validate(self, query_text: str) -> AnalysisQueriesValidateResponseBodyModel:
        return self._client.restapi.resource(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=self.customer_id,
        ).validate(
            {
                "query": {
                    "queryText": query_text,
                }
            }
        )
