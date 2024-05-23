from django.db import models

# Create your models here.


class Artist(models.Model):
    'PKey'
    
    
    CATEGORY_CHOICES = [
    ('ARTIST', 'Artist'),
    ('BAND', 'Band'),
    
    ] 
    
    GENRE_CHOICES = [
    ('BCHT', 'Bachata'),
    ('BND', 'Banda'),
    ('HS', 'House'),
    ('TRNC', 'Electronic'),
    ('FNK', 'Funk'),
    ('HHP', 'HipHop'),
    ('RGG', 'Reggea'),
    ('RGGT', 'Reggeaton'),
    ('MTL', 'Metal'),
    ('PNK', 'Punk'),
    ('RP', 'Rap'),
    ('RCK', 'Rock'),
    ('TRC', 'Trance'),
    ('TECH', 'Techno'),
    
    ] 
    
    day = models.DateTimeField()
    stage = models.PositiveIntegerField()
    hours = models.IntegerField()
    genre = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    
    
    def __str__(self) -> str:
        return f"You select is {self.firstname} {self.lastname} {self.genre} from {self.country}" 
    
    
    