from typing import Annotated

from pydantic import Field
from typing_extensions import TypedDict, deprecated

from ads_data_hub.restapi.schemas._model import ExtraForbidModel
from ads_data_hub.restapi.schemas.merge_column import MergeColumnModel


@deprecated('"mergeSpec" is deprecated, use "FilteredRowSummary" instead')
class MergeSpecDict(TypedDict):
    pass


@deprecated('"mergeSpec" is deprecated, use "FilteredRowSummary" instead')
class MergeSpecModel(ExtraForbidModel):
    columns: Annotated[dict[str, MergeColumnModel], Field(default_factory=dict)]
