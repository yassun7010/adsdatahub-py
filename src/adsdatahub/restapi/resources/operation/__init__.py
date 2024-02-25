import datetime
from typing import Any, Literal, TypedDict, Unpack

import httpx

from adsdatahub.restapi._helpers import (
    parse_response_body,
    validate_response_status_code,
)
from adsdatahub.restapi.resources.operation.wait import OperationWaitRequestBody
from adsdatahub.restapi.schemas._newtype import UniqueId
from adsdatahub.restapi.schemas.operation import OperationModel
from adsdatahub.restapi.schemas.query_metadata import (
    QueryMetadataModel,
    QueryMetadataWithQueryTextModel,
)

ResourceName = Literal["https://adsdatahub.googleapis.com/v1/operations/{unique_id}"]
RESOURCE_NAME: ResourceName = (
    "https://adsdatahub.googleapis.com/v1/operations/{unique_id}"
)


class PathParameters(TypedDict):
    unique_id: UniqueId


class Resource:
    """
    このリソースは、ネットワーク API 呼び出しの結果である長時間実行オペレーションを表します。
    """

    def __init__(self, client: httpx.Client, path_parameters: PathParameters) -> None:
        self._client = client
        self._base_url = RESOURCE_NAME.format(**path_parameters)

    def cancel(self):
        """
        長時間実行オペレーションの非同期キャンセルを開始します。
        サーバーは操作のキャンセルに全力を尽くしますが、成功は保証されません。
        このメソッドがサーバーでサポートされていない場合は、google.rpc.Code.UNIMPLEMENTED を返します。
        クライアントは Operations.GetOperation などのメソッドを使用して、キャンセルが成功したか、あるいはキャンセルしたにもかかわらずオペレーションが完了したかを確認できます。
        キャンセルが成功するとそのオペレーションは削除されず、google.rpc.Status.code が 1 の Operation.error 値を持つオペレーションになります。
        これは Code.CANCELLED に相当します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/cancel?hl=ja
        """
        return validate_response_status_code(
            self._client.request("POST", f"{self._base_url}:cancel"),
        )

    def delete(self) -> None:
        """
        長時間実行オペレーションを削除します。
        このメソッドは、クライアントがそのオペレーション結果に関心がなくなったことを表しています。
        このメソッドではオペレーションはキャンセルされません。
        このメソッドがサーバーでサポートされていない場合は、google.rpc.Code.UNIMPLEMENTED を返します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/delete?hl=ja
        """

        return validate_response_status_code(
            self._client.request("DELETE", self._base_url),
        )

    def get(self) -> OperationModel[QueryMetadataWithQueryTextModel]:
        """
        長時間実行オペレーションの最新の状態を取得します。
        クライアントはこのメソッドを使用して、API サービスで推奨される間隔でオペレーションの結果をポーリングできます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/get?hl=ja
        """

        return parse_response_body(
            OperationModel[QueryMetadataWithQueryTextModel],
            self._client.request("GET", self._base_url),
        )

    def wait(
        self, **request_body: Unpack[OperationWaitRequestBody]
    ) -> OperationModel[QueryMetadataModel]:
        """
        指定した長時間実行オペレーションが完了するか、指定したタイムアウトに達するまで待機し、最新の状態を返します。

        オペレーションがすでに完了している場合は、すぐに最新の状態が返されます。
        指定されたタイムアウトがデフォルトの HTTP/RPC タイムアウトを上回る場合は、HTTP/RPC タイムアウトが使用されます。
        サーバーがこのメソッドをサポートしていない場合は、google.rpc.Code.UNIMPLEMENTED を返します。
        このメソッドはベスト エフォートに基づきます。
        指定されたタイムアウト（直前を含む）の前に最新の状態を返すことがあります。
        つまり、すぐにレスポンスがあったとしても、オペレーションが完了したことを保証するものではありません。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/wait?hl=ja
        """
        json_value: dict[str, Any] = {}

        if timeout := request_body.get("timeout"):
            match timeout:
                case str():
                    timeout_sec = timeout
                case int() | float():
                    timeout_sec = f"{timeout}s"
                case datetime.timedelta():
                    timeout_sec = f"{timeout.total_seconds()}s"
            json_value["timeout"] = timeout_sec

        return parse_response_body(
            OperationModel[QueryMetadataModel],
            self._client.request("POST", f"{self._base_url}:wait", json=json_value),
        )
