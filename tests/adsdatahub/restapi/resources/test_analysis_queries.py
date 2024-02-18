import adsdatahub.restapi
import pytest
from adsdatahub.exceptions import ResponseStatusCodeError
from adsdatahub.restapi.resources import analysis_queries


class TestAnalysisQueries:
    @pytest.fixture
    def analysis_queries_resource(
        self,
        restapi_client: adsdatahub.restapi.Client,
        customer_id: str,
    ) -> analysis_queries.Resource:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        )

    def test_list(self, analysis_queries_resource: analysis_queries.Resource):
        response = analysis_queries_resource.list(filter="")
        assert response.queries

    def test_start_transient(
        self, analysis_queries_resource: analysis_queries.Resource, customer_id: str
    ):
        with pytest.raises(ResponseStatusCodeError):
            analysis_queries_resource.start_transient(**{})
