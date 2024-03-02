import adsdatahub.restapi


class TestRealClient:
    def test_client_constructer_type(self):
        assert isinstance(
            adsdatahub.restapi.RealClient(), adsdatahub.restapi.RealClient
        )
