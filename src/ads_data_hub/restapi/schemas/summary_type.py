from typing_extensions import Literal

SummaryType = Literal[
    "SUMMARY_TYPE_UNSPECIFIED",  # サマリータイプが指定されていません。概要列の値は NULL になります。
    "CONSTANT",  # マージされた列の値を、指定された定数に置き換えます。
    "SUM",  # 結合された列の値の合計を取得します。
]
"""
概要の種類。

列の結合でサポートされているすべてのオペレーション。

Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja
"""
