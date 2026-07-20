import pytest 
import requests
import allure 
from url import URL, CREATE_USER
from helpers import generate_user
from data import USER_ALREADY_EXISTS, REQUIRED_FIELDS


class TestCreateUser:

    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self, create_user):
        response = create_user['response']
        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.json()['success'] is True


    @allure.title("Повторное создание пользователя")
    def test_create_same_user_error(self, create_user):

        with allure.step("Отправить запрос на повторное создание пользователя"):
            response = requests.post(URL+CREATE_USER, json=create_user['user'])
        
        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 403
            assert response.json()['message'] == USER_ALREADY_EXISTS
            assert response.json()['success'] is False


    @pytest.mark.parametrize('field',['email', 'password', 'name'])
    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_without_data_error(self, field):
        user = generate_user()
        del user[field]

        with allure.step("Отправить запрос на создание пользователя"):
            response = requests.post(URL+CREATE_USER, json=user)
        
        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 403
            assert response.json()['message'] == REQUIRED_FIELDS
            assert response.json()['success'] is False

     
