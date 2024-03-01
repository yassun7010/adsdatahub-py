from collections import UserList
from typing import Annotated, Generic, TypeVar

from pydantic import Field

from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.column_info import ColumnInfoModel
from adsdatahub.restapi.schemas.table_noise_impact import TableNoiseImpact

T = TypeVar("T", bound=ColumnInfoModel)


class ColumnInfoList(UserList, Generic[T]):
    def __getitem__(self, key: int | str) -> ColumnInfoModel:
        if column := self.get(key):
            return column

        elif isinstance(key, int):
            raise IndexError(f"Column not found: {key}")

        else:
            raise KeyError(f"Column not found: {key}")

    def get(
        self, key: int | str, default: ColumnInfoModel | None = None
    ) -> ColumnInfoModel | None:
        if isinstance(key, int):
            if len(self) > key:
                return self[key]

            else:
                return default

        else:
            for column in self:
                if column.name == key:
                    return column

            else:
                return default


class DestinationTableInfoModel(Model):
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

    columns: Annotated[ColumnInfoList[ColumnInfoModel], Field(default_factory=list)]
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
