import adsdatahub
from google.cloud import bigquery


class TestClient:
    def test_query(
        self, client: adsdatahub.Client, project: str, dataset: str, imp_query_text: str
    ):
        table_name = f"{project}.{dataset}.ads_data_bub_test"

        try:
            client.query(
                imp_query_text,
                start_date="2021-01-01",
                end_date="2021-01-02",
                dest_table=table_name,
            )

        finally:
            bigquery.Client().delete_table(table_name, not_found_ok=True)
