import pytest
import requests
from helpers import generate_user
from url import URL, CREATE_USER, UPDATE_USER, INGREDIENTS


@pytest.fixture
def user_data():
    return generate_user()


@pytest.fixture
def create_user(user_data):
    response = requests.post(URL+CREATE_USER, json=user_data)
    access_token = response.json()["accessToken"]
    yield {
        'user': user_data,
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

