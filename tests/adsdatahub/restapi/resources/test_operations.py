from typing import Callable

import adsdatahub.restapi
from adsdatahub.exceptions import (
    AdsDataHubUnavailableError,
    AdsDataHubUnimplementedError,
)
from adsdatahub.restapi.resources import operation
from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.operation import OperationModel

OperationId = str

OperationResourceGetter = Callable[[OperationId], operation.Resource]


class Operations(Model):
    operations: list[OperationModel]


class TestOperations:
    def test_list(self, restapi_client: adsdatahub.restapi.Client):
        try:
            restapi_client.resource(
                "https://adsdatahub.googleapis.com/v1/operations"
            ).list()

        except (AdsDataHubUnimplementedError, AdsDataHubUnavailableError):
            # NOTE: たまに 503 が返ってくることがある。
            pass
