import requests
import allure
from url import URL, UPDATE_USER
from helpers import generate_user
from data import UNAUTHORIZED


class TestUpdateUser: 

    @allure.title("Изменение email авторизованного пользователя")
    def test_update_email_after_auth_success(self, create_user):
        token = create_user["token"]
        new_email = generate_user()["email"]

        with allure.step("Отправить запрос на изменение email"):
            response = requests.patch(URL + UPDATE_USER,headers={"Authorization": token},json={"email": new_email})

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.json()["success"] is True
            assert response.json()["user"]["email"] == new_email

        
    @allure.title("Изменение имени авторизованного пользователя")
    def test_update_name_after_auth_success(self, create_user):
        token = create_user["token"]

        with allure.step("Отправить запрос на изменение имени"):
            response = requests.patch(URL + UPDATE_USER,headers={"Authorization": token},json={"name": "new_name"})

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.json()["success"] is True
            assert response.json()["user"]["name"] == "new_name"


    @allure.title("Изменение пароля авторизованного пользователя")
    def test_update_password_after_auth_success(self, create_user):
        token = create_user["token"]

        with allure.step("Отправить запрос на изменение пароля"):
            response = requests.patch(URL + UPDATE_USER,headers={"Authorization": token},json={"password": "new_password"})

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.title("Изменение email без авторизации")
    def test_update_email_without_auth_error(self):

        with allure.step("Отправить запрос на изменение email"):
            response = requests.patch(URL + UPDATE_USER,json={"email": generate_user()["email"]})

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 401
            assert response.json()["success"] is False
            assert response.json()["message"] == UNAUTHORIZED

    @allure.title("Изменение имени без авторизации")
    def test_update_name_without_auth_error(self):

        with allure.step("Отправить запрос на изменение имени"):
            response = requests.patch(URL + UPDATE_USER,json={"name": "new_name"})

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 401
            assert response.json()["success"] is False
            assert response.json()["message"] == UNAUTHORIZED

    @allure.title("Изменение пароля без авторизации")
    def test_update_password_without_auth_error(self):

        with allure.step("Отправить запрос на изменение пароля"):
            response = requests.patch(URL + UPDATE_USER,json={"password": "new_password"})

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 401
            assert response.json()["success"] is False
            assert response.json()["message"] == UNAUTHORIZED
