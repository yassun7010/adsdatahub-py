from typing import Callable

import adsdatahub.restapi
from adsdatahub.restapi.resources import operation
from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.operation import OperationModel

OperationId = str

OperationResourceGetter = Callable[[OperationId], operation.Resource]


class Operations(Model):
    operations: list[OperationModel]


class TestOperations:
    def test_list(self, restapi_client: adsdatahub.restapi.Client):
        restapi_client.request("https://adsdatahub.googleapis.com/v1/operations").list()
