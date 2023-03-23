import pytest
from service import Service

class TestService:
    def test_check_init_service(self):
        service = Service
        assert service is not None

    def test_check_get_service(self):
        service = Service
        assert str(service.get_service) is not None