from rest_framework import viewsets, filters

from .models import Apiary, Hive, Device
from .serializers import ApiarySerializer, HiveSerializer, ListHiveSerializer, DeviceSerializer, ListDeviceSerializer


class ApiaryViewSet(viewsets.ModelViewSet):
    queryset = Apiary.objects.all()
    serializer_class = ApiarySerializer


class HiveViewSet(viewsets.ModelViewSet):
    queryset = Hive.objects.all()
    serializer_class = HiveSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["apiary__name", "apiary__address", "apiary__city"]

    def get_serializer_class(self):
        if self.action == "list":
            return ListHiveSerializer

        return HiveSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ListDeviceSerializer

        return DeviceSerializer
