import uuid
from typing import Callable, TypedDict

import adsdatahub.restapi
import pytest
from adsdatahub.exceptions import (
    AdsDataHubResponseStatusCodeError,
    AdsDataHubUnimplementedError,
)
from adsdatahub.restapi.resources import operation
from adsdatahub.restapi.schemas.operation import OperationModel
from adsdatahub.restapi.schemas.query_metadata import QueryMetadataModel

OperationId = str

OperationResourceGetter = Callable[[OperationId], operation.Resource]


class TestOperation:
    @pytest.fixture
    def operation_response(
        self, restapi_client: adsdatahub.restapi.Client, customer_id: int
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

    def test_cancel(
        self,
        restapi_client: adsdatahub.restapi.Client,
        operation_response: OperationModel[QueryMetadataModel],
    ):
        # TODO: 正しいクエリを作成する必要がある。
        with pytest.raises(AdsDataHubResponseStatusCodeError):
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/operations/{unique_id}",
                **parse_operation_name(operation_response.name),
            ).cancel()

    def test_delete(
        self,
        restapi_client: adsdatahub.restapi.Client,
        operation_response: OperationModel[QueryMetadataModel],
    ):
        try:
            restapi_client.request(
                "https://adsdatahub.googleapis.com/v1/operations/{unique_id}",
                **parse_operation_name(operation_response.name),
            ).delete()

        except AdsDataHubUnimplementedError:
            # NOTE: サーバーによっては google.rpc.Code.UNIMPLEMENTED を返すことがある。
            #       Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/delete?hl=ja
            pass

    def test_get(
        self,
        restapi_client: adsdatahub.restapi.Client,
        operation_response: OperationModel[QueryMetadataModel],
    ):
        restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/operations/{unique_id}",
            **parse_operation_name(operation_response.name),
        ).get()

    def test_wait(
        self,
        restapi_client: adsdatahub.restapi.Client,
        operation_response: OperationModel[QueryMetadataModel],
    ):
        restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/operations/{unique_id}",
            **parse_operation_name(operation_response.name),
        ).wait()


class OperationNameParams(TypedDict):
    unique_id: str


def parse_operation_name(name: str) -> OperationNameParams:
    return {"unique_id": name.split("/")[-1]}
