from typing import TypedDict

from ads_data_hub.restapi.schemas._model import ExtraForbidModel
from ads_data_hub.restapi.schemas.merge_type import MergeType
from ads_data_hub.restapi.schemas.parameter_value import ParameterValue


class MergeColumnDict(TypedDict):
    """
    単一の出力列の手順をマージします。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#MergeColumn
    """

    type: MergeType
    """
    列の値を組み合わせるために使用するメソッドです。
    """

    value: ParameterValue
    """
    使用する定数値（CONSTANT マージタイプでのみ有効）。
    """


class MergeColumnModel(ExtraForbidModel):
    """
    単一の出力列の手順をマージします。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#MergeColumn
    """

    type: MergeType
    """
    列の値を組み合わせるために使用するメソッドです。
    """

    value: ParameterValue
    """
    使用する定数値（CONSTANT マージタイプでのみ有効）。
    """
