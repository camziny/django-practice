# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'), 
    path('bye/', views.bye_world, name='bye_world'), 
    path('posts/', views.fetch_posts, name='fetch_posts'),
    path('weather/<str:city>/', views.fetch_weather),
]
