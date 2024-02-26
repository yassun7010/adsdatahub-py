import asyncio
import uuid
from typing import Callable

import adsdatahub.restapi
import adsdatahub.restapi.resources.operation
import pytest
from adsdatahub.exceptions import (
    AdsDataHubUnimplementedError,
)
from adsdatahub.restapi.resources import operation
from adsdatahub.restapi.schemas._newtype import CustomerId
from adsdatahub.restapi.schemas.operation import OperationModel
from adsdatahub.restapi.schemas.query_metadata import QueryMetadataModel

from tests.conftest import SLEEP_TIME_SEC

OperationId = str

OperationResourceGetter = Callable[[OperationId], operation.Resource]


class TestOperation:
    @pytest.fixture
    def operation_response(
        self, restapi_client: adsdatahub.restapi.Client, customer_id: CustomerId
    ) -> OperationModel[QueryMetadataModel]:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).start_transient(
            query={
                "title": f"ads-data-hub-test-{uuid.uuid4()}",
                "queryText": """
                    SELECT
                        COUNT(DISTINCT user_id) AS total_users,
                        COUNT(DISTINCT event.site_id) AS total_sites,
                        COUNT(DISTINCT device_id_md5) AS total_devices,
                        COUNT(event.placement_id) AS impressions
                    FROM
                        adh.cm_dt_impressions
                    WHERE
                        user_id != '0'
                        AND event.advertiser_id IN UNNEST(@advertiser_ids)
                        AND event.campaign_id IN UNNEST(@campaign_ids)
                        AND event.placement_id IN UNNEST(@placement_ids)
                        AND event.country_domain_name = 'US'
                        ;
                """,
            },
            spec={
                "startDate": "2023-01-01",
                "endDate": "2023-01-01",
            },
            dest_table="operation_test",
        )

    @pytest.fixture
    def operation_resource(
        self,
        restapi_client: adsdatahub.restapi.Client,
        operation_response: OperationModel[QueryMetadataModel],
    ) -> adsdatahub.restapi.resources.operation.Resource:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/operations/{unique_id}",
            unique_id=operation_response.name.unique_id,
        )

    @pytest.mark.asyncio
    async def test_cancel(
        self, operation_resource: adsdatahub.restapi.resources.operation.Resource
    ):
        await asyncio.sleep(SLEEP_TIME_SEC)
        operation_resource.cancel()

    def test_delete(
        self, operation_resource: adsdatahub.restapi.resources.operation.Resource
    ):
        try:
            operation_resource.delete()

        except AdsDataHubUnimplementedError:
            # NOTE: サーバーによっては google.rpc.Code.UNIMPLEMENTED を返すことがある。
            #       Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/delete?hl=ja
            pass

    def test_get(
        self, operation_resource: adsdatahub.restapi.resources.operation.Resource
    ):
        operation_resource.get()

    def test_wait(
        self, operation_resource: adsdatahub.restapi.resources.operation.Resource
    ):
        operation_resource.wait()
