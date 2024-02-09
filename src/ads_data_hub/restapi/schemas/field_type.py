from typing_extensions import Literal, TypedDict


class Type(TypedDict):
    type: Literal["STRING", "INT64"]


class ArrayType(TypedDict):
    arrayType: "FieldType"


class StructType(TypedDict):
    structType: list["StructField"]


class StructField(TypedDict):
    fieldName: str
    fieldType: "FieldType"


FieldType = Type | ArrayType
"""
BigQuery のフィールド タイプを定義します。

Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/FieldType?hl=ja
"""
