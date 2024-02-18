import datetime

from typing_extensions import NotRequired, TypedDict

from adsdatahub.restapi.schemas._model import ExtraForbidModel
from adsdatahub.restapi.schemas.date import DateDict, DateModel
from adsdatahub.restapi.schemas.parameter_value import (
    ParameterValueDict,
    ParameterValueModel,
)


class QueryExecutionSpecRequestDict(TypedDict):
    """クエリ実行パラメータを定義します。

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
    startDate: DateDict | datetime.date | str
    """クエリの開始日（この日付を含む）。"""

    # TODO: converter
    endDate: DateDict | datetime.date | str
    """クエリの終了日（その日を含む）。"""

    timeZone: NotRequired[str | None]
    """クエリの開始日と終了日のタイムゾーン。指定しない場合、デフォルトは 'UTC' です。"""

    parameterValues: NotRequired[dict[str, ParameterValueDict]]
    """クエリで想定されるその他のパラメータ。各パラメータ名をそのバインドされた値にマッピングします。"""

    jobId: NotRequired[str]
    """
    クエリ オペレーションのジョブ ID。
    結果として得られるオペレーションは、"operations/[jobId]" という名前になります（例: "operations/job_123"）。
    同じジョブ ID のオペレーションがすでに存在する場合は、エラーが発生します。
    指定されていない場合、サーバーによってジョブ ID が生成されます。
    """


class QueryExecutionSpecRequestModel(ExtraForbidModel):
    adsDataCustomerId: str | None = None
    matchDataCustomerId: str | None = None
    startDate: DateModel | datetime.date | str
    endDate: DateModel | datetime.date | str
    timeZone: str | None = None
    parameterValues: dict[str, ParameterValueModel]
    jobId: str | None = None


class QueryExecutionSpecResponseModel(ExtraForbidModel):
    adsDataCustomerId: str
    matchDataCustomerId: str
    startDate: DateModel
    endDate: DateModel
    timeZone: str
    parameterValues: dict[str, ParameterValueModel]
    jobId: str


QueryExecutionSpecRequest = (
    QueryExecutionSpecRequestDict | QueryExecutionSpecRequestModel
)
