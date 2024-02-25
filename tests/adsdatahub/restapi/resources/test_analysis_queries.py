import adsdatahub.restapi
import pytest
from adsdatahub.exceptions import AdsDataHubResponseStatusCodeError
from adsdatahub.restapi.resources import analysis_queries


class TestAnalysisQueries:
    @pytest.fixture
    def analysis_queries_resource(
        self,
        restapi_client: adsdatahub.restapi.Client,
        customer_id: int,
    ) -> analysis_queries.Resource:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        )

    def test_create(
        self, analysis_queries_resource: analysis_queries.Resource, customer_id: int
    ):
        with pytest.raises(AdsDataHubResponseStatusCodeError):
            analysis_queries_resource.create(
                {
                    "title": "ads-data-hub-test",
                    "queryText": "SELECT * FROM `project.dataset.table`",
                }
            )

    def test_list(self, analysis_queries_resource: analysis_queries.Resource):
        response = analysis_queries_resource.list()
        assert response.queries

    def test_start_transient(
        self, analysis_queries_resource: analysis_queries.Resource, customer_id: int
    ):
        analysis_queries_resource.start_transient(
            query={
                "title": "ads-data-hub-test",
                "queryText": "SELECT * FROM `project.dataset.table`",
            },
            spec={
                "startDate": "2021-01-01",
                "endDate": "2021-12-31",
            },
            dest_table="project.dataset.table",
        )

    def test_validate(
        self, analysis_queries_resource: analysis_queries.Resource, customer_id: int
    ):
        analysis_queries_resource.validate(
            query={
                "title": "ads-data-hub-test",
                "queryText": """
                    select
                        campaign_id,
                        date(timestamp_micros(query_id.time_usec), 'Asia/Tokyo') as date,
                        count(query_id.time_usec) as imp
                    from
                        adh.google_ads_impressions
                    group by
                        campaign_id,
                        date
                    """,
            },
        )
