from django.db import models
from django.contrib.auth.models import User
from events.models import Event
from groups.models import Group  # Import the Group model

class ShoppingChecklist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name='event')

    # Add ForeignKey field to reference Group model
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    checklist = models.ForeignKey(ShoppingChecklist, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
