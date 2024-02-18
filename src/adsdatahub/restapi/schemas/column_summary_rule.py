from typing_extensions import TypedDict

from adsdatahub.restapi.schemas._model import ExtraForbidModel
from adsdatahub.restapi.schemas.parameter_value import ParameterValue
from adsdatahub.restapi.schemas.summary_type import SummaryType


class ColumnSummaryRuleDict(TypedDict):
    """
    単一の出力列の手順をマージします。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#ColumnSummaryRule
    """

    type: SummaryType
    value: ParameterValue


class ColumnSummaryRuleModel(ExtraForbidModel):
    type: SummaryType
    value: ParameterValue
