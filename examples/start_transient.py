import os
from textwrap import dedent

import adsdatahub

credentials_file = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
customer_id = os.environ["CUSTOMER_ID"]
project = os.environ["PROJECT"]
dataset = os.environ["DATASET"]

query_text = dedent(
    """
    SELECT
        campaign_id,
        date(timestamp_micros(query_id.time_usec), 'Asia/Tokyo') AS date,
        count(query_id.time_usec) AS imp
    FROM
        adh.google_ads_impressions
    GROUP BY
        campaign_id,
        date
    """
)


client = adsdatahub.Client(
    client_options={
        "credentials_file": credentials_file,
    },
).customer(customer_id)

# クエリの問い合わせ
result = client.query(
    query_text,
    start_date="2024-01-01",
    end_date="2024-02-02",
    dest_table=f"{project}.{dataset}.sample",
)

print(result.table_info.columns.get("campaign_id"))
