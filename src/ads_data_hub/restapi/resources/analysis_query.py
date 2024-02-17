from typing import Annotated, Literal, TypedDict

import httpx
from httpx._types import QueryParamTypes
from typing_extensions import Doc

from ads_data_hub.restapi.schemas.analysis_queries_start import (
    AnalysisQueriesStartDict,
    AnalysisQueriesStartModel,
)
from ads_data_hub.restapi.schemas.analysis_queries_start_transient import (
    AnalysisQueriesStartTransient,
)
from ads_data_hub.restapi.schemas.analysis_query import AnalysisQuery

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

    def delete(self, name: str) -> None:
        """
        分析クエリを削除します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/delete?hl=ja
        """
        raise NotImplementedError()

    def get(self, name: str) -> None:
        """
        リクエストされた分析クエリを取得します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/get?hl=ja
        """
        raise NotImplementedError()

    def list(
        self,
        page_size: Annotated[
            int | None,
            Doc(
                "返される最大アイテム数。0 の場合、サーバーは返されるクエリの数を決定します。"
            ),
        ] = None,
        page_token: Annotated[
            str | None,
            Doc(
                "前の呼び出しによって返されたページトークン。次のページの結果を返すために使用されます。"
            ),
        ] = None,
        filter: Annotated[
            str | None,
            Doc(
                """
                レスポンスをフィルタします。

                次のフィールド / 形式を使用します。
                name=”customers/271828/analysisQueries/pi314159265359” title=”up_and_right” queryText="SELECT LN(2.7182818284);" queryState="RUNNABLE"createTime>updateTime>updateTime>updateTime>updateTime>update_time
                """
            ),
        ] = None,
    ) -> httpx.Response:
        """
        指定した顧客が所有する分析クエリを一覧表示します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/list?hl=ja
        """
        query_params: QueryParamTypes = {}
        if page_size is not None:
            query_params["pageSize"] = page_size
        if page_token is not None:
            query_params["pageToken"] = page_token
        if filter is not None:
            query_params["filter"] = filter

        return self._http.request("GET", self._base_url, params=query_params)

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

    def start_transient(self, params: AnalysisQueriesStartTransient, /):
        """
        一時的な分析クエリで実行を開始します。
        結果は、指定した BigQuery 宛先テーブルに書き込まれます。
        返されたオペレーション名を使用して、クエリ完了ステータスをポーリングできます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/startTransient?hl=ja
        """
        _response = self._http.post(
            "/v1/customers.analysisQueries:startTransient", json=params
        )

    def validate(self, parent: str):
        """
        提供された分析クエリに対して静的検証チェックを実行します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/validate?hl=ja
        """
