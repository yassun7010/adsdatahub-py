import os

import adsdatahub.restapi
import pytest


@pytest.fixture
def restapi_client():
    return adsdatahub.restapi.Client(
        client_options={
            "credentials_file": os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        }
    )


@pytest.fixture
def customer_id() -> int:
    return int(os.environ["ADS_DATA_HUB_CUSTOMER_ID"])


@pytest.fixture
def project() -> str:
    return os.environ["PROJECT"]


@pytest.fixture
def dataset() -> str:
    return os.environ["DATASET"]
