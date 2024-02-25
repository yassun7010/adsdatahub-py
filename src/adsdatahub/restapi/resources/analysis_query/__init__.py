from typing import Literal, TypedDict, Unpack

import httpx

from adsdatahub.restapi._helpers import parse_response_body
from adsdatahub.restapi.resources.analysis_query.start import (
    AnalysisQueryStartRequestBody,
)
from adsdatahub.restapi.schemas.analysis_query import (
    AnalysisQueryModel,
    AnalysisQueryRequestDict,
    AnalysisQueryRequestModel,
)
from adsdatahub.restapi.schemas.operation import OperationModel
from adsdatahub.restapi.schemas.query_execution_spec import (
    QueryExecutionSpecRequestModel,
)
from adsdatahub.restapi.schemas.query_metadata import QueryMetadataModel

ResourceName = Literal[
    "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}"
]
RESOURCE_NAME: ResourceName = "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries/{resource_id}"


class PathParameters(TypedDict):
    customer_id: int
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
        return parse_response_body(
            None,
            self._http.request("DELETE", self._base_url),
        )

    def get(self) -> AnalysisQueryModel:
        """
        リクエストされた分析クエリを取得します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/get?hl=ja
        """
        return parse_response_body(
            AnalysisQueryModel,
            self._http.request("GET", self._base_url),
        )

    def patch(
        self, request_body: AnalysisQueryRequestModel | AnalysisQueryRequestDict
    ) -> AnalysisQueryModel:
        """
        既存の分析クエリを更新します。部分更新はサポートされています。次のクエリ フィールドは、この方法では更新できないため、無視されます。

        - queryState
        - createTime
        - createEmail（作成メール）
        - updateTime
        - updateEmail

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/patch?hl=ja
        """
        return parse_response_body(
            AnalysisQueryModel,
            self._http.request(
                "PATCH",
                self._base_url,
                json=(
                    AnalysisQueryRequestModel.model_validate(request_body)
                    if isinstance(request_body, dict)
                    else request_body
                ).model_dump(),
            ),
        )

    def start(
        self, **request_body: Unpack[AnalysisQueryStartRequestBody]
    ) -> OperationModel[QueryMetadataModel]:
        """
        保存された分析クエリの実行を開始します。
        結果は、指定した BigQuery 宛先テーブルに書き込まれます。
        返されたオペレーション名を使用して、クエリ完了ステータスをポーリングできます。

        Refarence: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/start?hl=ja
        """
        spec = request_body["spec"]

        json_value = {
            "spec": (
                QueryExecutionSpecRequestModel.model_validate(spec)
                if isinstance(spec, dict)
                else spec
            ).model_dump(),
            "destTable": request_body["dest_table"],
        }

        if customer_id := request_body.get("customer_id"):
            json_value["customerId"] = customer_id

        return parse_response_body(
            OperationModel[QueryMetadataModel],
            self._http.request(
                "POST",
                f"{self._base_url}:start",
                json=json_value,
            ),
        )
