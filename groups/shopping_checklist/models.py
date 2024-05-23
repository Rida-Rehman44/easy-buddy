from django.conf import settings
from django.db import models
from trip.models import Trip


# Create your models here.

class ShoppingChecklist(models.Model):
    # Add any fields specific to the checklist itself
    # For example:
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, related_name='trip')

    def __str__(self):
        return self.name


class ShoppingItem(models.Model):
    checklist = models.ForeignKey(ShoppingChecklist, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    bought = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.item_name