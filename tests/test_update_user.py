import pytest
import requests
import allure
from url import URL, UPDATE_USER


class TestUpdateUser:

    @pytest.mark.parametrize('field, value', 
                             [
                                 ('email', 'new_email_new_@mail.ru'),
                                 ('password', 'new_password'),
                                 ('name', 'new_name'),
                             ] )
    @allure.title('Изменение данных авторизованного пользователя')
    def test_update_after_auth_success(self, create_user, field, value):
        token = create_user['token']
        payload = {field:value}

        with allure.step('Отправить запрос на измнение данных'):
            response = requests.patch(URL+UPDATE_USER, headers={'Authorization': token}, json=payload)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.json()['success'] is True
            if field == 'email':
                assert response.json()['user']['email'] ==  value
            elif field == 'name':
                assert response.json()['user']['name'] == value


    @pytest.mark.parametrize('field, value', 
                             [
                                 ('email', 'new_email@mail.ru'),
                                 ('password', 'new_password'),
                                 ('name', 'new_name'),
                             ] )
    @allure.title("Изменение данных пользователя без авторизации")
    def test_update_user_without_auth_error(self, field, value):
        payload = {field:value}
        
        with allure.step('Отправить запрос на измнение данных без авторизации'):
            response = requests.patch(URL+UPDATE_USER, json=payload)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 401
            assert response.json()['success'] is False
            assert response.json()['message'] == 'You should be authorised'

