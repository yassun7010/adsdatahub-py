from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.query_metadata import QueryMetadataModel
from adsdatahub.restapi.schemas.query_response import QueryResponseModel
from adsdatahub.restapi.schemas.status import StatusModel


class OperationModel(Model):
    name: str
    """
    サーバーによって割り当てられる名前。

    最初にその名前を返すサービスと同じサービス内でのみ一意になります。
    デフォルトの HTTP マッピングを使用している場合は、name を operations/{unique_id} で終わるリソース名にします。
    """

    metadata: QueryMetadataModel

    done: bool = False

    error: StatusModel

    response: QueryResponseModel
