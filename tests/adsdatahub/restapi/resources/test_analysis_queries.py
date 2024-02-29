import uuid

import adsdatahub.restapi
import pytest
from adsdatahub.restapi.resources import analysis_queries
from adsdatahub.restapi.schemas._newtype import CustomerId


class TestAnalysisQueries:
    @pytest.fixture
    def analysis_queries_resource(
        self,
        restapi_client: adsdatahub.restapi.Client,
        customer_id: CustomerId,
    ) -> analysis_queries.Resource:
        return restapi_client.resource(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        )

    def test_create(
        self,
        analysis_queries_resource: analysis_queries.Resource,
        restapi_client: adsdatahub.restapi.Client,
        imp_query_text: str,
    ):
        analysis_query = None
        try:
            analysis_query = analysis_queries_resource.create(
                {
                    "title": f"ads-data-hub-test-{uuid.uuid4()}",
                    "queryText": imp_query_text,
                }
            )

            with open("response_body.json", "w") as f:
                f.write(analysis_query.model_dump_json(indent=2, by_alias=True))
        finally:
            if analysis_query:
                restapi_client.resource(
                    "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}",
                    customer_id=analysis_query.name.customer_id,
                    resource_id=analysis_query.name.resource_id,
                )

    def test_list(self, analysis_queries_resource: analysis_queries.Resource):
        response = analysis_queries_resource.list()
        assert response.queries

    def test_start_transient(
        self,
        analysis_queries_resource: analysis_queries.Resource,
    ):
        analysis_queries_resource.start_transient(
            {
                "query": {
                    "queryText": "SELECT * FROM project.dataset.table",
                },
                "spec": {
                    "startDate": "2021-01-01",
                    "endDate": "2021-12-31",
                },
                "destTable": "project.dataset.table",
            }
        )

    def test_validate(
        self,
        analysis_queries_resource: analysis_queries.Resource,
        imp_query_text: str,
    ):
        analysis_queries_resource.validate(
            {
                "query": {"queryText": imp_query_text},
            }
        )
