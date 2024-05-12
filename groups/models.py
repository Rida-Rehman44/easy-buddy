from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_groups')
    location = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GroupMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('owner', 'Owner'), ('member', 'Member')])

    def __str__(self):
        return f"{self.user} - {self.group} ({self.role})"


class BulletinBoardMessage(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_bulletinboard_messages')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='bulletinboard/images/', null=True, blank=True)
    video = models.FileField(upload_to='bulletinboard/videos/', null=True, blank=True)
    
    def __str__(self):
        return self.content
