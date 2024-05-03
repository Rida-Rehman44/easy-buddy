from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ShoppingChecklist(models.Model):
    # Add any fields specific to the checklist itself
    # For example:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Checklist {self.id}"


class ShoppingItem(models.Model):
    checklist = models.ForeignKey(ShoppingChecklist, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name

