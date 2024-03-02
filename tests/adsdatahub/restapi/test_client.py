import adsdatahub.restapi


class TestClient:
    def test_client_constructer_type(self):
        assert isinstance(adsdatahub.restapi.Client(), adsdatahub.restapi.RealClient)
