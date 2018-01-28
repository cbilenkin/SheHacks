from .models import Device
from .models import LocationSync
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import generics


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

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        #import ipdb; ipdb.set_trace();
        queryset = Device.objects.all()
        zipcode = self.request.query_params.get('zipcode', None)
        if zipcode is not None:
            queryset = queryset.filter(location__zipcode=zipcode)
        return queryset


class DeviceList(generics.ListAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        import ipdb; ipdb.set_trace();
        queryset = device.objects.all()
        zipcode = self.request.query_params.get('zipcode', None)
        if zipcode is not None:
            queryset = queryset.filter(location__zipcode=zipcode)
        return queryset
