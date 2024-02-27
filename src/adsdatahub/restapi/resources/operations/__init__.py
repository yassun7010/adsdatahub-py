from typing import Literal, TypedDict

import httpx

from adsdatahub.restapi._helpers import parse_response_body
from adsdatahub.restapi.resources.operations.list import (
    OperationsListQueryParams,
    OperationsListResponseBody,
)

ResourceName = Literal["https://adsdatahub.googleapis.com/v1/operations"]
RESOURCE_NAME: ResourceName = "https://adsdatahub.googleapis.com/v1/operations"


class PathParameters(TypedDict):
    pass


class Resource:
    """
    このリソースは、ネットワーク API 呼び出しの結果である長時間実行オペレーションを表します。
    """

    def __init__(self, client: httpx.Client, path_params: PathParameters) -> None:
        self._client = client
        self._base_url = RESOURCE_NAME.format(**path_params)

    def list(
        self, query_params: OperationsListQueryParams | None = None
    ) -> OperationsListResponseBody:
        """
        リクエストで指定されたフィルタに一致するオペレーションをリストします。
        このメソッドがサーバーでサポートされていない場合は、UNIMPLEMENTED を返します。

        注: name バインディングを使用すると、users/*/operations などの異なるリソース名スキームを使用するために、API サービスがバインディングをオーバーライドできます。
        バインディングをオーバーライドするときに、API サービスは "/v1/{name=users/*}/operations" のようなバインディングをサービス構成に追加する場合があります。
        下位互換性を維持するため、デフォルトの名前にはオペレーションのコレクション ID が含まれています。
        ただし、オーバーライドを行うユーザーは、名前のバインディングが親リソースであり、オペレーション コレクション ID がないことを確認する必要があります。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/list?hl=ja
        """

        return parse_response_body(
            OperationsListResponseBody,
            self._client.request(
                "GET",
                self._base_url,
                params={k: v for k, v in (query_params or {}) if v is not None},
            ),
        )
