import datetime
from typing import Callable, TypedDict

import adsdatahub.restapi
import pytest
from adsdatahub.restapi.resources import operation

OperationId = str

OperationResourceGetter = Callable[[OperationId], operation.Resource]


class TestOperations:
    def test_cancel(
        self,
        restapi_client: adsdatahub.restapi.Client,
        customer_id: int,
        project: str,
        dataset: str,
    ):
        operation = restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).start_transient(
            query={
                "title": "ads-data-hub-test",
                "queryText": "SELECT 1 as id",
            },
            spec={
                "startDate": "2021-01-01",
                "endDate": "2021-12-31",
            },
            dest_table=f"{project}.{dataset}.ads_data_hub_test",
        )

        restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/operations/{unique_id}",
            **parse_query_name(operation.name),
        ).cancel()

    def test_wait(self, get_operations_resource: OperationResourceGetter):
        with pytest.raises(NotImplementedError):
            get_operations_resource("1234").wait(timeout=datetime.timedelta(seconds=1))


class OperationNameParams(TypedDict):
    unique_id: str


def parse_query_name(name: str) -> OperationNameParams:
    return {"unique_id": name.split("/")[-1]}
