from typing import Union, assert_never, overload

from typing_extensions import override

from adsdatahub.restapi import http
from adsdatahub.restapi.client import Client
from adsdatahub.restapi.resources import (
    analysis_queries,
    analysis_query,
    operation,
    operations,
)


class MockClient(Client):
    def __init__(self) -> None:
        self._http_internal = http.MockClient()

    @property
    @override
    def _http(self) -> http.MockClient:
        return self._http_internal

    @overload
    def inject_response(
        self, resource_name: analysis_queries.ResourceName
    ) -> analysis_queries.MockResource: ...

    @overload
    def inject_response(
        self, resource_name: analysis_query.ResourceName
    ) -> analysis_query.MockResource: ...

    @overload
    def inject_response(
        self, resource_name: operations.ResourceName
    ) -> operations.MockResource: ...

    @overload
    def inject_response(
        self, resource_name: operation.ResourceName
    ) -> operation.MockResource: ...

    def inject_response(
        self,
        resource_name: Union[
            analysis_queries.ResourceName,
            analysis_query.ResourceName,
            operations.ResourceName,
            operation.ResourceName,
        ],
    ) -> Union[
        analysis_queries.MockResource,
        analysis_query.MockResource,
        operations.MockResource,
        operation.MockResource,
    ]:
        match resource_name:
            case analysis_queries.RESOURCE_NAME:
                return analysis_queries.MockResource(self)
            case analysis_query.RESOURCE_NAME:
                return analysis_query.MockResource(self)
            case operations.RESOURCE_NAME:
                return operations.MockResource(self)
            case operation.RESOURCE_NAME:
                return operation.MockResource(self)
            case _ as unreachable:
                assert_never(unreachable)
