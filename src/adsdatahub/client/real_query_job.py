import pandas as pd
from google.cloud import bigquery

from adsdatahub.client.query_job import QueryJob


class RealQueryJob(QueryJob):
    def __init__(self, job: bigquery.QueryJob) -> None:
        self._job = job

    def to_dataframe(self) -> pd.DataFrame:
        return self._job.to_dataframe()
