from typing import Annotated, NotRequired, TypedDict

from pydantic import Field

from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.analysis_query import AnalysisQueryRequest
from adsdatahub.restapi.schemas.filtered_row_summary import FilteredRowSummaryModel
from adsdatahub.restapi.schemas.query_execution_spec import QueryExecutionSpecRequest
from adsdatahub.restapi.schemas.query_performance_info import QueryPerformanceInfoModel


class AnalysisQueriesValidateQueryParams(TypedDict):
    """
    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/validate?hl=ja#request-body
    """

    query: AnalysisQueryRequest
    """
    検証するクエリ。
    """

    ads_data_customer_id: NotRequired[str]
    """
    （省略可）広告データの検証と一時テーブル アクセスに使用する、リンクされた Ads Ads Hub お客様 ID。

    デフォルトでは、リンクされているすべての顧客に表示されます。
    非推奨です。query_execution_spec 内で adsDataCustomerId を使用します。
    """

    matchDataCustomerId: NotRequired[str]
    """
    （省略可）マッチデータと検証テーブルへのアクセスの検証に使用する、リンクされた Ads Ads Hub お客様 ID。

    デフォルトでは、リンクされているすべての顧客に表示されます。
    非推奨です。query_execution_spec 内の match_table_customer_id を使用します。
    """

    spec: NotRequired[QueryExecutionSpecRequest]
    """
    （省略可）query_execution_spec 内の重複するフィールドが、外側のフィールドより優先されます。
    """

    include_performance_info: NotRequired[bool]
    """
    （省略可）true の場合、BigQuery を呼び出してクエリをドライランして、パフォーマンス情報を収集します。

    クエリを検証するだけの場合よりも時間がかかる可能性があります。
    ドライランには、startDate、endDate、query_execution_spec 内のパラメータを設定する必要があります。
    """


class AnalysisQueriesValidateResponseBody(Model):
    """
    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/validate?hl=ja#response-body
    """

    processed_bytes: Annotated[int | None, Field(alias="processedBytes")] = None
    """
    サポートが終了し、代わりに queryPerformanceInfo を使用してください。

    このクエリが読み取るデータのバイト数。
    この計算方法の詳細については、https://cloud.google.com/bigquery/pricing#data をご覧ください。
    includePerformanceInfo が true の場合に返されます。
    Google は processBytes バイトを MB 単位に丸め、次にバイト単位に変換します。
    -1 は、このクエリで取得できなかったことを意味します。
    """

    query_performance_info: Annotated[
        QueryPerformanceInfoModel | None, Field(alias="queryPerformanceInfo")
    ] = None
    """
    includePerformanceInfo が true の場合に返されます。
    """

    filtered_row_summary: Annotated[
        FilteredRowSummaryModel,
        Field(alias="filteredRowSummary"),
    ]