import uuid

import adsdatahub.restapi
import pytest
from adsdatahub.restapi.resources.analysis_queries.list import AnalysisQueryListResponse
from adsdatahub.restapi.schemas.analysis_query import (
    AnalysisQueryModel,
)
from adsdatahub.types import CustomerId

from tests.conftest import synthetic_monitoring_is_disable


@pytest.mark.skipif(**synthetic_monitoring_is_disable())
class TestMockAnalysisQueries:
    @pytest.fixture
    def analysis_query(
        self,
        customer_id: CustomerId,
        imp_query_text: str,
    ):
        return AnalysisQueryModel.model_validate(
            {
                "name": f"customers/{customer_id}/analysisQueries/123456cdeada4c3aab91a06dd1a90abc",
                "title": f"ads-data-hub-test-{uuid.uuid4()}",
                "queryText": imp_query_text,
                "queryState": "RUNNABLE",
                "updateTime": "2024-02-28T15:50:11.497000Z",
                "updateEmail": "myaccount@myproject.iam.gserviceaccount.com",
                "createTime": "2024-02-28T15:50:11.497000Z",
                "createEmail": "myaccount@myproject.iam.gserviceaccount.com",
            }
        )

    def test_create(
        self,
        mock_restapi_client: adsdatahub.restapi.MockClient,
        customer_id: CustomerId,
        analysis_query: AnalysisQueryModel,
        imp_query_text: str,
    ):
        title = f"ads-data-hub-test-{uuid.uuid4()}"

        expected_response = analysis_query

        mock_restapi_client.inject_response(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            expected_response,
        )

        response = mock_restapi_client.resource(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            {
                "title": title,
                "queryText": imp_query_text,
            }
        )

        assert response == expected_response

    def test_list(
        self,
        mock_restapi_client: adsdatahub.restapi.MockClient,
        customer_id: CustomerId,
        analysis_query: AnalysisQueryModel,
    ):
        expected_response = AnalysisQueryListResponse.model_validate(
            {
                "queries": [
                    analysis_query,
                ]
            }
        )

        mock_restapi_client.inject_response(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).list(expected_response)

        response = mock_restapi_client.resource(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).list()

        assert response == expected_response
