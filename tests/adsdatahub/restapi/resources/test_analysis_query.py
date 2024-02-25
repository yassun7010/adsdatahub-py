import asyncio
import uuid

import adsdatahub.restapi
import adsdatahub.restapi.resources.analysis_query
import pytest
from adsdatahub.restapi.schemas._newtype import CustomerId
from adsdatahub.restapi.schemas.analysis_query import AnalysisQueryModel

from tests.conftest import SLEEP_TIME_SEC


class TestAnalysisQuery:
    @pytest.fixture
    def analysis_query(
        self, restapi_client: adsdatahub.restapi.Client, customer_id: CustomerId
    ) -> AnalysisQueryModel:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            {
                "title": f"ads-data-hub-test-{uuid.uuid4()}",
                "queryText": "SELECT 1",
            }
        )

    @pytest.fixture
    def analysis_query_resource(
        self,
        analysis_query: AnalysisQueryModel,
        restapi_client: adsdatahub.restapi.Client,
    ) -> adsdatahub.restapi.resources.analysis_query.Resource:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
            customer_id=analysis_query.name.customer_id,
            resource_id=analysis_query.name.resource_id,
        )

    @pytest.mark.asyncio
    async def test_delete(
        self,
        analysis_query_resource: adsdatahub.restapi.resources.analysis_query.Resource,
    ):
        await asyncio.sleep(SLEEP_TIME_SEC)

        analysis_query_resource.delete()

    @pytest.mark.asyncio
    async def test_get(
        self,
        analysis_query_resource: adsdatahub.restapi.resources.analysis_query.Resource,
    ):
        await asyncio.sleep(SLEEP_TIME_SEC)

        try:
            analysis_query_resource.get()

        finally:
            analysis_query_resource.delete()

    def test_patch(
        self,
        analysis_query: AnalysisQueryModel,
        analysis_query_resource: adsdatahub.restapi.resources.analysis_query.Resource,
    ):
        try:
            analysis_query_resource.patch(
                {
                    "title": analysis_query.title,
                    "queryText": "SELECT 2",
                }
            )

        finally:
            analysis_query_resource.delete()

    @pytest.mark.asyncio
    async def test_start(
        self,
        analysis_query_resource: adsdatahub.restapi.resources.analysis_query.Resource,
    ):
        await asyncio.sleep(SLEEP_TIME_SEC)

        try:
            analysis_query_resource.start(
                spec={
                    "startDate": "2021-01-01",
                    "endDate": "2021-12-31",
                },
                dest_table="project.dataset.table",
            )

        finally:
            analysis_query_resource.delete()
