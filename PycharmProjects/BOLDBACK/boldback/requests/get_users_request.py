import requests
from boldback.config.settings import Config


def get_users(page):
    url = f"{Config.BASE_URL}{Config.GET_USERS_URL}?page={page}"
    response = requests.get(url, timeout=Config.TIMEOUT)

    if response.status_code != 200:
        raise Exception(f"Error: Expected status 200, but got {response.status_code}")

    try:
        response_json = response.json()
    except ValueError:
        raise Exception("Error: Response is not a valid JSON")

    if 'data' not in response_json:
        raise Exception("Error: Response does not contain 'data' field")

    return response
