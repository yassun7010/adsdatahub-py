from typing import Literal, TypedDict

import httpx
from typing_extensions import Unpack

from adsdatahub.restapi._helpers import parse_response_body, snake2camel
from adsdatahub.restapi.resources.analysis_queries.list import (
    AnalysisQueryListQueryParams,
    AnalysisQueryListResponse,
)
from adsdatahub.restapi.resources.analysis_queries.start_transient import (
    AnalysisQueriesStartTransientQueryParams,
)
from adsdatahub.restapi.schemas.analysis_query import (
    AnalysisQueryModel,
    AnalysisQueryRequest,
    AnalysisQueryRequestModel,
)
from adsdatahub.restapi.schemas.operation import OperationModel
from adsdatahub.restapi.schemas.query_execution_spec import (
    QueryExecutionSpecRequestModel,
)

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
        query: AnalysisQueryRequest,
    ) -> AnalysisQueryModel:
        """
        後で実行するための分析クエリを作成します。
        現時点では、クエリの検証は行われません。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/create?hl=ja
        """
        if isinstance(query, dict):
            query = AnalysisQueryRequestModel.model_validate(query)

        return parse_response_body(
            AnalysisQueryModel,
            self._http.request("POST", self._base_url, json=query.model_dump()),
        )

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

    def start_transient(
        self, **query_params: Unpack[AnalysisQueriesStartTransientQueryParams]
    ) -> OperationModel:
        """
        一時的な分析クエリで実行を開始します。
        結果は、指定した BigQuery 宛先テーブルに書き込まれます。
        返されたオペレーション名を使用して、クエリ完了ステータスをポーリングできます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/startTransient?hl=ja
        """
        query = query_params["query"]
        spec = query_params["spec"]

        return parse_response_body(
            OperationModel,
            self._http.request(
                "POST",
                f"{self._base_url}:startTransient",
                json={
                    "query": (
                        AnalysisQueryRequestModel.model_validate(query)
                        if isinstance(query, dict)
                        else query
                    ).model_dump(),
                    "spec": (
                        QueryExecutionSpecRequestModel.model_validate(spec)
                        if isinstance(spec, dict)
                        else spec
                    ).model_dump(),
                    "destTable": query_params["dest_table"],
                },
            ),
        )

    def validate(self, parent: str):
        """
        提供された分析クエリに対して静的検証チェックを実行します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/validate?hl=ja
        """
        raise NotImplementedError()
