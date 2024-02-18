import adsdatahub.restapi
import pytest
from adsdatahub.restapi.resources import analysis_query


class TestAnalysisQuery:
    @pytest.fixture
    def analysis_query_resource(
        self,
        restapi_client: adsdatahub.restapi.Client,
        client_id: str,
    ) -> analysis_query.Resource:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=client_id,
        )

    def test_list(self, analysis_query_resource: analysis_query.Resource):
        response = analysis_query_resource.list(filter="")
        assert response.queries
