import datetime

from ads_data_hub.restapi.schemas.parameter_value import ParameterValue
from typing_extensions import NotRequired, TypedDict


class QueryExecutionSpec(TypedDict):
    """
    クエリ実行パラメータを定義します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/QueryExecutionSpec?hl=ja
    """

    adsDataCustomerId: NotRequired[str]
    """
    クエリで使用されている広告データを所有している、
    リンクされた Ads Data Hub お客様 ID。
    指定されていない場合、クエリは、Ads Data Hub ユーザーが所有する広告データを使用して実行されます。
    """

    matchDataCustomerId: NotRequired[str]
    """
    クエリの一致データを所有している、リンクされた Ads Data Hub お客様 ID。
    指定されていない場合、クエリは、該当する場合は Ads Data Hub お客様 ID が所有するマッチデータを使用して実行されます。
    """

    # TODO: converter
    startDate: datetime.date
    """クエリの開始日（この日付を含む）。"""

    # TODO: converter
    endDate: datetime.date
    """クエリの終了日（その日を含む）。"""

    timeZone: str
    """クエリの開始日と終了日のタイムゾーン。指定しない場合、デフォルトは 'UTC' です。"""

    parameterValues: dict[str, ParameterValue]
    """クエリで想定されるその他のパラメータ。各パラメータ名をそのバインドされた値にマッピングします。"""

    jobId: str
    """
    クエリ オペレーションのジョブ ID。
    結果として得られるオペレーションは、"operations/[jobId]" という名前になります（例: "operations/job_123"）。
    同じジョブ ID のオペレーションがすでに存在する場合は、エラーが発生します。
    指定されていない場合、サーバーによってジョブ ID が生成されます。
    """
