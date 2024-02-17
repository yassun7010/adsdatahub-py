import pytest
from ads_data_hub.restapi.client import Client


class TestAnalysisQuery:
    def test_start(self):
        with pytest.raises(NotImplementedError):
            Client().request("operations").wait(name="aaa")
