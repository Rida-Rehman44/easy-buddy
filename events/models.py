from django.db import models
from django.contrib.auth.models import Group, User


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='groups', blank=True, null=True)
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return self.name