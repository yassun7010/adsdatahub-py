from google.cloud import bigquery

from adsdatahub.restapi.schemas.operation import (
    OperationModel,
)
from adsdatahub.restapi.schemas.query_metadata import QueryMetadataModel


class QueryResult:
    def __init__(
        self,
        *,
        operation: OperationModel[QueryMetadataModel],
        job: bigquery.QueryJob,
    ) -> None:
        self.operation = operation
        self.job = job
