from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from events.models import Event


# Create your models here.

class ShoppingChecklist(models.Model):
    # Add any fields specific to the checklist itself
    # For example:
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_checklist_items')
    name = models.CharField(max_length=255, default="") 
    date_time_created = models.DateTimeField(default=timezone.now, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name='event')

    def __str__(self):
        return self.name


class ShoppingItem(models.Model):
    checklist = models.ForeignKey(ShoppingChecklist, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    bought = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.item_name

