import datetime

from pydantic import Field
from typing_extensions import Annotated, NotRequired, TypedDict

from ads_data_hub.restapi.schemas._model import ExtraForbidModel
from ads_data_hub.restapi.schemas.filtered_row_summary import FilteredRowSummaryDict
from ads_data_hub.restapi.schemas.merge_spec import MergeSpecDict, MergeSpecModel
from ads_data_hub.restapi.schemas.parameter_type import (
    ParameterTypeDict,
    ParameterTypeModel,
)
from ads_data_hub.restapi.schemas.query_share import QueryShareDict
from ads_data_hub.restapi.schemas.query_state import QueryState


class AnalysisQueryDict(TypedDict):
    """
    Ads Data Hub 内で実行できる分析クエリを定義します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#AnalysisQuery
    """

    name: str
    """クエリを一意に識別する名前。"""

    title: str
    """クエリのタイトル。Ads Data Hub の単一顧客とクエリタイプ内で一意です。"""

    queryText: str
    """標準 SQL で記述されたクエリテキスト。"""

    parameterTypes: dict[str, ParameterTypeDict]
    """クエリで想定されるその他のパラメータ。各引数名をその引数タイプにマッピングします。"""

    mergeSpec: NotRequired[MergeSpecDict]
    """
    行をマージする手順。
    存在する場合、プライバシー上の理由でドロップされるはずの行が 1 つに結合されます。
    マージされた行がプライバシー要件を満たしている場合は、マージされた行が最終出力に表示されます。
    """

    queryState: QueryState
    """クエリの状態。"""

    # TODO: convertion
    updateTime: datetime.datetime
    """クエリが最後に更新された時刻。"""

    updateEmail: str
    """クエリを最後に更新したユーザーのメールアドレス。"""

    # TODO: convertion
    createTime: datetime.datetime
    """クエリが作成された時刻。"""

    createEmail: str
    """クエリを作成したユーザーのメールアドレス。"""

    queryShare: list[QueryShareDict]
    """所有する Ads Data Hub ユーザー以外のクエリも共有する方法を紹介します。"""

    filteredRowSummary: FilteredRowSummaryDict
    """
    プライバシー上の理由によってドロップされた行を 1 つの結合行に統合する方法を定義します。
    マージされた行がプライバシー要件を満たしている場合は、マージされた行が最終出力に含められます。

    generateFilteredRowSummaryAutomatically と同時に使えません。"""

    generateFilteredRowSummaryAutomatically: bool
    """
    true の場合、フィルタリングされた行の概要が自動的に生成されます。

    filteredRowSummary と同時に使えません。
    """


class AnalysisQueryModel(ExtraForbidModel):
    name: str

    title: str

    query_text: Annotated[str, Field(alias="queryText")]

    parameter_types: Annotated[
        dict[str, ParameterTypeModel],
        Field(
            alias="parameterTypes",
        ),
    ]

    merge_spec: MergeSpecModel | None = None

    query_state: QueryState

    update_time: datetime.datetime

    update_email: str

    create_time: datetime.datetime

    create_email: str

    query_share: list[QueryShareDict]

    filtered_row_summary: FilteredRowSummaryDict

    generate_filtered_row_summary_automatically: bool
