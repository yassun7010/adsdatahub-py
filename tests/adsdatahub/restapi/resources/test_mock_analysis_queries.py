import uuid

import adsdatahub.restapi
import pytest
from adsdatahub.restapi.schemas.analysis_query import (
    AnalysisQueryModel,
)
from adsdatahub.types import CustomerId

from tests.conftest import synthetic_monitoring_is_disable


@pytest.mark.skipif(**synthetic_monitoring_is_disable())
class TestMockAnalysisQueries:
    def test_create(
        self,
        mock_restapi_client: adsdatahub.restapi.MockClient,
        customer_id: CustomerId,
        imp_query_text: str,
    ):
        title = f"ads-data-hub-test-{uuid.uuid4()}"

        mock_restapi_client.inject_response(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            AnalysisQueryModel.model_validate(
                {
                    "name": "customers/417739410/analysisQueries/615154cdeada4c3aab91a06dd1a90afb",
                    "title": title,
                    "queryText": imp_query_text,
                    "queryState": "RUNNABLE",
                    "updateTime": "2024-02-28T15:50:11.497000Z",
                    "updateEmail": "adh-querier-executer@aitech-aoc-akagi-cdp-dev.iam.gserviceaccount.com",
                    "createTime": "2024-02-28T15:50:11.497000Z",
                    "createEmail": "adh-querier-executer@aitech-aoc-akagi-cdp-dev.iam.gserviceaccount.com",
                }
            )
        ).resource(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        ).create(
            {
                "title": title,
                "queryText": imp_query_text,
            }
        )
