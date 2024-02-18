from adsdatahub.restapi._helpers import snake2camel


def test_snake2camel():
    assert snake2camel(
        **{
            "name": "taro tanaka",
            "first_name": "taro",
            "last_name": "tanaka",
            "age": 20,
            "is_student": None,
        }
    ) == {
        "name": "taro tanaka",
        "firstName": "taro",
        "lastName": "tanaka",
        "age": 20,
    }
