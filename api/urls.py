# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_world, name="hello_world"),
    path("bye/", views.bye_world, name="bye_world"),
    path("posts/", views.fetch_posts, name="fetch_posts"),
    path("weather/<str:city>/", views.fetch_weather),
    path("books/<str:title>/", views.search_books),
    path(
        "books/search/",
        views.search_books_with_filters,
        name="search_books_with_filters",
    ),
    path("book/details/<str:olid>/", views.get_book_details, name="get_book_details"),
    path("random-dog/", views.random_dog_image, name="random_dog_image"),
    path(
        "random-dog/<str:breed>/",
        views.random_dog_breed_image,
        name="random_dog_breed_image",
    ),
    path("dog-breeds/", views.list_all_breeds, name="list_all_breeds"),
    path("dogs-by-breed/", views.dogs_by_breed, name="dogs_by_breed"),
    path(
        "dog-breed-list/<str:breed>/",
        views.browse_dog_breed_list,
        name="browse_dog_breed_list",
    ),
    path(
        "comments-by-post/<int:post_id>/",
        views.comments_by_post,
        name="comments_by_post",
    ),
    path("launches/", views.space_x_launches, name="space_x_launches"),
    path(
        "launch-details/",
        views.space_x_launches_details,
        name="space_x_launches_details",
    ),
    path("past-launches/", views.past_launches, name="past_launches"),
    path("rocket-details/", views.rocket_details, name="rocket_details"),
    path("launches_by_rocket/", views.launches_by_rocket, name="launches_by_rocket"),
]
