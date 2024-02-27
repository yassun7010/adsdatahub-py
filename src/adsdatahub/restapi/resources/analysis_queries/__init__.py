from typing import Any, Literal, TypedDict

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
from adsdatahub.restapi.schemas.operation import OperationModel
from adsdatahub.restapi.schemas.query_execution_spec import (
    QueryExecutionSpecRequestModel,
)
from adsdatahub.restapi.schemas.query_metadata import QueryMetadataModel

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
        self, **request_body: Unpack[AnalysisQueriesStartTransientQueryParams]
    ) -> OperationModel[QueryMetadataModel]:
        """
        一時的な分析クエリで実行を開始します。
        結果は、指定した BigQuery 宛先テーブルに書き込まれます。
        返されたオペレーション名を使用して、クエリ完了ステータスをポーリングできます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/startTransient?hl=ja
        """
        query = request_body["query"]
        spec = request_body["spec"]

        return parse_response_body(
            OperationModel[QueryMetadataModel],
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
                    "destTable": request_body["dest_table"],
                },
            ),
        )

    def validate(
        self, **request_body: Unpack[AnalysisQueriesValidateQueryParams]
    ) -> AnalysisQueriesValidateResponseBody:
        """
        提供された分析クエリに対して静的検証チェックを実行します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/validate?hl=ja
        """
        query = request_body["query"]
        json_value: dict[str, Any] = {
            "query": (
                AnalysisQueryRequestOptionalTitleModel.model_validate(query)
                if isinstance(query, dict)
                else query
            ).model_dump(),
        }

        if ads_data_customer_id := request_body.get("ads_data_customer_id"):
            json_value["adsDataCustomerId"] = ads_data_customer_id

        if match_data_customer_id := request_body.get("match_data_customer_id"):
            json_value["matchDataCustomerId"] = match_data_customer_id

        if spec := request_body.get("spec"):
            json_value["spec"] = (
                QueryExecutionSpecRequestModel.model_validate(spec)
                if isinstance(spec, dict)
                else spec
            ).model_dump()

        if include_performance_info := request_body.get("include_performance_info"):
            json_value["includePerformanceInfo"] = include_performance_info

        return parse_response_body(
            AnalysisQueriesValidateResponseBody,
            self._http.request(
                "POST",
                f"{self._base_url}:validate",
                json=json_value,
            ),
        )
