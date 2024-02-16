from typing import Literal

from ads_data_hub.restapi.schemas.analysis_queries_start import (
    AnalysisQueriesStartDict,
    AnalysisQueriesStartModel,
)
from ads_data_hub.restapi.schemas.analysis_queries_start_transient import (
    AnalysisQueriesStartTransient,
)

ResourceName = Literal["customers.analysisQueries"]


class Resource:
    def create(self) -> None:
        """
        後で実行するための分析クエリを作成します。
        現時点では、クエリの検証は行われません。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/create?hl=ja
        """

        raise NotImplementedError()

    def delete(self, name: str) -> None:
        """
        分析クエリを削除します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/delete?hl=ja
        """
        raise NotImplementedError()

    def get(self, name: str) -> None:
        """
        リクエストされた分析クエリを取得します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/get?hl=ja
        """
        raise NotImplementedError()

    def list(self) -> None:
        """
        指定した顧客が所有する分析クエリを一覧表示します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/list?hl=ja
        """
        raise NotImplementedError()

    def patch(self, name: str) -> None:
        """
        既存の分析クエリを更新します。部分更新はサポートされています。次のクエリ フィールドは、この方法では更新できないため、無視されます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/patch?hl=ja
        """

    def start(
        self, params: AnalysisQueriesStartDict | AnalysisQueriesStartModel
    ) -> None:
        """
        保存された分析クエリの実行を開始します。
        結果は、指定した BigQuery 宛先テーブルに書き込まれます。
        返されたオペレーション名を使用して、クエリ完了ステータスをポーリングできます。

        Refarence: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/start?hl=ja
        """
        raise NotImplementedError()

    def start_transient(self, params: AnalysisQueriesStartTransient, /):
        """
        一時的な分析クエリで実行を開始します。
        結果は、指定した BigQuery 宛先テーブルに書き込まれます。
        返されたオペレーション名を使用して、クエリ完了ステータスをポーリングできます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/startTransient?hl=ja
        """
        raise NotImplementedError()

    def validate(self, parent: str):
        """
        提供された分析クエリに対して静的検証チェックを実行します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/customers.analysisQueries/validate?hl=ja
        """
