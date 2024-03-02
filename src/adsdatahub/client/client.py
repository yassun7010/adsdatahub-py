from typing import TYPE_CHECKING, Unpack

from google.cloud import bigquery

import adsdatahub.restapi
from adsdatahub._types import CustomerId
from adsdatahub.restapi.real_client import RealClientConstructerKwargs

if TYPE_CHECKING:
    from adsdatahub.client.customer import CustomerClient


class Client:
    def __init__(
        self,
        restapi_client: adsdatahub.restapi.Client | None = None,
        bigquery_client: bigquery.Client | None = None,
        **kwargs: Unpack[RealClientConstructerKwargs],
    ) -> None:
        if not restapi_client:
            restapi_client = adsdatahub.restapi.Client(**kwargs)

        if not bigquery_client:
            bigquery_client = bigquery.Client(**kwargs)

        self.restapi = restapi_client
        self.bigquery_client = bigquery_client

    def customer(self, customer_id: CustomerId) -> "CustomerClient":
        from adsdatahub.client.customer import CustomerClient

        return CustomerClient(self, customer_id)
