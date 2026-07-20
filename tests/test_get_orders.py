import requests
import allure
from url import URL, GET_ORDERS, CREATE_ORDER


class TestGetOrdersUser:

    @allure.title("Получение заказов конкрентого пользователя")
    def test_get_orders_after_auth_success(self, create_user, ingredients):
        token = create_user['token']
        payload = {'ingredients': ingredients}

        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(URL + CREATE_ORDER, headers={"Authorization": token}, json=payload)


        with allure.step("Отправить запрос на получение заказов пользователя"):
            response = requests.get(URL + GET_ORDERS, headers={"Authorization": token})

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.json()['success'] is True
        

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_without_auth_error(self):

        with allure.step("Отправить запрос на получение заказов"):
            response = requests.get(URL + GET_ORDERS)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 401
            assert response.json()['success'] is False
            assert response.json()['message'] == 'You should be authorised'

        


