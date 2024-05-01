from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ShoppingChecklist(models.Model):
    quantity = models.TextField()
    item_name = models.TextField(default='')

    def __str__(self):
        return self.item_name
