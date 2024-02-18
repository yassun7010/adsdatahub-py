from typing import Literal, TypedDict

import httpx

from adsdatahub.restapi._helpers import parse_response_body
from adsdatahub.restapi.schemas.analysis_queries_start import (
    AnalysisQueriesStartDict,
    AnalysisQueriesStartModel,
)
from adsdatahub.restapi.schemas.analysis_query import AnalysisQueryModel

ResourceName = Literal[
    "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}"
]
RESOURCE_NAME: ResourceName = "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}"


class PathParameters(TypedDict):
    customer_id: str
    resource_id: str


class Resource:
    def __init__(self, http: httpx.Client, path_parameters: PathParameters) -> None:
        self._http = http
        self._base_url = RESOURCE_NAME.format(**path_parameters)

    def delete(self) -> None:
        """
        分析クエリを削除します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/delete?hl=ja
        """
        raise NotImplementedError()

    def get(self) -> AnalysisQueryModel:
        """
        リクエストされた分析クエリを取得します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/get?hl=ja
        """
        return parse_response_body(
            AnalysisQueryModel,
            self._http.request("GET", self._base_url),
        )

    def patch(self, name: str) -> None:
        """
        既存の分析クエリを更新します。部分更新はサポートされています。次のクエリ フィールドは、この方法では更新できないため、無視されます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/patch?hl=ja
        """

    def start(
        self, params: AnalysisQueriesStartDict | AnalysisQueriesStartModel
    ) -> None:
        """
        保存された分析クエリの実行を開始します。
        結果は、指定した BigQuery 宛先テーブルに書き込まれます。
        返されたオペレーション名を使用して、クエリ完了ステータスをポーリングできます。

        Refarence: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/start?hl=ja
        """
        raise NotImplementedError()
