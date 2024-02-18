from typing_extensions import TypedDict

from adsdatahub.restapi.schemas._model import ExtraForbidModel


class ValueDict(TypedDict):
    value: str


class ArrayValueDict(TypedDict):
    arrayValue: "ArrayValueValuesDict"


class ArrayValueValuesDict(TypedDict):
    values: list["ParameterValueDict"]


class StructValueDict(TypedDict):
    structValue: "StructValueValuesDict"


class StructValueValuesDict(TypedDict):
    values: dict[str, "ParameterValueDict"]


ParameterValueDict = ValueDict | ArrayValueDict | StructValueDict


class ValueModel(ExtraForbidModel):
    value: str


class ArrayValueModel(ExtraForbidModel):
    arrayValue: "ArrayValueValuesModel"


class ArrayValueValuesModel(TypedDict):
    values: list["ParameterValueModel"]


class StructValueModel(TypedDict):
    structValue: "StructValueValuesModel"


class StructValueValuesModel(TypedDict):
    values: dict[str, "ParameterValueModel"]


ParameterValueModel = ValueModel | ArrayValueModel | StructValueModel
