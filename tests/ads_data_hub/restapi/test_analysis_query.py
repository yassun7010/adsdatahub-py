from ads_data_hub.restapi.client import Client


class TestAnalysisQuery:
    def test_start(self):
        Client().request("operations").wait(name="aaa")
