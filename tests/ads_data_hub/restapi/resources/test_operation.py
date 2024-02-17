import datetime
from typing import Callable

import ads_data_hub.restapi
import pytest
from ads_data_hub.restapi.resources import operations

OperationId = str

OperationResourceGetter = Callable[[OperationId], operations.Resource]


class TestOperations:
    @pytest.fixture
    def get_operations_resource(
        self, restapi_client: ads_data_hub.restapi.Client
    ) -> Callable[[OperationId], operations.Resource]:
        return lambda operation_id: restapi_client.request(
            "https://adsdatahub.googleapis.com/v1/operations/{operation_id}",
            operation_id=operation_id,
        )

    def test_wait(self, get_operations_resource: OperationResourceGetter):
        with pytest.raises(NotImplementedError):
            get_operations_resource("1234").wait(timeout=datetime.timedelta(seconds=1))
