from django.db import models
from django.conf import settings


# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    is_open = models.BooleanField(default=True)

    latitude = models.FloatField(null=True, blank=True)  # Add latitude field
    longitude = models.FloatField(null=True, blank=True)  # Add longitude field


    def __str__(self):
        return self.name


class Event(models.Model):
    trip = models.ForeignKey(Trip, related_name='events', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name

