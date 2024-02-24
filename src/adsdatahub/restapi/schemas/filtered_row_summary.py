from typing import Annotated

from pydantic import Field
from typing_extensions import TypedDict

from adsdatahub.restapi.schemas._model import ExtraForbidModel
from adsdatahub.restapi.schemas.column_summary_rule import (
    ColumnSummaryRuleDict,
    ColumnSummaryRuleModel,
)


class FilteredRowSummaryDict(TypedDict):
    """
    分析クエリ結果のスキーマの手順を結合します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#FilteredRowSummary
    """

    columns: dict[str, ColumnSummaryRuleDict]


class FilteredRowSummaryModel(ExtraForbidModel):
    """
    分析クエリ結果のスキーマの手順を結合します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#FilteredRowSummary
    """

    columns: Annotated[dict[str, ColumnSummaryRuleModel], Field(default_factory=dict)]
