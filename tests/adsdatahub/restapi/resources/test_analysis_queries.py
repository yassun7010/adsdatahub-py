from textwrap import dedent

import adsdatahub.restapi
import pytest
from adsdatahub.exceptions import AdsDataHubResponseStatusCodeError
from adsdatahub.restapi.resources import analysis_queries
from adsdatahub.restapi.schemas._newtype import CustomerId


class TestAnalysisQueries:
    @pytest.fixture
    def analysis_queries_resource(
        self,
        restapi_client: adsdatahub.restapi.Client,
        customer_id: CustomerId,
    ) -> analysis_queries.Resource:
        return restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
            customer_id=customer_id,
        )

    def test_create(
        self,
        analysis_queries_resource: analysis_queries.Resource,
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
    ):
        analysis_queries_resource.validate(
            {
                "query": {
                    "queryText": dedent(
                        """
                        SELECT
                            campaign_id,
                            date(timestamp_micros(query_id.time_usec), 'Asia/Tokyo') AS date,
                            count(query_id.time_usec) AS imp
                        FROM
                            adh.google_ads_impressions
                        GROUP BY
                            campaign_id,
                            date
                        """
                    ),
                },
            }
        )
