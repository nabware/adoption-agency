import requests
import os


SECRET_KEY = os.environ['API_SECRET_KEY']
CLIENT_ID = os.environ['API_CLIENT_ID']
token = os.environ['API_TOKEN']


def update_auth_token_string():
    """This will authenticate with Petfinder api and return OAuth token"""

    requests.post(
        "https://api.petfinder.com/v2/oauth2/token",
        body={
            "grant_type": "client_credentials",
            "client_id": f"{CLIENT_ID}",
            "client_secret": f"{SECRET_KEY}"
                 }
        )



def get_random_animal():
    """Get 100 animals list and pick a random one"""

    requests.get(
        "https://api.petfinder.com/v2/animals?limit=100",
        headers={"Authorization": f"Bearer {token}"})
