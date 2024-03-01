import os
from textwrap import dedent

import adsdatahub.restapi
import pytest
from adsdatahub._types import CustomerId

SLEEP_TIME_SEC = 3


@pytest.fixture
def client() -> adsdatahub.Client:
    return adsdatahub.Client(
        customer_id=os.environ["ADS_DATA_HUB_CUSTOMER_ID"],
        client_options={
            "credentials_file": os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        },
    )


@pytest.fixture
def restapi_client():
    return adsdatahub.restapi.Client(
        client_options={
            "credentials_file": os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        }
    )


@pytest.fixture
def mock_restapi_client():
    return adsdatahub.restapi.MockClient()


@pytest.fixture
def customer_id() -> CustomerId:
    return os.environ["ADS_DATA_HUB_CUSTOMER_ID"]


@pytest.fixture
def project() -> str:
    return os.environ["PROJECT"]


@pytest.fixture
def dataset() -> str:
    return os.environ["DATASET"]


@pytest.fixture
def imp_query_text() -> str:
    return dedent(
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
    )
