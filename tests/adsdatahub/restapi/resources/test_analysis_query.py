import asyncio
import uuid

import adsdatahub.restapi
import pytest
from adsdatahub.restapi.schemas._newtype import CustomerId


class TestAnalysisQuery:
    @pytest.mark.asyncio
    async def test_delete(
        self, restapi_client: adsdatahub.restapi.Client, customer_id: CustomerId
    ):
        query = restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            {
                "title": f"ads-data-hub-test-{uuid.uuid4()}",
                "queryText": "SELECT 1",
            }
        )

        await asyncio.sleep(1)

        restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
            customer_id=query.name.customer_id,
            resource_id=query.name.resource_id,
        ).delete()

    @pytest.mark.asyncio
    async def test_get(
        self, restapi_client: adsdatahub.restapi.Client, customer_id: CustomerId
    ):
        query = restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            {
                "title": f"ads-data-hub-test-{uuid.uuid4()}",
                "queryText": "SELECT 1",
            }
        )

        await asyncio.sleep(1)

        try:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                customer_id=query.name.customer_id,
                resource_id=query.name.resource_id,
            ).get()

        finally:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                customer_id=query.name.customer_id,
                resource_id=query.name.resource_id,
            ).delete()

    def test_patch(
        self, restapi_client: adsdatahub.restapi.Client, customer_id: CustomerId
    ):
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
                customer_id=query.name.customer_id,
                resource_id=query.name.resource_id,
            ).patch(
                {
                    "title": query_title,
                    "queryText": "SELECT 2",
                }
            )

        finally:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                customer_id=query.name.customer_id,
                resource_id=query.name.resource_id,
            ).delete()

    @pytest.mark.asyncio
    async def test_start(
        self, restapi_client: adsdatahub.restapi.Client, customer_id: CustomerId
    ):
        query = restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            {
                "title": f"ads-data-hub-test-{uuid.uuid4()}",
                "queryText": "SELECT 1",
            }
        )

        await asyncio.sleep(1)

        try:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                customer_id=query.name.customer_id,
                resource_id=query.name.resource_id,
            ).start(
                spec={
                    "startDate": "2021-01-01",
                    "endDate": "2021-12-31",
                },
                dest_table="project.dataset.table",
            )

        finally:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                customer_id=query.name.customer_id,
                resource_id=query.name.resource_id,
            ).delete()
