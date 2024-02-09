from typing_extensions import TypedDict


class ArrayValue(TypedDict):
    values: list["ParameterValue"]


class StructValue(TypedDict):
    values: dict[str, "ParameterValue"]


ParameterValue = str | ArrayValue | StructValue
