from typing_extensions import Literal

ShareType = Literal[
    "SHARE_TYPE_UNSPECIFIED",  # クエリの共有タイプが指定されていません。
    "MANAGED_CUSTOMERS",  # クエリは、Ads Data Hub ユーザー、またはお客様が管理している Ads Data Hub ユーザーのどちらからでも実行できます。
]
"""
サポートされているクエリ共有のタイプ。

Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/QueryShare?hl=ja
"""
