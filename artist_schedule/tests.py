from django.test import TestCase
from artist_schedule.models import Artist


# Create your tests here.



class TestArtist(TestCase):
    
    
    
    def test_artists_firstname():
        
        artist = Artist.objects.create(
        genre = 'pop',
        country = 'UK',
        firstname = 'Dua',
        lastname = 'Lipa',
    )
    
        assert artist.firstname == 'Dua'
        
        
    def test_artists_lastname():
        
        artist = Artist.objects.create(
        genre = 'pop',
        country = 'UK',
        firstname = 'Dua',
        lastname = 'Lipa',
    )
        
        assert artist.lastname == 'Lipa'
        
        
        
    def test_firstname_correct(self):
       
        artist = Artist.objects.create(
            genre='pop',
            country='USA',
            firstname='Selena',
            lastname='Gomez',
        )
        
        artist.save() 
        self.assertEqual(artist.firstname, 'Selena')
        
        

    def test_lastname_correct(self):
        
        artist = Artist.objects.create(
            genre='pop',
            country='USA',
            firstname='Selena',
            lastname='Gomez',
        )
        
        artist.save()  
        self.assertEqual(artist.lastname, 'Gomez')
        
        
        
    def test_country_correct(self):
        
        artist = Artist.objects.create(
        genre='pop',
        country='USA',
        firstname='Selena',
        lastname='Gomez',
    )
        artist.save() 
        self.assertEqual(artist.country, 'USA')
        
    
    
    def test_genre_correct(self):
   
        artist = Artist.objects.create(
        genre='pop',
        country='USA',
        firstname='Selena',
        lastname='Gomez',
    )
        artist.save()  
        self.assertEqual(artist.genre, 'pop')
        
        
        
    def test_artist_not_in_database(self):
        
        new_artist = Artist.objects.create(
        genre='rock',
        country='USA',
        firstname='Bruno',
        lastname='Mars',
    )
        new_artist.save()  
        
        self.assertEqual(Artist.objects.filter(firstname='Bruno').count(), 1)
        self.assertEqual(Artist.objects.filter(lastname='Mars').count(), 1)
        self.assertEqual(Artist.objects.filter(country='USA').count(), 1)
        self.assertEqual(Artist.objects.filter(genre='rock').count(), 1)
      
      
        
    def test_delete_artist(self):
   
        existing_artist = Artist.objects.create(
        genre='rock',
        country='UK',
        firstname='Ed',
        lastname='Sheeran',
    )

        existing_artist.delete()
        self.assertFalse(Artist.objects.filter(firstname='Ed').exists())
        self.assertFalse(Artist.objects.filter(lastname='Sheeran').exists())
        self.assertFalse(Artist.objects.filter(country='UK').exists())
        self.assertFalse(Artist.objects.filter(genre='rock').exists())
        
        
    # def test_artists_fail():
        
     
     
     
    
    
    
    