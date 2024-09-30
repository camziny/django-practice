
import requests
from django.http import JsonResponse
from django.conf import settings

def hello_world(request):
    return JsonResponse({'message': 'Hello, World!'})

def bye_world(request):
    return JsonResponse({'message': "Bye, World!"})

def fetch_posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': "Failed to fetch posts"}, status=500)
    
def fetch_weather(request, city):
        api_key = settings.OPENWEATHERMAP_API_KEY
        base_url = 'http://api.openweathermap.org/data/2.5/weather'

        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({'error': 'Failed to fetch weather data'}, status=500)
        