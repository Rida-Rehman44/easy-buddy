import requests
from django.http import JsonResponse
from django.conf import settings

def get_weather_data(lat, lon):
    api_key = settings.WEATHER_API_KEY
    weather_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q=Bulk'

    try:
        response = requests.get(weather_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        weather_data = response.json()
        print(weather_data)
        current_weather = {
            'temperature': weather_data['current']['temp'],
            'condition': weather_data['current']['weather'][0]['description'],
            'humidity': weather_data['current']['humidity']
        }

        return current_weather

    except requests.exceptions.RequestException as e:
        print(f'Error fetching weather data: {e}')  # Log the error for debugging
        return None

def get_weather(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    if not lat or not lon:
        return JsonResponse({'error': 'Latitude and longitude are required.'}, status=400)

    weather_data = get_weather_data(lat, lon)
    if weather_data:
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'Error fetching weather data.'}, status=500)
