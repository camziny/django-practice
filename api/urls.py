# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'), 
    path('bye/', views.bye_world, name='bye_world'), 
    path('posts/', views.fetch_posts, name='fetch_posts'),
    path('weather/<str:city>/', views.fetch_weather),
    path('books/<str:title>/', views.search_books),
    path('books/search/', views.search_books_with_filters, name='search_books_with_filters'),
    path('book/details/<str:olid>/', views.get_book_details, name='get_book_details'),
    path('random-dog/', views.random_dog_image, name='random_dog_image'),
    path('random-dog/<str:breed>/', views.random_dog_breed_image, name='random_dog_breed_image'),
    path('dog-breeds/', views.list_all_breeds, name='list_all_breeds'),
    path('dogs-by-breed/', views.dogs_by_breed, name='dogs_by_breed')
]
