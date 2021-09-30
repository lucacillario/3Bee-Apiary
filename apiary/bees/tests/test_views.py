from decimal import Decimal

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from bees.tests.factories import ApiaryFactory
from bees.models import Apiary
from bees.serializers import ApiarySerializer

pytestmark = pytest.mark.django_db


def test_apiary_list(client: APIClient) -> None:
    assert Apiary.objects.count() == 0

    url = reverse("bees:apiary-list")

    # empty list
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert not response.json()

    # insert some dummy data
    num_of_dummies = 10
    for _ in range(num_of_dummies):
        ApiaryFactory()

    assert Apiary.objects.count() == 10
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    results = response.json()
    assert len(results) == 10
    serializer = ApiarySerializer(Apiary.objects.all(), many=True)
    assert serializer.data == results


def test_apiary_retrieve(client: APIClient) -> None:
    assert Apiary.objects.count() == 0

    # make sure that if the resource is not found a 404 is returned
    url = reverse("bees:apiary-detail", args=(1,))
    response = client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # insert a dummy apiary
    apiary = ApiaryFactory()
    assert Apiary.objects.filter(pk=apiary.pk).exists()
    url = reverse("bees:apiary-detail", args=(apiary.pk,))
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    serializer = ApiarySerializer(apiary)
    assert serializer.data == response.json()


def test_apiary_create(client: APIClient) -> None:
    assert Apiary.objects.count() == 0

    url = reverse("bees:apiary-list")

    # make sure that a validation error is raised if not all the mandatory fields are given
    response = client.post(url, data={}, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # create an apiary
    data = {
        "longitude": Decimal("12.111"),
        "latitude": Decimal("10.223"),
    }
    response = client.post(url, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


####################################
# SAME STORY FOR THE OTHER ENDPOINTS
#####################################
