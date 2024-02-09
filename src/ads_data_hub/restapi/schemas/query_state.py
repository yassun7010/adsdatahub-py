from typing_extensions import Literal

QueryState = Literal[
    "QUERY_STATE_UNSPECIFIED",  # クエリの状態は指定されていません。
    "RUNNABLE",  # クエリはお客様が実行できます。
    "WHITELISTED",  # クエリは手動で安全であることが確認されています。
]
"""
分析クエリの実行モードを決定する状態。

See https://developers.google.com/ads-data-hub/reference/rest/v1/QueryState?hl=ja
"""
