from typing_extensions import Literal, TypedDict


class TypeDict(TypedDict):
    type: Literal["STRING", "INT64"]


class ArrayTypeDict(TypedDict):
    arrayType: "FieldTypeDict"


class StructTypeDict(TypedDict):
    structType: list["StructFieldDict"]


class StructFieldDict(TypedDict):
    fieldName: str
    fieldType: "FieldTypeDict"


FieldTypeDict = TypeDict | ArrayTypeDict
"""
BigQuery のフィールド タイプを定義します。

Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/FieldType?hl=ja
"""


class TypeModel(TypedDict):
    type: Literal[
        "BIGNUMERIC",
        "BOOL",
        "BYTES",
        "DATE",
        "DATETIME",
        "FLOAT64",
        "GEOGRAPHY",
        "INT64",
        "INTERVAL",
        "JSON",
        "NUMERIC",
        "STRING",
        "TIME",
        "TIMESTAMP",
    ]


class ArrayTypeModel(TypedDict):
    arrayType: "FieldTypeModel"


class StructTypeModel(TypedDict):
    structType: list["StructFieldModel"]


class StructFieldModel(TypedDict):
    fieldName: str
    fieldType: "FieldTypeModel"


FieldTypeModel = TypeModel | ArrayTypeModel

FieldType = FieldTypeDict | FieldTypeModel
