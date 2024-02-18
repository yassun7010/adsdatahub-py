from typing import Annotated, Literal, TypedDict

import httpx
from typing_extensions import Doc, Unpack

from adsdatahub.restapi._helpers import parse_response_body, snake2camel
from adsdatahub.restapi.resources.analysis_queries.list import (
    AnalysisQueryListQueryParams,
    AnalysisQueryListResponse,
)
from adsdatahub.restapi.schemas.analysis_queries_start_transient import (
    AnalysisQueriesStartTransient,
)
from adsdatahub.restapi.schemas.analysis_query import AnalysisQuery

ResourceName = Literal[
    "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries"
]
RESOURCE_NAME: ResourceName = (
    "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries"
)


class PathParameters(TypedDict):
    customer_id: str


class Resource:
    def __init__(self, http: httpx.Client, path_parameters: PathParameters) -> None:
        self._http = http
        self._base_url = RESOURCE_NAME.format(**path_parameters)

    def create(
        self,
        parent: Annotated[str, Doc("クエリを所有する親リソース名。")],
        query: AnalysisQuery,
    ) -> None:
        """
        後で実行するための分析クエリを作成します。
        現時点では、クエリの検証は行われません。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/create?hl=ja
        """

        raise NotImplementedError()

    def list(
        self,
        **query_params: Unpack[AnalysisQueryListQueryParams],
    ) -> AnalysisQueryListResponse:
        """
        指定した顧客が所有する分析クエリを一覧表示します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/list?hl=ja
        """
        return parse_response_body(
            AnalysisQueryListResponse,
            self._http.request(
                "GET", self._base_url, params=snake2camel(**query_params)
            ),
        )

    def start_transient(self, params: AnalysisQueriesStartTransient, /):
        """
        一時的な分析クエリで実行を開始します。
        結果は、指定した BigQuery 宛先テーブルに書き込まれます。
        返されたオペレーション名を使用して、クエリ完了ステータスをポーリングできます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/startTransient?hl=ja
        """
        raise NotImplementedError()

    def validate(self, parent: str):
        """
        提供された分析クエリに対して静的検証チェックを実行します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/validate?hl=ja
        """
        raise NotImplementedError()
