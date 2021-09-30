from rest_framework import serializers

from .models import Apiary, Hive, Device


class ApiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Apiary
        fields = "__all__"


class HiveSerializer(serializers.ModelSerializer):
    apiary = ApiarySerializer(read_only=True)
    device = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Hive
        fields = "__all__"


class ListHiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields = ["name"]
        read_only_fields = ["name"]


class DeviceHiveSerializer(serializers.ModelSerializer):
    apiary = ApiarySerializer(read_only=True)

    class Meta:
        model = Hive
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    hive = DeviceHiveSerializer(read_only=True)

    class Meta:
        model = Device
        fields = "__all__"


class ListDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ["serial", "is_on", "status"]
        read_only_fields = ["serial", "is_on", "status"]
