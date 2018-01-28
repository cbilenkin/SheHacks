from django.db import models

# Create your models here.

class LocationSync(models.Model):
    latitude = models.CharField(max_length=30)
    longtitude = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    sync_time = models.DateTimeField()

    def __str__(self):
        return str(self.zipcode)

class Device(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField()
    location = models.ForeignKey(
        LocationSync,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return str(self.phone)
