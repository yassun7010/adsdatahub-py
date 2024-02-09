from typing_extensions import TypedDict

from ads_data_hub.restapi.schemas._model import ExtraForbidModel
from ads_data_hub.restapi.schemas.share_type import ShareType


class QueryShareDict(TypedDict):
    """
    所有する Ads Data Hub ユーザー以外のクエリも共有する方法を共有します。

    Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/QueryShare?hl=ja
    """

    shareType: ShareType


class QueryShareModel(ExtraForbidModel):
    shareType: ShareType
