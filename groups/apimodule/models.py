from django.db import models

# Create your models here.
class Hunde(models.Model):
    name = models.CharField(max_length=100)
    rasse = models.CharField(max_length=100)
    alter = models.IntegerField()
    geschlecht = models.CharField(max_length=100)
    bild = models.ImageField(upload_to='images/', blank=True, null=True)
    beschreibung = models.TextField()
    erstellt_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name