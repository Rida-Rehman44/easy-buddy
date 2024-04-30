from django.db import models

# Create your models here.


class Artist(models.Model):
    'PKey'
    
    
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    genre = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    
    
    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname} {self.genre} from {self.country}" 
    
    
    