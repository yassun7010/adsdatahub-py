from typing import Literal, TypedDict

import httpx

from adsdatahub.restapi._helpers import parse_response_body
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

    def get(self) -> AnalysisQueryModel:
        """
        リクエストされた分析クエリを取得します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/get?hl=ja
        """
        return parse_response_body(
            AnalysisQueryModel,
            self._http.request("GET", self._base_url),
        )
