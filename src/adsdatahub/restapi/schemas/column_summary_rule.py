from typing_extensions import TypedDict

from adsdatahub.restapi.schemas._model import ExtraForbidModel
from adsdatahub.restapi.schemas.parameter_value import (
    ParameterValueDict,
    ParameterValueModel,
)
from adsdatahub.restapi.schemas.summary_type import SummaryType


class ColumnSummaryRuleDict(TypedDict):
    """
    単一の出力列の手順をマージします。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#ColumnSummaryRule
    """

    type: SummaryType
    value: ParameterValueDict


class ColumnSummaryRuleModel(ExtraForbidModel):
    type: SummaryType
    value: ParameterValueModel
