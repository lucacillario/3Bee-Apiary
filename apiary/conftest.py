import pytest
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def client() -> APIClient:
    """API Client for DRF.

    See https://www.django-rest-framework.org/api-guide/testing/
    """
    return APIClient()
