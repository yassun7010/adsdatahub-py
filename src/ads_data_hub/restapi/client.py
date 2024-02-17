from typing import assert_never

import httpx
from typing_extensions import overload

from ads_data_hub.restapi.resources import analysis_query, operations


class Client:
    def __init__(self) -> None:
        self._http_client = httpx.Client()

    @overload
    def request(
        self, resource_name: analysis_query.ResourceName
    ) -> analysis_query.Resource:
        """
        Ads Data Hub 内で実行できる分析クエリを定義します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/startTransient?hl=ja
        """
        ...

    @overload
    def request(self, resource_name: operations.ResourceName) -> operations.Resource:
        """
        このリソースは、ネットワーク API 呼び出しの結果である長時間実行オペレーションを表します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations?hl=ja
        """
        ...

    def request(
        self, resource_name: analysis_query.ResourceName | operations.ResourceName
    ) -> analysis_query.Resource | operations.Resource:
        match resource_name:
            case "customers.analysisQueries":
                return analysis_query.Resource(self._http_client)
            case "operations":
                return operations.Resource(self._http_client)
            case _:
                assert_never(resource_name)
