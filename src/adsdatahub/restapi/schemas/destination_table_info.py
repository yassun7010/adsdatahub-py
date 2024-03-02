from typing import Annotated

from pydantic import Field

from adsdatahub.restapi.schemas._model import ExtraAllowModel
from adsdatahub.restapi.schemas.column_info import ColumnInfoModel
from adsdatahub.restapi.schemas.table_noise_impact import TableNoiseImpact


class DestinationTableInfoModel(ExtraAllowModel):
    """
    Metadata of an exported query output table.

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/DestinationTableInfo
    """

    table_path: Annotated[str, Field(alias="tablePath")]
    """
    Table path in the customer BigQuery project.
    """

    row_count: Annotated[int, Field(alias="rowCount")] = 0
    """
    Number of rows in the result.
    """

    columns: Annotated[list[ColumnInfoModel], Field(default_factory=list)]
    """
    Information about columns in result.
    """

    noise_impact: Annotated[TableNoiseImpact, Field(alias="noiseImpact")]
    """
    The noise impact message for this table.
    """

    impact_percentage: Annotated[float | None, Field(alias="impactPercentage")] = None
    """
    If applicable, the percent of cells in this table which are not greatly affected by noise.
    """

    def get_column(self, column_name: str) -> ColumnInfoModel | None:
        for column in self.columns:
            if column.name == column_name:
                return column

        return None
