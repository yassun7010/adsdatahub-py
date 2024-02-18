from typing_extensions import TypedDict

from adsdatahub.restapi.schemas._model import ExtraForbidModel

from .field_type import FieldType
from .parameter_value import ParameterValueDict, ParameterValueModel


class ParameterTypeDict(TypedDict):
    """
    特定のクエリ パラメータに関する情報。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/ParameterType?hl=ja
    """

    type: FieldType

    description: str

    defaultValue: ParameterValueDict


class ParameterTypeModel(ExtraForbidModel):
    type: FieldType
    description: str | None = None
    defaultValue: ParameterValueModel