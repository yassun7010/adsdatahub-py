import adsdatahub
import pytest
from adsdatahub._types import CustomerId
from google.cloud import bigquery

from tests.conftest import synthetic_monitoring_is_disable


@pytest.mark.skipif(**synthetic_monitoring_is_disable())
class TestClient:
    @pytest.mark.long
    def test_query(
        self,
        client: adsdatahub.Client,
        project: str,
        dataset: str,
        imp_query_text: str,
        customer_id: CustomerId,
    ):
        table_name = f"{project}.{dataset}.ads_data_bub_test"

        try:
            client.customer(customer_id).query(
                imp_query_text,
                start_date="2021-01-01",
                end_date="2021-01-02",
                dest_table=table_name,
            )

        finally:
            bigquery.Client().delete_table(table_name, not_found_ok=True)
