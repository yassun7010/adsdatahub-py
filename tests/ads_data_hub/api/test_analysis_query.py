from ads_data_hub.client import Client


class TestAnalysisQuery:
    def test_start(self):
        Client("aitech-aoc-akagi-cdp-dev").analysis_queries(
            "customers/1000000000"
        ).start
