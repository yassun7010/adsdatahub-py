import os
from textwrap import dedent
from time import sleep

import adsdatahub.restapi

credentials_file = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
customer_id = os.environ["ADS_DATA_HUB_CUSTOMER_ID"]
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


client = adsdatahub.restapi.Client(
    client_options={
        "credentials_file": credentials_file,
    }
)

# クエリの問い合わせ
operation = client.resource(
    "https://adsdatahub.googleapis.com/v1/customers/{customer_id}/analysisQueries",
    customer_id=customer_id,
).start_transient(
    {
        "query": {
            "queryText": query_text,
        },
        "spec": {
            "startDate": "2021-01-01",
            "endDate": "2021-12-31",
        },
        "destTable": f"{project}.{dataset}.sample",
    }
)

# クエリの完了を待つ。
while not (
    operation := client.resource(
        "https://adsdatahub.googleapis.com/v1/operations/{unique_id}",
        unique_id=operation.name.unique_id,
    ).wait()
).done:
    sleep(1)

# 成功した場合
if operation.response:
    for table in operation.response.destination_tables:
        for column in table.columns:
            print(
                {
                    "name": column.name,
                    "noise_impact": column.noise_impact,
                    "impact_percentage": column.impact_percentage,
                }
            )

# 失敗した場合
elif operation.error:
    print(operation.error.message)