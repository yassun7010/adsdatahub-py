from typing_extensions import TypedDict

from adsdatahub.restapi.schemas._model import ExtraForbidModel
from adsdatahub.restapi.schemas.analysis_query import (
    AnalysisQueryDict,
    AnalysisQueryModel,
)
from adsdatahub.restapi.schemas.query_execution_spec import (
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
