from typing import Literal, TypedDict

import httpx

from adsdatahub.restapi._helpers import convert_json_value, parse_response_body
from adsdatahub.restapi.resources.analysis_queries.list import (
    AnalysisQueryListQueryParams,
    AnalysisQueryListResponse,
)
from adsdatahub.restapi.resources.analysis_queries.start_transient import (
    AnalysisQueriesStartTransientQueryParams,
)
from adsdatahub.restapi.resources.analysis_queries.validate import (
    AnalysisQueriesValidateQueryParams,
    AnalysisQueriesValidateResponseBody,
)
from adsdatahub.restapi.schemas._newtype import CustomerId
from adsdatahub.restapi.schemas.analysis_query import (
    AnalysisQueryModel,
    AnalysisQueryRequest,
    AnalysisQueryRequestModel,
    AnalysisQueryRequestOptionalTitleModel,
)
from adsdatahub.restapi.schemas.analysis_query_metadata import (
    AnalysisQueryMetadataModel,
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
    customer_id: CustomerId


class Resource:
    def __init__(self, http: httpx.Client, path_parameters: PathParameters) -> None:
        self._http = http
        self._base_url = RESOURCE_NAME.format(**path_parameters)

    def create(
        self,
        request_body: AnalysisQueryRequest,
    ) -> AnalysisQueryModel:
        """
        後で実行するための分析クエリを作成します。
        現時点では、クエリの検証は行われません。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/create?hl=ja
        """
        if isinstance(request_body, dict):
            request_body = AnalysisQueryRequestModel.model_validate(request_body)

        return parse_response_body(
            AnalysisQueryModel,
            self._http.request("POST", self._base_url, json=request_body.model_dump()),
        )

    def list(
        self,
        query_params: AnalysisQueryListQueryParams | None = None,
    ) -> AnalysisQueryListResponse:
        """
        指定した顧客が所有する分析クエリを一覧表示します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/list?hl=ja
        """
        return parse_response_body(
            AnalysisQueryListResponse,
            self._http.request(
                "GET",
                self._base_url,
                params={k: v for k, v in (query_params or {}) if v is not None},
            ),
        )

    def start_transient(
        self, request_body: AnalysisQueriesStartTransientQueryParams
    ) -> OperationModel[AnalysisQueryMetadataModel]:
        """
        一時的な分析クエリで実行を開始します。
        結果は、指定した BigQuery 宛先テーブルに書き込まれます。
        返されたオペレーション名を使用して、クエリ完了ステータスをポーリングできます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/startTransient?hl=ja
        """

        return parse_response_body(
            OperationModel[AnalysisQueryMetadataModel],
            self._http.request(
                "POST",
                f"{self._base_url}:startTransient",
                json=convert_json_value(
                    request_body,
                    model_map={
                        "query": AnalysisQueryRequestOptionalTitleModel,
                        "spec": QueryExecutionSpecRequestModel,
                    },
                ),
            ),
        )

    def validate(
        self, request_body: AnalysisQueriesValidateQueryParams
    ) -> AnalysisQueriesValidateResponseBody:
        """
        提供された分析クエリに対して静的検証チェックを実行します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/validate?hl=ja
        """
        return parse_response_body(
            AnalysisQueriesValidateResponseBody,
            self._http.request(
                "POST",
                f"{self._base_url}:validate",
                json=convert_json_value(
                    request_body,
                    model_map={
                        "query": AnalysisQueryRequestOptionalTitleModel,
                        "spec": QueryExecutionSpecRequestModel,
                    },
                ),
            ),
        )
