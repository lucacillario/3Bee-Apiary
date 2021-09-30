from django.contrib import admin

from .models import Apiary, Hive, Device


class ApiaryAdmin(admin.ModelAdmin):
    pass


class HiveAdmin(admin.ModelAdmin):
    pass


class DeviceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Apiary, ApiaryAdmin)
admin.site.register(Hive, HiveAdmin)
admin.site.register(Device, DeviceAdmin)
