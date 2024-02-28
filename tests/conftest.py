import os

import adsdatahub.restapi
import pytest
from adsdatahub.restapi.schemas._newtype import CustomerId

SLEEP_TIME_SEC = 3


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
