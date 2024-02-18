import datetime
from typing import Callable

import adsdatahub.restapi
import pytest
from adsdatahub.restapi.resources import operations

OperationId = str

OperationResourceGetter = Callable[[OperationId], operations.Resource]


class TestOperations:
    @pytest.fixture
    def get_operations_resource(
        self, restapi_client: adsdatahub.restapi.Client
    ) -> Callable[[OperationId], operations.Resource]:
        return lambda operation_id: restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/operations/{operation_id}",
            operation_id=operation_id,
        )

    def test_wait(self, get_operations_resource: OperationResourceGetter):
        with pytest.raises(NotImplementedError):
            get_operations_resource("1234").wait(timeout=datetime.timedelta(seconds=1))
