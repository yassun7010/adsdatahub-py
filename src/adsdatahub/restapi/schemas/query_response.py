from typing import Annotated

from pydantic import Field

from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.destination_table_info import DestinationTableInfoModel
from adsdatahub.restapi.schemas.output_artifacts import OutputArtifactsModel
from adsdatahub.restapi.schemas.privacy_message import PrivacyMessageModel


class QueryResponseModel(Model):
    """
    クエリ実行ジョブが成功すると、レスポンスが返されます。
    これは、クエリ実行リクエストによって返される google.longrunning.Operation のレスポンス フィールドに保存されます。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/QueryResponse?hl=ja
    """

    row_count: Annotated[
        int,
        Field(alias="rowCount"),
    ]

    destination_tables: Annotated[
        list[DestinationTableInfoModel],
        Field(alias="destinationTables", default_factory=list),
    ]

    output_artifacts: Annotated[
        OutputArtifactsModel,
        Field(alias="outputArtifacts"),
    ]

    privacy_messages: Annotated[
        list[PrivacyMessageModel],
        Field(alias="privacyMessages", default_factory=list),
    ]
