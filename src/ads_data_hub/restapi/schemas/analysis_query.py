import datetime
from typing import Union

from pydantic import Field
from typing_extensions import Annotated, NotRequired, TypedDict

from ads_data_hub.restapi.schemas._model import ExtraForbidModel
from ads_data_hub.restapi.schemas.filtered_row_summary import (
    FilteredRowSummaryDict,
    FilteredRowSummaryModel,
)
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


class AnalysisQueryBaseModel(ExtraForbidModel):
    """
    Ads Data Hub 内で実行できる分析クエリを定義します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#AnalysisQuery
    """

    name: str

    title: str

    query_text: Annotated[str, Field(alias="queryText")]

    parameter_types: Annotated[
        dict[str, ParameterTypeModel],
        Field(
            alias="parameterTypes",
            default_factory=dict,
        ),
    ]

    merge_spec: Annotated[
        MergeSpecModel,
        Field(alias="mergeSpec", default_factory=MergeSpecDict),
    ]
    """
    行をマージする手順。

    deprecated: このフィールドは非推奨です。代わりに filter_row_summary を使用してください。

    存在する場合、プライバシー上の理由でドロップされるはずの行が 1 つに結合されます。
    マージされた行がプライバシー要件を満たしている場合は、マージされた行が最終出力に表示されます。
    """

    query_state: Annotated[QueryState, Field(alias="queryState")]

    update_time: Annotated[datetime.datetime, Field(alias="updateTime")]

    update_email: Annotated[str, Field(alias="updateEmail")]

    create_time: Annotated[datetime.datetime, Field(alias="createTime")]

    create_email: Annotated[str | None, Field(alias="createEmail")] = None

    query_share: Annotated[list[QueryShareDict], Field(default_factory=list)]


class AnalysisQueryGenerateFilteredRowSummaryAutomaticallyModel(AnalysisQueryBaseModel):
    generate_filtered_row_summary_automatically: Annotated[
        bool, Field(alias="generateFilteredRowSummaryAutomatically")
    ]


class AnalysisQueryFilteredRowSummaryModel(AnalysisQueryBaseModel):
    filtered_row_summary: Annotated[
        FilteredRowSummaryModel, Field(alias="filteredRowSummary")
    ]


AnalysisQueryModel = Union[
    AnalysisQueryBaseModel,
    AnalysisQueryGenerateFilteredRowSummaryAutomaticallyModel,
    AnalysisQueryFilteredRowSummaryModel,
]

AnalysisQuery = AnalysisQueryModel | AnalysisQueryDict
