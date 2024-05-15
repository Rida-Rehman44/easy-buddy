from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import requests
from urllib.parse import urlencode, urlparse, parse_qsl
from keys import map_api_key
import gpsd
import datetime as dt


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
    



    ###### Google Maps Api #################

# gps or ip to lat and long
class User_location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()

    @classmethod
    def fetch_gps_coordinates(cls):
        # Attempt to get GPS coordinates from the GPS device
        gpsd.connect()
        packet = gpsd.get_current()

        if packet.mode >= 2:
            # If GPS fix is available, use GPS coordinates
            latitude = packet.lat
            longitude = packet.lon
            altitude = packet.alt
            location = cls(latitude=latitude, longitude=longitude, altitude=altitude)
            location.save()
            return location
        else:
            # If no GPS fix is available, use IP-based geolocation
            try:
                ip_info = requests.get('https://ipinfo.io/json')
                ip_data = ip_info.json()
                # Extract latitude and longitude from IP geolocation data
                lat, lon = ip_data['loc'].split(',')
                location = cls(latitude=float(lat), longitude=float(lon), altitude=None)
                location.save()
                return location
            except Exception as e:
                print(f"Error fetching location from IP: {e}")
                return None
    @classmethod
    def fetch_and_create_location(cls):
        lat, lng = cls.fetch_gps_coordinates()
        if lat is not None and lng is not None:
            # Create a new Location object with fetched coordinates
            location = cls(latitude=lat, longitude=lng, altitude=None)
            location.save()
            return location
        else:
            return None
            



################################################################



class GoogleMapsClient(object):
 

    data_type = 'json'
    location_query = None
    api_key = map_api_key
    
    def __init__(self, User_location, api_key=None, address_or_postal_code=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lat = User_location.latitude
        self.lng = User_location.longitude 
        if api_key == None:
            raise Exception("API key is required")
        self.api_key = api_key
        self.location_query = address_or_postal_code
        if self.location_query != None:
            self.extract_lat_lng()
    
    def extract_lat_lng(self, location=None):
        loc_query = self.location_query
        if location != None:
            loc_query = location
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        params = {"address": loc_query, "key": self.api_key}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200, 299): 
            return {}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        lat,lng = latlng.get("lat"), latlng.get("lng")
        self.lat = lat
        self.lng = lng
        return lat, lng
    
    def search(self, keyword="Supermarket", radius=5000, location=None):
        lat, lng = self.lat, self.lng
        if location != None:
            lat, lng = self.extract_lat_lng(location=location)
        endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{self.data_type}"
        params = {
            "key": self.api_key,
            "location": f"{lat},{lng}",
            "radius": radius,
            "keyword": keyword
        }
        params_encoded = urlencode(params)
        places_url = f"{endpoint}?{params_encoded}"
        r = requests.get(places_url)
        # print(places_url, r.text)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()
    
    def detail(self, place_id="ChIJlXOKcDC3j4ARzal-5j-p-FY", fields=["name", "rating", "formatted_phone_number", "formatted_address"]):
        detail_base_endpoint = f"https://maps.googleapis.com/maps/api/place/details/{self.data_type}"
        detail_params = {
            "place_id": f"{place_id}",
            "fields" : ",".join(fields),
            "key": self.api_key
        }
        detail_params_encoded = urlencode(detail_params)
        detail_url = f"{detail_base_endpoint}?{detail_params_encoded}"
        r = requests.get(detail_url)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()
    

    

    