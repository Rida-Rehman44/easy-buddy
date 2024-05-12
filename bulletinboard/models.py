# models.py
from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    # Add your Group model fields here
    name = models.CharField(max_length=100)
    # Add other fields as needed

class BulletinBoardMessage(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='bulletinboard/images/', null=True, blank=True)
    video = models.FileField(upload_to='bulletinboard/videos/', null=True, blank=True)

    def __str__(self):
        return self.content
