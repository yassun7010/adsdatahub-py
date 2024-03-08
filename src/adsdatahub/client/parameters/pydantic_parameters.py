import datetime
from typing import List, get_args, get_origin

from pydantic import BaseModel

from adsdatahub.restapi.schemas.field_type import ArrayTypeDict, FieldTypeDict, TypeDict
from adsdatahub.restapi.schemas.parameter_type import ParameterTypeDict


def convert_pydantic_param_types(params: BaseModel) -> dict[str, ParameterTypeDict]:
    return {
        name: ParameterTypeDict(
            {"type": convert_pydantic_parameter_type(field.annotation)}
        )
        for name, field in params.model_fields.items()
    }


def convert_pydantic_parameter_type(field_type: type | None) -> FieldTypeDict:
    if field_type is None:
        raise TypeError("Field annotation cannot be None")

    if issubclass(field_type, bool):
        return TypeDict({"type": "BOOL"})

    elif issubclass(field_type, str):
        return TypeDict({"type": "STRING"})

    elif issubclass(field_type, int):
        return TypeDict({"type": "INT64"})

    elif issubclass(field_type, float):
        return TypeDict({"type": "FLOAT64"})

    elif issubclass(field_type, datetime.datetime):
        return TypeDict({"type": "TIMESTAMP"})

    elif issubclass(field_type, datetime.date):
        return TypeDict({"type": "DATE"})

    else:
        origin_type = get_origin(field_type)
        if origin_type is list or origin_type is List:
            element_type = get_args(field_type)[0]
            return ArrayTypeDict(
                {"arrayType": convert_pydantic_parameter_type(element_type)}
            )
        raise TypeError(f"Unsupported type: {field_type}")
