import requests
from django.http import JsonResponse
from django.conf import settings


def hello_world(request):
    return JsonResponse({"message": "Hello, World!"})


def bye_world(request):
    return JsonResponse({"message": "Bye, World!"})


def fetch_posts(request):
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch posts"}, status=500)


def fetch_weather(request, city):
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to fetch weather data"}, status=500)


def search_books(request, title):
    base_url = "https://openlibrary.org/search.json"
    params = {"title": title}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch books"}, status=500)


def search_books_paginated(request, title, page=1):
    base_url = "https://openlibrary.org/search.json"
    params = {"title": title, "page": page}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch books"}, status=500)


def search_books_with_filters(request):
    title = request.GET.get("title", "")
    author = request.GET.get("author", "")
    publish_year = request.GET.get("publish_year", "")

    base_url = "https://openlibrary.org/search.json"
    params = {"title": title, "author": author, "publish_year": publish_year}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch books"}, status=500)


def get_book_details(request, olid):
    base_url = f"https://openlibrary.org/works/{olid}.json"

    response = requests.get(base_url)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch book details"}, status=500)


def random_dog_image(request):
    response = requests.get("https://dog.ceo/api/breeds/image/random")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch dog image"}, status=500)


def random_dog_breed_image(request, breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": f"Failed to fetch {breed} image"}, status=500)


def list_all_breeds(request):
    response = requests.get("https://dog.ceo/api/breeds/list/all")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch all breeds"}, status=500)


def dogs_by_breed(request):
    response = requests.get("https://dog.ceo/api/breed/hound/images")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch dogs by breed"}, status=500)


def browse_dog_breed_list(request, breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch all breeds"}, status=500)


def comments_by_post(request, post_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
    )

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse(
            {"error": f"Failed to fetch comments for post {post_id}"}, status=500
        )


def space_x_launches(request):
    response = requests.get("https://api.spacexdata.com/v4/launches/upcoming")

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch launch data"}, status=500)


def space_x_launches_details(request):
    launches_response = requests.get("https://api.spacexdata.com/v4/launches/upcoming")

    if launches_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch launch data"}, status=500)

    launches = launches_response.json()

    launch_data = []

    for launch in launches:
        rocket_id = launch.get("rocket")

        rocket_response = requests.get(
            f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
        )

        if rocket_response.status_code == 200:
            rocket_name = rocket_response.json().get("name", "Unknown Rocket")
        else:
            rocket_name = "Unknown Rocket"

        launch_data.append(
            {
                "launch_name": launch.get("name", "Unknown Launch"),
                "launch_date": launch.get("date_utc", "Unknown Date"),
                "rocket_name": rocket_name,
            }
        )

    return JsonResponse(launch_data, safe=False)


def past_launches(request):
    launches_response = requests.get("https://api.spacexdata.com/v4/launches/past")

    if launches_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch launch data"}, status=500)

    launches = launches_response.json()

    launch_data = []

    for launch in launches:
        rocket_id = launch.get("rocket")

        rocket_response = requests.get(
            f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
        )

        if rocket_response.status_code == 200:
            rocket_name = rocket_response.json().get("name", "Unknown Rocket")
        else:
            rocket_name = "Unknown Rocket"

        launchpad_id = launch.get("launchpad")
        launchpad_response = requests.get(
            f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
        )

        if launchpad_response.status_code == 200:
            launchpad_name = launchpad_response.json().get("name", "Unknown Launchpad")
        else:
            launchpad_name = "Unknown Launchpad"

        launch_data.append(
            {
                "launch_name": launch.get("name", "Unknown Launch"),
                "launch_date": launch.get("date_utc", "Unknown Date"),
                "launch_success": launch.get("success", None),
                "rocket_name": rocket_name,
                "launchpad_name": launchpad_name,
            }
        )

    return JsonResponse(launch_data, safe=False)


def rocket_details(request):
    rockets_response = requests.get("https://api.spacexdata.com/v4/rockets")

    if rockets_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch rocket data"}, status=500)

    rockets = rockets_response.json()

    rockets_data = []

    launches_response = requests.get("https://api.spacexdata.com/v4/launches")

    if launches_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch launch data"}, status=500)

    launches = launches_response.json()

    for rocket in rockets:
        rocket_id = rocket.get("id")

        times_used = sum(1 for launch in launches if launch.get("rocket") == rocket_id)

        rockets_data.append(
            {
                "rocket_name": rocket.get("name", "Unknown rocket"),
                "first_flight": rocket.get("first_flight", "Unknown first flight"),
                "success_rate": rocket.get("success_rate_pct", "Unknown success rate"),
                "times_used": times_used,
                "description": rocket.get("description", "Description unavailable"),
            }
        )

    return JsonResponse(rockets_data, safe=False)


def launches_by_rocket(request):
    rocket_name = request.GET.get("rocket_name", "")

    if not rocket_name:
        return JsonResponse({"error": "Rocket name is required"}, status=400)

    rockets_response = requests.get("https://api.spacexdata.com/v4/rockets")

    if rockets_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch rocket data"}, status=500)

    rockets = rockets_response.json()

    rocket_id = None
    for rocket in rockets:
        if rocket.get("name").lower() == rocket_name.lower():
            rocket_id = rocket.get("id")
            break

    if not rocket_id:
        return JsonResponse(
            {"error": f"Rocket named {rocket_name} not found"}, status=404
        )

    launches_response = requests.get("https://api.spacexdata.com/v4/launches")

    if launches_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch launches data"}, status=500)

    launches = launches_response.json()

    filtered_launches = [
        launch for launch in launches if launch.get("rocket") == rocket_id
    ]

    launch_data = []
    for launch in filtered_launches:
        launchpad_id = launch.get("launchpad")

        launchpad_response = requests.get(
            f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
        )
        if launchpad_response.status_code == 200:
            launchpad_name = launchpad_response.json().get("name", "Unknown Launchpad")
        else:
            launchpad_name = "Unknown Launchpad"

        launch_data.append(
            {
                "launch_name": launch.get("name", "Unknown Launch"),
                "launch_date": launch.get("date_utc", "Unknown Date"),
                "launch_success": launch.get("success", None),
                "launchpad_name": launchpad_name,
            }
        )

    return JsonResponse(launch_data, safe=False)
