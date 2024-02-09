from typing_extensions import TypedDict, deprecated

from ads_data_hub.restapi.schemas._model import ExtraForbidModel


@deprecated('"mergeSpec" is deprecated, use "FilteredRowSummary" instead')
class MergeSpecDict(TypedDict):
    pass


@deprecated('"mergeSpec" is deprecated, use "FilteredRowSummary" instead')
class MergeSpecModel(ExtraForbidModel):
    pass
