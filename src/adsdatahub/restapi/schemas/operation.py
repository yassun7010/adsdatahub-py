from typing import Generic, TypeVar

from pydantic import field_serializer, validator

from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.query_metadata import QueryMetadataModel
from adsdatahub.restapi.schemas.query_response import QueryResponseModel
from adsdatahub.restapi.schemas.status import StatusModel

GenericQueryMetadataModel = TypeVar(
    "GenericQueryMetadataModel", bound=QueryMetadataModel
)


class OperationNameModel(Model):
    unique_id: str


class OperationModel(Model, Generic[GenericQueryMetadataModel]):
    """
    このリソースは、ネットワーク API 呼び出しの結果である長時間実行オペレーションを表します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations?hl=ja#Operation
    """

    name: OperationNameModel
    """
    サーバーによって割り当てられる名前。

    最初にその名前を返すサービスと同じサービス内でのみ一意になります。
    デフォルトの HTTP マッピングを使用している場合は、name を operations/{unique_id} で終わるリソース名にします。
    """

    metadata: GenericQueryMetadataModel | None
    """
    オペレーションに関連付けられたサービス固有のデータを含む QueryMetadata オブジェクト。

    任意のデータ型のフィールドを含むオブジェクト。
    タイプを識別する URI を含むフィールド "@type" を追加できます。

    例: { "id": 1234, "@type": "types.example.com/standard/id" }
    """

    done: bool = False
    """
    値が false の場合は、オペレーションが進行中であることを意味します。

    true の場合、オペレーションは完了しており、error または response が利用可能です。
    """

    error: StatusModel | None = None
    """
    失敗またはキャンセルされた場合のオペレーションのエラー結果。
    """

    response: QueryResponseModel | None = None
    """
    クエリ オペレーションが成功した場合に返される QueryResponse オブジェクト。

    任意のデータ型のフィールドを含むオブジェクト。
    タイプを識別する URI を含むフィールド "@type" を追加できます。

    例: { "id": 1234, "@type": "types.example.com/standard/id" }
    """

    @validator("name", pre=True)
    @classmethod
    def _parse_name(cls, v: str) -> dict[str, str]:
        if not v.startswith("operations/"):
            raise ValueError(f"Invalid operation name: {v}")

        return {"unique_id": v[len("operations/") :]}

    @field_serializer("name")
    def _serialize_name(self, v: OperationNameModel) -> str:
        return f"operations/{v.unique_id}"
