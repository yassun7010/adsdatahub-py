import os
from textwrap import dedent

import adsdatahub

credentials_file = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
customer_id = os.environ["CUSTOMER_ID"]
project = os.environ["PROJECT"]
dataset = os.environ["DATASET"]


client = adsdatahub.Client().customer(customer_id)

# クエリの問い合わせ
result = client.query(
    dedent(
        """
        SELECT
            @value as value,
            @start_date as start_date
        """
    ),
    {"value": 1},
    start_date="2024-01-01",
    end_date="2024-02-02",
    dest_table=f"{project}.{dataset}.sample",
)

for column in result.table_info.columns:
    print(column.model_dump_json(by_alias=True, exclude_unset=True))

print(result.job.to_dataframe())
