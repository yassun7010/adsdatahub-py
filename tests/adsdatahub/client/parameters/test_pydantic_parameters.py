import datetime

from pydantic import BaseModel


class Params(BaseModel):
    string: str
    integer: int
    float: float
    boolean: bool
    date: datetime.date
    timestamp: datetime.datetime
    list_string: list[str]


class TestConvertPydanticParamTypes:
    def test_convert_pydantic_param_types(self):
        from adsdatahub.client.parameters.pydantic_parameters import (
            convert_pydantic_param_types,
        )

        assert convert_pydantic_param_types(
            Params(
                string="string",
                integer=1,
                float=1.1,
                boolean=True,
                date=datetime.date.today(),
                timestamp=datetime.datetime.now(),
                list_string=["a", "b", "c"],
            )
        ) == {
            "string": {"type": {"type": "STRING"}},
            "integer": {"type": {"type": "INT64"}},
            "float": {"type": {"type": "FLOAT64"}},
            "boolean": {"type": {"type": "BOOL"}},
            "date": {"type": {"type": "DATE"}},
            "timestamp": {"type": {"type": "TIMESTAMP"}},
            "list_string": {
                "type": {
                    "arrayType": {
                        "type": "STRING",
                    }
                }
            },
        }
