from textwrap import dedent

import adsdatahub.restapi
import pytest
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
        analysis_queries_resource.start_transient(
            query={
                "name": "customers/417739410/analysisQueries/7b54b3857feb4c329fb7917152a081ae",
                "title": "adh_cache_test_chiba",
                "queryText": dedent(
                    """
                    select
                        campaign_id,
                        date(timestamp_micros(query_id.time_usec), 'Asia/Tokyo') as date,
                        count(query_id.time_usec) as imp
                    from
                        adh.google_ads_impressions
                    group by 1, 2;
                    """
                ),
                "updateTime": "2023-12-21T03:54:31.642Z",
                "updateEmail": "chiba_katsuhito@cyberagent.co.jp",
                "createTime": "2023-12-21T03:54:31.642Z",
                "createEmail": "chiba_katsuhito@cyberagent.co.jp",
                "generateFilteredRowSummaryAutomatically": True,
            },
            spec={
                "adsDataCustomerId": customer_id,
                "startDate": "2023-12-21T03:54:31.642Z",
                "endDate": "2023-12-21T03:54:31.642Z",
                "timeZone": "Asia/Tokyo",
            },
            dest_table="adh_cache_test_chiba",
        )
