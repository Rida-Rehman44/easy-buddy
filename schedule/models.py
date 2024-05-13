from django.db import models

class Artist(models.Model):
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
    
    day = models.DateField()
    stage = models.PositiveIntegerField()
    hours = models.IntegerField()
    genre = models.CharField(max_length=4, choices=GENRE_CHOICES)
    country = models.CharField(max_length=40)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES)
    
    class Meta:
        app_label = 'schedule'
    
    def __str__(self) -> str:
        return f"You selected {self.firstname} {self.lastname}, {self.genre} artist from {self.country}"
