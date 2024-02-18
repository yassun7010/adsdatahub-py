from typing_extensions import TypedDict


class Value(TypedDict):
    value: str


class ArrayValue(TypedDict):
    arrayValue: "ArrayValueValues"


class ArrayValueValues(TypedDict):
    values: list["ParameterValue"]


class StructValue(TypedDict):
    structValue: "StructValueValues"


class StructValueValues(TypedDict):
    values: dict[str, "ParameterValue"]


ParameterValue = Value | ArrayValue | StructValue
