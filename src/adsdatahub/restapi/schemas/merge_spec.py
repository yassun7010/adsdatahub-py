from typing import Annotated

from pydantic import Field
from typing_extensions import TypedDict

from adsdatahub.restapi.schemas._model import ExtraForbidModel
from adsdatahub.restapi.schemas.merge_column import MergeColumnDict, MergeColumnModel


class MergeSpecDict(TypedDict):
    columns: dict[str, MergeColumnDict]


class MergeSpecModel(ExtraForbidModel):
    columns: Annotated[dict[str, MergeColumnModel], Field(default_factory=dict)]
