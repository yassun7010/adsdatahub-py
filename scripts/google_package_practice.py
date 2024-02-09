#!/usr/bin/env python3

"""
Google の公式サンプルのコードをもとに、開発できるように練習中のコード。
"""
import json

import googleapiclient.discovery

from google.oauth2.service_account import Credentials


SCOPES = ["https://www.googleapis.com/auth/adsdatahub"]
DISCOVERY_URL = "https://adsdatahub.googleapis.com/$discovery/rest?version=v1"
creds = Credentials.from_service_account_file("service-account.json").with_scopes(
    SCOPES
)
developer_key = "YOUR_DEVELOPER_KEY"  # Replace with your developer key.
service = googleapiclient.discovery.build(
    "AdsDataHub",
    "v1",
    credentials=creds,
    developerKey=developer_key,
    discoveryServiceUrl=DISCOVERY_URL,
)

# Replace with your customer ID.
customer_name = input('Customer name (e.g. "customers/123"): ').strip()
queries = service.customers().analysisQueries().list(parent=customer_name).execute()  # type: ignore
print(json.dumps(queries, sort_keys=True, indent=4))
