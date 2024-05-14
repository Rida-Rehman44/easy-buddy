from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Group(models.Model):
    name = models.CharField(max_length=100) 
    location = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_groups"
    )
    members = models.ManyToManyField(User, related_name="joined_groups")
    is_open = models.BooleanField(default=True)

    class Meta:
        app_label = "groups"


class GroupMembership(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="memberships"
    )
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "groups"


class BulletinBoardMessage(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="group_bulletinboard_messages"
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="bulletinboard/images/", null=True, blank=True)
    video = models.FileField(upload_to="bulletinboard/videos/", null=True, blank=True)

    class Meta:
        app_label = "groups"

    def __str__(self):
        return self.content


class Artist(models.Model):
    CATEGORY_CHOICES = [
        ("ARTIST", "Artist"),
        ("BAND", "Band"),
    ]

    GENRE_CHOICES = [
        ("BCHT", "Bachata"),
        ("BND", "Banda"),
        ("HS", "House"),
        ("TRNC", "Electronic"),
        ("FNK", "Funk"),
        ("HHP", "HipHop"),
        ("RGG", "Reggea"),
        ("RGGT", "Reggeaton"),
        ("MTL", "Metal"),
        ("PNK", "Punk"),
        ("RP", "Rap"),
        ("RCK", "Rock"),
        ("TRC", "Trance"),
        ("TECH", "Techno"),
    ]

    day = models.DateTimeField()
    stage = models.PositiveIntegerField()
    hours = models.IntegerField()
    genre = models.CharField(max_length=40, choices=GENRE_CHOICES)
    country = models.CharField(max_length=40)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    class Meta:
        app_label = "groups"

    def __str__(self):
        return f"You select is {self.firstname} {self.lastname} {self.genre} from {self.country}"


class ShoppingChecklist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='group')
    
    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    checklist = models.ForeignKey(ShoppingChecklist, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name