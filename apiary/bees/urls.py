from rest_framework import routers

from .views import ApiaryViewSet, HiveViewSet, DeviceViewSet

router = routers.SimpleRouter()
router.register("apiaries", ApiaryViewSet, basename="apiary")
router.register("hives", HiveViewSet, basename="hive")
router.register("devices", DeviceViewSet, basename="device")

app_name = "bees"
urlpatterns = router.urls
