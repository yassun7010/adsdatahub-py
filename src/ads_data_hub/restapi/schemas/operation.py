from ads_data_hub.restapi.schemas._model import Model
from ads_data_hub.restapi.schemas.query_metadata import QueryMetadataModel
from ads_data_hub.restapi.schemas.query_response import QueryResponseModel
from ads_data_hub.restapi.schemas.status import StatusModel


class OperationModel(Model):
    name: str

    metadata: QueryMetadataModel

    done: bool = False

    error: StatusModel

    response: QueryResponseModel
