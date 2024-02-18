import os

import ads_data_hub.restapi
import pytest
from ads_data_hub.restapi.resources import analysis_query


class TestAnalysisQuery:
    @pytest.fixture
    def analysis_query_resource(
        self, restapi_client: ads_data_hub.restapi.Client
    ) -> analysis_query.Resource:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=os.environ["ADS_DATA_HUB_CUSTOMER_ID"],
        )

    def test_list(self, analysis_query_resource: analysis_query.Resource):
        response = analysis_query_resource.list(filter="")
        assert response.queries
