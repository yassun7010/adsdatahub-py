from google.cloud import bigquery

from adsdatahub.restapi.schemas.analysis_query_metadata import (
    AnalysisQueryMetadataModel,
)
from adsdatahub.restapi.schemas.operation import (
    OperationModel,
)


class QueryResult:
    def __init__(
        self,
        *,
        operation: OperationModel[AnalysisQueryMetadataModel],
        job: bigquery.QueryJob,
    ) -> None:
        self.operation = operation
        self.job = job
