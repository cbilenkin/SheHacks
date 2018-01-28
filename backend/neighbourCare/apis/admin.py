from django.contrib import admin

from .models import LocationSync
from .models import Device


class LocationAdmin(admin.ModelAdmin):
    pass

class DeviceAdmin(admin.ModelAdmin):
    pass

admin.site.register(LocationSync, LocationAdmin)
admin.site.register(Device, DeviceAdmin)
