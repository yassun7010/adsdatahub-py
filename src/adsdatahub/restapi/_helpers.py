import json
from typing import Any, TypeVar

import httpx

from adsdatahub.exceptions import (
    AdsDataHubResponseStatusCodeError,
    AdsDataHubUnavailableError,
    AdsDataHubUnimplementedError,
)
from adsdatahub.restapi.schemas._model import Model

GenericResponseBody = TypeVar("GenericResponseBody", bound=Model)


def snake2camel(**origin: Any) -> dict[str, Any]:
    data = {}
    for k, v in origin.items():
        if v is None:
            continue

        if "_" in k:
            camel_key = "".join(map(lambda s: s.capitalize(), k.split("_")))
            camel_key = camel_key[0].lower() + camel_key[1:]

            data[camel_key] = v
        else:
            data[k] = v

    return data


def validate_response_status_code(response: httpx.Response) -> None:
    if response.status_code != 200:
        match response.status_code:
            case 501:
                try:
                    if (
                        response.json().get("error", {}).get("status")
                        == "UNIMPLEMENTED"
                    ):
                        raise AdsDataHubUnimplementedError(response)
                except json.JSONDecodeError:
                    pass

            case 503:
                raise AdsDataHubUnavailableError(response)

        raise AdsDataHubResponseStatusCodeError(response)


def parse_response_body(
    response_body_type: type[GenericResponseBody],
    response: httpx.Response,
) -> GenericResponseBody:
    validate_response_status_code(response)

    return response_body_type.model_validate_json(response.content)
