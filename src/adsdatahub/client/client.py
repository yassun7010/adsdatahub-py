import datetime
from time import sleep
from typing import Unpack

from google.cloud import bigquery

import adsdatahub.restapi
from adsdatahub.client.query_result import QueryResult
from adsdatahub.restapi.real_client import RealClientConstructerKwargs
from adsdatahub.restapi.schemas._newtype import CustomerId


class Client:
    def __init__(
        self,
        customer_id: CustomerId,
        restapi_client: adsdatahub.restapi.Client | None = None,
        bigquery_client: bigquery.Client | None = None,
        **kwargs: Unpack[RealClientConstructerKwargs],
    ) -> None:
        if not restapi_client:
            restapi_client = adsdatahub.restapi.Client(**kwargs)

        if not bigquery_client:
            bigquery_client = bigquery.Client(**kwargs)

        self._customer_id = customer_id
        self.restapi = restapi_client
        self.bigquery_client = bigquery_client

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
        operation = self.restapi.resource(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=self._customer_id,
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
            operation := self.restapi.resource(
                "https://adsdatahub.googleapis.com/v1/operations/{unique_id}",
                unique_id=operation.name.unique_id,
            ).wait()
        ).done:
            sleep(3)

        return QueryResult(
            dest_table=dest_table,
            operation=operation,
            job=self.bigquery_client.query(f"SELECT * FROM {dest_table}"),
        )
