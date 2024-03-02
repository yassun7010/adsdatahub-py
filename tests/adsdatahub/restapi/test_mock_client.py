import adsdatahub.restapi


class TestMockClient:
    def test_client_constructer_type(self):
        assert isinstance(
            adsdatahub.restapi.MockClient(), adsdatahub.restapi.MockClient
        )
