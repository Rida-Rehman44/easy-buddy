from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Hunde
from .serializers import HundeSerializer


class HundeTests(APITestCase):

    def setUp(self):
        # Create some sample data
        self.hunde1 = Hunde.objects.create(
            name="Bello",
            rasse="Golden Retriever",
            alter=5,
            geschlecht="Männlich",
            beschreibung="Ein freundlicher Hund"
        )
        self.hunde2 = Hunde.objects.create(
            name="Luna",
            rasse="Labrador",
            alter=3,
            geschlecht="Weiblich",
            beschreibung="Ein energischer Hund"
        )
    
    def test_create_dogs(self):
        url = reverse('create-dogs')
        data = [
            {
                "name": "Max",
                "rasse": "Beagle",
                "alter": 2,
                "geschlecht": "Männlich",
                "beschreibung": "Ein neugieriger Hund"
            },
            {
                "name": "Bella",
                "rasse": "Poodle",
                "alter": 4,
                "geschlecht": "Weiblich",
                "beschreibung": "Ein kluger Hund"
            }
        ]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hunde.objects.count(), 4)

    def test_dog_list(self):
        url = reverse('dog-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_update_dogs(self):
        url = reverse('update-dogs', kwargs={'pk': self.hunde1.pk})
        data = {
            "name": "Bello",
            "rasse": "Golden Retriever",
            "alter": 6,  # Updated age
            "geschlecht": "Männlich",
            "beschreibung": "Ein sehr freundlicher Hund"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.hunde1.refresh_from_db()
        self.assertEqual(self.hunde1.alter, 6)
        self.assertEqual(self.hunde1.beschreibung, "Ein sehr freundlicher Hund")
    
    def test_delete_dogs(self):
        url = reverse('delete-dogs', kwargs={'pk': self.hunde1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hunde.objects.count(), 1)

    def test_list_create(self):
        url = reverse('underdog')
        data = {
            "name": "Charlie",
            "rasse": "Cocker Spaniel",
            "alter": 4,
            "geschlecht": "Männlich",
            "beschreibung": "Ein verspielter Hund"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hunde.objects.count(), 3)
    
    def test_get_update_delete_dogs(self):
        url = reverse('topdog', kwargs={'pk': self.hunde2.pk})
        # Test GET
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Luna')

        # Test PUT
        data = {
            "name": "Luna",
            "rasse": "Labrador",
            "alter": 3,
            "geschlecht": "Weiblich",
            "beschreibung": "Ein sehr energischer Hund"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.hunde2.refresh_from_db()
        self.assertEqual(self.hunde2.beschreibung, "Ein sehr energischer Hund")

        # Test DELETE
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Hunde.objects.count(), 1)
