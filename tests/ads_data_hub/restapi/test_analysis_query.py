import pytest
from ads_data_hub.restapi.client import Client


class TestAnalysisQuery:
    def test_start(self):
        with pytest.raises(NotImplementedError):
            Client().request(
                "https://adsdatahub.googleapis.com/v1/operations/{operation_id}",
                operation_id="aaa",
            ).wait()
