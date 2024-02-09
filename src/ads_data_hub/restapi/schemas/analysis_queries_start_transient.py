from typing_extensions import TypedDict

from ads_data_hub.restapi.schemas._model import ExtraForbidModel
from ads_data_hub.restapi.schemas.analysis_query import (
    AnalysisQueryDict,
    AnalysisQueryModel,
)
from ads_data_hub.restapi.schemas.query_execution_spec import (
    QueryExecutionSpecDict,
    QueryExecutionSpecModel,
)


class AnalysisQueriesStartTransientDict(TypedDict):
    query: AnalysisQueryDict
    spec: QueryExecutionSpecDict
    destTable: str


class AnalysisQueriesStartTransient(ExtraForbidModel):
    query: AnalysisQueryModel
    spec: QueryExecutionSpecModel
    destTable: str
