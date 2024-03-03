import datetime
from typing import assert_never

from adsdatahub.restapi.schemas.field_type import (
    TypeDict,
)
from adsdatahub.restapi.schemas.parameter_type import (
    ParameterTypeDict,
)
from adsdatahub.restapi.schemas.parameter_value import ParameterValueDict, ValueDict

# TODO: 配列の型、デフォルト値などをサポートする必要があるが、後回し。
PythonParameterType = str | int | float | bool | datetime.date | datetime.datetime
"""
クエリのパラメータとして使える Python の型。
"""


def convert_param_types(
    params: dict[str, PythonParameterType],
) -> dict[str, ParameterTypeDict]:
    return {key: convert_parameter_type(value) for key, value in params.items()}


def convert_param_values(
    params: dict[str, PythonParameterType],
) -> dict[str, ParameterValueDict]:
    return {key: convert_parameter_value(value) for key, value in params.items()}


def convert_parameter_type(
    value: PythonParameterType,
) -> ParameterTypeDict:
    match value:
        case str():
            return ParameterTypeDict({"type": TypeDict({"type": "STRING"})})

        case int():
            return ParameterTypeDict({"type": TypeDict({"type": "INT64"})})

        case float():
            return ParameterTypeDict({"type": TypeDict({"type": "FLOAT64"})})

        case bool():
            return ParameterTypeDict({"type": TypeDict({"type": "BOOL"})})

        case datetime.date():
            return ParameterTypeDict({"type": TypeDict({"type": "DATE"})})

        case datetime.datetime():
            return ParameterTypeDict({"type": TypeDict({"type": "TIMESTAMP"})})

        case _ as unreachable:
            assert_never(unreachable)


def convert_parameter_value(value: PythonParameterType) -> ParameterValueDict:
    match value:
        case str():
            return ValueDict({"value": value})

        case int():
            return ValueDict({"value": str(value)})

        case float():
            return ValueDict({"value": str(value)})

        case bool():
            return ValueDict({"value": str(value)})

        case datetime.date():
            return ValueDict({"value": value.isoformat()})

        case datetime.datetime():
            return ValueDict({"value": value.isoformat()})

        case _ as unreachable:
            assert_never(unreachable)
