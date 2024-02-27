from typing import Annotated, NotRequired, TypedDict

from pydantic import Field

from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.operation import OperationModel
from adsdatahub.restapi.schemas.query_metadata import QueryMetadataModel


class OperationsListQueryParams(TypedDict):
    filter: NotRequired[str | None]
    pageSize: NotRequired[int | None]
    pageToken: NotRequired[str | None]


class OperationsListResponseBody(Model):
    operations: Annotated[
        list[OperationModel[QueryMetadataModel]], Field(default_factory=list)
    ]
    """
    リクエストで指定されたフィルタに一致するオペレーションのリスト。
    """

    next_page_token: Annotated[str | None, Field(alias="nextPageToken")] = None
    """
    標準的なリストの次ページのトークン。
    """
