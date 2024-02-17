import os

import ads_data_hub.restapi
import pytest


@pytest.fixture
def restapi_client():
    return ads_data_hub.restapi.Client(
        client_options={
            "credentials_file": os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        }
    )
