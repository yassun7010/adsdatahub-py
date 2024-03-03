import uuid

import adsdatahub
import pytest
from adsdatahub.exceptions import AdsDataHubResponseStatusCodeError
from adsdatahub.types import CustomerId
from google.cloud import bigquery

from tests.conftest import synthetic_monitoring_is_disable


@pytest.mark.skipif(**synthetic_monitoring_is_disable())
class TestClient:
    @pytest.fixture
    def table_name(self, project: str, dataset: str) -> str:
        return f"{project}.{dataset}.ads_data_bub_test_{str(uuid.uuid4()).replace('-', '')}"

    def test_constructor_type(self):
        assert isinstance(adsdatahub.Client(), adsdatahub.RealClient)

    @pytest.mark.long
    def test_query(
        self,
        client: adsdatahub.Client,
        imp_query_text: str,
        customer_id: CustomerId,
        table_name: str,
    ):
        try:
            client.customer(customer_id).query(
                imp_query_text,
                start_date="2021-01-01",
                end_date="2021-01-02",
                dest_table=table_name,
            )

        finally:
            bigquery.Client().delete_table(table_name, not_found_ok=True)

    @pytest.mark.long
    def test_query_with_default_parameter(
        self,
        client: adsdatahub.Client,
        customer_id: CustomerId,
        table_name: str,
    ):
        try:
            # NOTE: start_date, end_date はデフォルトで定義されているため、エラーにならない。
            client.customer(customer_id).query(
                "SELECT @start_date as start_date",
                start_date="2021-01-01",
                end_date="2021-01-02",
                dest_table=table_name,
            )
        finally:
            bigquery.Client().delete_table(table_name, not_found_ok=True)

    def test_query_with_undefined_parameter(
        self,
        client: adsdatahub.Client,
        customer_id: CustomerId,
    ):
        with pytest.raises(AdsDataHubResponseStatusCodeError):
            client.customer(customer_id).query(
                "SELECT @value as value",
                start_date="2021-01-01",
                end_date="2021-01-02",
                dest_table="test",
            )

    def test_query_with_parameter(
        self,
        client: adsdatahub.Client,
        customer_id: CustomerId,
        table_name: str,
    ):
        try:
            client.customer(customer_id).query(
                "SELECT @value as value",
                {"value": 1},
                start_date="2021-01-01",
                end_date="2021-01-02",
                dest_table=table_name,
            )
        finally:
            bigquery.Client().delete_table(table_name, not_found_ok=True)

    def test_validate_with_default_parameter(
        self,
        client: adsdatahub.Client,
        customer_id: CustomerId,
    ):
        # NOTE: start_date, end_date はデフォルトで定義されているため、エラーにならない。
        client.customer(customer_id).validate(
            "SELECT @start_date as start_date",
        )

    def test_validate_with_undefined_parameter(
        self,
        client: adsdatahub.Client,
        customer_id: CustomerId,
    ):
        with pytest.raises(AdsDataHubResponseStatusCodeError):
            client.customer(customer_id).validate(
                "SELECT @value as value",
            )

    def test_validate_with_parameter(
        self,
        client: adsdatahub.Client,
        customer_id: CustomerId,
    ):
        client.customer(customer_id).validate(
            "SELECT @value as value",
            {"value": 1},
        )
