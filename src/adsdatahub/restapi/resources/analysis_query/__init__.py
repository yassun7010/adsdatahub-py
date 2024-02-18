from typing import Annotated, Literal, TypedDict

import httpx
from httpx._types import QueryParamTypes
from typing_extensions import Doc, Unpack

from adsdatahub.restapi.resources.analysis_query.list import (
    AnalysisQueryListQueryParams,
    AnalysisQueryResponse,
)
from adsdatahub.restapi.schemas.analysis_queries_start import (
    AnalysisQueriesStartDict,
    AnalysisQueriesStartModel,
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
        **query_params: Unpack[AnalysisQueryListQueryParams],
    ) -> AnalysisQueryResponse:
        """
        指定した顧客が所有する分析クエリを一覧表示します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/list?hl=ja
        """
        _query_params: QueryParamTypes = {}
        if page_size := query_params.get("page_size"):
            _query_params["pageSize"] = page_size
        if page_token := query_params.get("page_token"):
            _query_params["pageToken"] = page_token
        if filter := query_params.get("filter"):
            _query_params["filter"] = filter

        response = self._http.request("GET", self._base_url, params=_query_params)
        if response.status_code != 200:
            raise Exception(response.json())

        with open("response.json", "w") as f:
            f.write(response.content.decode("utf-8"))
        return AnalysisQueryResponse.model_validate_json(response.content)

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