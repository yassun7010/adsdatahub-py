import adsdatahub.restapi
import pytest
from adsdatahub.restapi.resources import analysis_queries


class TestAnalysisQueries:
    @pytest.fixture
    def analysis_queries_resource(
        self,
        restapi_client: adsdatahub.restapi.Client,
        client_id: str,
    ) -> analysis_queries.Resource:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=client_id,
        )

    def test_list(self, analysis_queries_resource: analysis_queries.Resource):
        response = analysis_queries_resource.list(filter="")
        assert response.queries
