from typing import Any, TypeVar

import httpx

from adsdatahub.exceptions import ResponseStatusCodeError
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


def parse_response_body(
    response_body_type: type[GenericResponseBody], response: httpx.Response
) -> GenericResponseBody:
    if response.status_code != 200:
        raise ResponseStatusCodeError(response)
    return response_body_type.model_validate_json(response.content)
