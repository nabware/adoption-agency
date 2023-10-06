import requests
import os
from random import choice
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ["API_SECRET_KEY"]
CLIENT_ID = os.environ["API_CLIENT_ID"]
token = ""

#TODO: go back and return token instead of global variable
def update_token_and_return_animal():
    """Updates auth token and returns random animal"""

    update_auth_token_string()
    animal = get_random_animal()

    return parse_animal_display_info(animal)


def parse_animal_display_info(animal):
    """Takes animal dict and returns name, age, and photo"""

    parsed_animal = {"name": animal["name"], "age": animal["age"]}

    parsed_animal["photo_url"] = (
        animal["photos"][0]["medium"] if animal["photos"] else ""
    )

    print(parsed_animal)

    return parsed_animal


def update_auth_token_string():
    """This will authenticate with Petfinder api and return OAuth token"""

    response = requests.post(
        "https://api.petfinder.com/v2/oauth2/token",
        data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": SECRET_KEY,
        },
    )

    data = response.json()

    global token
    token = data["access_token"]
    print("Token successfully updated.")

#TODO: Petfinder base url or one global per url we have at the top
def get_random_animal():
    """Get 100 animals list and return a random one"""

    response = requests.get(
        "https://api.petfinder.com/v2/animals?limit=100",
        headers={"Authorization": f"Bearer {token}"},
    )

    data = response.json()
    animals = data["animals"]

    return choice(animals)
