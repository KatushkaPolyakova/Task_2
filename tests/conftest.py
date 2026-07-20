import pytest
import requests
from helpers import generate_user
from url import URL, CREATE_USER, UPDATE_USER, INGREDIENTS


@pytest.fixture
def create_user():
    user = generate_user()
    response = requests.post(URL+CREATE_USER, json=user)
    access_token = response.json()["accessToken"]
    yield {
        'user': user,
        'response': response,
        'token': access_token
    }
    requests.delete(URL+UPDATE_USER, headers={'Authorization': access_token})


@pytest.fixture
def ingredients():
    response = requests.get(URL+INGREDIENTS)
    return [
        response.json()['data'][0]['_id'],
        response.json()['data'][1]['_id']        
        ]

