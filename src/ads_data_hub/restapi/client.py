from typing import Any, assert_never, cast

import httpx
from typing_extensions import Unpack, overload

from ads_data_hub.restapi.resources import analysis_query, operations


class Client:
    def __init__(self) -> None:
        self._http_client = httpx.Client()

    @overload
    def request(
        self,
        resource_name: analysis_query.ResourceName,
        **params: Unpack[analysis_query.QueryParameters],
    ) -> analysis_query.Resource:
        """
        Ads Data Hub 内で実行できる分析クエリを定義します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/startTransient?hl=ja
        """
        ...

    @overload
    def request(
        self,
        resource_name: operations.ResourceName,
        **params: Unpack[operations.QueryParameters],
    ) -> operations.Resource:
        """
        このリソースは、ネットワーク API 呼び出しの結果である長時間実行オペレーションを表します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations?hl=ja
        """
        ...

    def request(
        self,
        resource_name: analysis_query.ResourceName | operations.ResourceName,
        **params: Any,
    ) -> analysis_query.Resource | operations.Resource:
        match resource_name:
            case "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries":
                return analysis_query.Resource(
                    self._http_client, cast(analysis_query.QueryParameters, params)
                )
            case "https://adsdatahub.googleapis.com/v1/operations/{operation_id}":
                return operations.Resource(
                    self._http_client, cast(operations.QueryParameters, params)
                )
            case _:
                assert_never(resource_name)
