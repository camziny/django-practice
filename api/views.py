
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
        
def search_books(request,title):
        base_url = 'https://openlibrary.org/search.json'
        params = {'title': title}

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch books'}, status=500)
        
def search_books_paginated(request, title, page=1):
        base_url = 'https://openlibrary.org/search.json'
        params = {
          'title': title,
          'page': page
     }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch books'}, status=500)
        
def search_books_with_filters(request):
        title = request.GET.get('title', '')
        author = request.GET.get('author', '')
        publish_year = request.GET.get('publish_year', '')

        base_url = 'https://openlibrary.org/search.json'
        params = {
             'title': title,
             'author': author,
             'publish_year': publish_year
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else: 
            return JsonResponse({'error': 'Failed to fetch books'}, status=500)
        
def get_book_details(request, olid):
    base_url = f'https://openlibrary.org/works/{olid}.json'

    response = requests.get(base_url)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch book details'}, status=500)
    
def random_dog_image(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch dog image'}, status=500) 

def random_dog_breed_image(request, breed):
     response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')

     if response.status_code == 200:
          return JsonResponse(response.json(), safe=False)
     else:
          return JsonResponse({'error': f'Failed to fetch {breed} image'}, status=500)
     
def list_all_breeds(request):
     response = requests.get('https://dog.ceo/api/breeds/list/all')

     if response.status_code == 200:
          return JsonResponse(response.json(), safe=False)
     else:
          return JsonResponse({'error': 'Failed to fetch all breeds'}, status=500)
     
def dogs_by_breed(request):
     response = requests.get('https://dog.ceo/api/breed/hound/images')

     if response.status_code ==200:
          return JsonResponse(response.json(), safe=False)
     else:
          return JsonResponse({'error': 'Failed to fetch dogs by breed'}, status=500)
     
def browse_dog_breed_list(request, breed):
     response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')

     if response.status_code == 200:
          return JsonResponse(response.json(), safe=False)
     else:
          return JsonResponse({'error': 'Failed to fetch all breeds'}, status=500)
     
def comments_by_post(request, post_id):
     response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')

     if response.status_code == 200:
          return JsonResponse(response.json(), safe=False)
     else:
          return JsonResponse({'error': f'Failed to fetch comments for post {post_id}'}, status=500)