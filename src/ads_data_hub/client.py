from ads_data_hub.restapi.resources.analysis_query import AnalysisQueriesResource
from ads_data_hub.restapi.resources.operations import OperationsResource


class Client:
    def __init__(self, project_id: str) -> None:
        pass

    def analysis_queries(self, parent: str) -> AnalysisQueriesResource:
        """
        Ads Data Hub 内で実行できる分析クエリを定義します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/startTransient?hl=ja
        """
        return AnalysisQueriesResource(parent)

    def operations(self, name: str) -> OperationsResource:
        """
        このリソースは、ネットワーク API 呼び出しの結果である長時間実行オペレーションを表します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations?hl=ja
        """
        return OperationsResource()
