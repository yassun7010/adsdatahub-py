import uuid
from typing import TypedDict

import adsdatahub.restapi


class TestAnalysisQuery:
    def test_delete(self, restapi_client: adsdatahub.restapi.Client, customer_id: str):
        query = restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            {
                "title": f"ads-data-hub-test-{uuid.uuid4()}",
                "queryText": "SELECT 1",
            }
        )
        restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
            **parse_query_name(query.name),
        ).delete()

    def test_get(self, restapi_client: adsdatahub.restapi.Client, customer_id: str):
        query = restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            {
                "title": f"ads-data-hub-test-{uuid.uuid4()}",
                "queryText": "SELECT 1",
            }
        )

        try:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                **parse_query_name(query.name),
            ).get()

        finally:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                **parse_query_name(query.name),
            ).delete()

    def test_patch(self, restapi_client: adsdatahub.restapi.Client, customer_id: str):
        query_title = f"ads-data-hub-test-{uuid.uuid4()}"
        query = restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            {
                "title": query_title,
                "queryText": "SELECT 1",
            }
        )

        try:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                **parse_query_name(query.name),
            ).patch(
                {
                    "title": query_title,
                    "queryText": "SELECT 2",
                }
            )

        finally:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                **parse_query_name(query.name),
            ).delete()


class AnalysisQueryNameParams(TypedDict):
    customer_id: str
    resource_id: str


def parse_query_name(name: str) -> AnalysisQueryNameParams:
    parts = name.split("/")
    return AnalysisQueryNameParams(customer_id=parts[1], resource_id=parts[3])
