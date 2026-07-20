import pytest
import requests
import allure
from url import URL, LOGIN
from data import WRONG_LOGIN


class TestLogin:

    @allure.title("Успешный логин существующего пользователя")
    def test_login_success(self, create_user):
        user = create_user['user']

        with allure.step("Отправить запрос на логин"):    
            response = requests.post(URL+LOGIN, json={"email": user["email"],"password": user["password"]})

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.json()['success'] is True


    @pytest.mark.parametrize('email, password',
                             [
                                ('xoxoxo', '123456'),
                                ('test@mail.ru', 'zyzyzy2222'),
    ]
    )
    @allure.title("Логин с неверным логином или паролем")
    def test_login_wrong_email_or_password_error(self, email, password):
        
        with allure.step("Отправить запрос на логин"):
            response = requests.post(URL+LOGIN, json={'email': email, 'password': password})
        
        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 401
            assert response.json()['success'] is False
            assert response.json()['message'] == WRONG_LOGIN
            

     