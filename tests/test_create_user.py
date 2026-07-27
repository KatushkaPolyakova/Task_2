import pytest 
import requests
import allure 
from url import URL, CREATE_USER, UPDATE_USER
from helpers import generate_user
from data import USER_ALREADY_EXISTS, REQUIRED_FIELDS


class TestCreateUser:

    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self):
        user = generate_user()
        
        with allure.step("Отправить запрос на создание пользователя"):
            response = requests.post(URL+CREATE_USER, json=user)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.json()['success'] is True

        with allure.step("Удалить пользователя"):
            token = response.json()["accessToken"]
            requests.delete(URL + UPDATE_USER,headers={"Authorization": token})


    @allure.title("Повторное создание пользователя")
    def test_create_same_user_error(self):
        user = generate_user()

        with allure.step("Отправить запрос на создание пользователя"):
            response = requests.post(URL+CREATE_USER, json=user)

        with allure.step("Отправить запрос на повторное создание пользователя"):
            second_response = requests.post(URL+CREATE_USER, json=user)
        
        with allure.step("Проверить ответ сервера"):
            assert second_response.status_code == 403
            assert second_response.json()['message'] == USER_ALREADY_EXISTS
            assert second_response.json()['success'] is False

        with allure.step("Удалить пользователя"):
            token = response.json()["accessToken"]
            requests.delete(URL + UPDATE_USER,headers={"Authorization": token})


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

     
