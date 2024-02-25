import datetime

from pydantic import BeforeValidator, Field, PlainSerializer, ValidationInfo
from typing_extensions import Annotated, NotRequired, TypedDict

from adsdatahub.restapi.schemas._model import ExtraForbidModel
from adsdatahub.restapi.schemas._newtype import CustomerId, ResourceId
from adsdatahub.restapi.schemas.filtered_row_summary import (
    FilteredRowSummaryDict,
    FilteredRowSummaryModel,
)
from adsdatahub.restapi.schemas.merge_spec import MergeSpecDict, MergeSpecModel
from adsdatahub.restapi.schemas.parameter_type import (
    ParameterTypeDict,
    ParameterTypeModel,
)
from adsdatahub.restapi.schemas.query_share import QueryShareDict
from adsdatahub.restapi.schemas.query_state import QueryState


class AnalysisQueryNameModel(ExtraForbidModel):
    customer_id: CustomerId
    resource_id: ResourceId

    def __str__(self) -> str:
        return f"customers/{self.customer_id}/analysisQueries/{self.resource_id}"


def _deserialize_name(
    value: str | None, info: ValidationInfo
) -> dict[str, str | int] | None:
    if value is None:
        return None

    splited_value = value.split("/")

    if (
        len(splited_value) != 4
        or splited_value[0] != "customers"
        or splited_value[2] != "analysisQueries"
    ):
        raise ValueError(f"Invalid operation name: {value}")

    return {
        "customer_id": splited_value[1],
        "resource_id": splited_value[3],
    }


def _serialize_name(model: AnalysisQueryNameModel | None) -> str | None:
    if model is None:
        return None

    return f"customers/{model.customer_id}/analysisQueries/{model.resource_id}"


class AnalysisQueryRequestDict(TypedDict):
    """
    Ads Data Hub 内で実行できる分析クエリを定義します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#AnalysisQuery
    """

    name: NotRequired[str]
    """クエリを一意に識別する名前。"""

    title: str
    """クエリのタイトル。Ads Data Hub の単一顧客とクエリタイプ内で一意です。"""

    queryText: str
    """標準 SQL で記述されたクエリテキスト。"""

    parameterTypes: NotRequired[dict[str, ParameterTypeDict]]
    """クエリで想定されるその他のパラメータ。各引数名をその引数タイプにマッピングします。"""

    mergeSpec: NotRequired[MergeSpecDict]
    """
    行をマージする手順。
    存在する場合、プライバシー上の理由でドロップされるはずの行が 1 つに結合されます。
    マージされた行がプライバシー要件を満たしている場合は、マージされた行が最終出力に表示されます。
    """

    queryState: NotRequired[QueryState | str]
    """クエリの状態。"""

    queryShare: Annotated[
        NotRequired[list[QueryShareDict]], Field(default_factory=list)
    ]
    """所有する Ads Data Hub ユーザー以外のクエリも共有する方法を紹介します。"""

    filteredRowSummary: NotRequired[FilteredRowSummaryDict]
    """
    プライバシー上の理由によってドロップされた行を 1 つの結合行に統合する方法を定義します。
    マージされた行がプライバシー要件を満たしている場合は、マージされた行が最終出力に含められます。

    generateFilteredRowSummaryAutomatically と同時に使えません。"""

    generateFilteredRowSummaryAutomatically: NotRequired[bool]
    """
    true の場合、フィルタリングされた行の概要が自動的に生成されます。

    filteredRowSummary と同時に使えません。
    """


class AnalysisQueryRequestModel(ExtraForbidModel):
    """
    Ads Data Hub 内で実行できる分析クエリを定義します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#AnalysisQuery
    """

    name: Annotated[
        AnalysisQueryNameModel | None,
        BeforeValidator(_deserialize_name),
        PlainSerializer(_serialize_name),
    ] = None

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
        Field(alias="mergeSpec", default_factory=lambda: MergeSpecModel(columns={})),
    ]
    """
    行をマージする手順。

    deprecated: このフィールドは非推奨です。代わりに filter_row_summary を使用してください。

    存在する場合、プライバシー上の理由でドロップされるはずの行が 1 つに結合されます。
    マージされた行がプライバシー要件を満たしている場合は、マージされた行が最終出力に表示されます。
    """

    query_share: Annotated[list[QueryShareDict], Field(default_factory=list)]

    filtered_row_summary: Annotated[
        FilteredRowSummaryModel | None, Field(alias="filteredRowSummary")
    ] = None

    generate_filtered_row_summary_automatically: Annotated[
        bool | None, Field(alias="generateFilteredRowSummaryAutomatically")
    ] = None


class AnalysisQueryModel(ExtraForbidModel):
    """
    Ads Data Hub 内で実行できる分析クエリを定義します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries?hl=ja#AnalysisQuery
    """

    name: Annotated[
        AnalysisQueryNameModel,
        BeforeValidator(_deserialize_name),
        PlainSerializer(_serialize_name),
    ]

    title: str

    query_text: Annotated[str | None, Field(alias="queryText")] = None

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

    filtered_row_summary: Annotated[
        FilteredRowSummaryModel | None, Field(alias="filteredRowSummary")
    ] = None

    generate_filtered_row_summary_automatically: Annotated[
        bool | None, Field(alias="generateFilteredRowSummaryAutomatically")
    ] = None


AnalysisQueryRequest = AnalysisQueryRequestModel | AnalysisQueryRequestDict
