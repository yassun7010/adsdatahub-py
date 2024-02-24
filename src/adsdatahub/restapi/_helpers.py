from typing import Any, TypeVar, overload

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


@overload
def parse_response_body(response_body_type: None, response: httpx.Response) -> None:
    ...


@overload
def parse_response_body(
    response_body_type: type[GenericResponseBody], response: httpx.Response
) -> GenericResponseBody:
    ...


def parse_response_body(
    response_body_type: type[GenericResponseBody] | None, response: httpx.Response
) -> GenericResponseBody | None:
    if response.status_code != 200:
        raise ResponseStatusCodeError(response)

    if response_body_type is None:
        return None

    else:
        return response_body_type.model_validate_json(response.content)
