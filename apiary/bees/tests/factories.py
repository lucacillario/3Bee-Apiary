from decimal import Decimal

from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from bees.models import Apiary, Hive, Device


class ApiaryFactory(DjangoModelFactory):
    name = Faker("word")
    address = Faker("address")
    city = Faker("city")
    longitude = Decimal("12.111")
    latitude = Decimal("10.112")

    class Meta:
        model = Apiary
        django_get_or_create = ["name"]


class HiveFactory(DjangoModelFactory):
    name = Faker("word")
    apiary = SubFactory(ApiaryFactory)

    class Meta:
        model = Hive
        django_get_or_create = ["name"]


class DeviceFactory(DjangoModelFactory):
    serial = Faker("uuid4")

    class Meta:
        model = Device
        django_get_or_create = ["serial"]
