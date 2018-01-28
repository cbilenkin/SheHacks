from .models import Device
from .models import LocationSync
from rest_framework import viewsets
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
      class Meta:
        model = LocationSync
        fields = "__all__"

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = Device
        fields = "__all__"

class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
