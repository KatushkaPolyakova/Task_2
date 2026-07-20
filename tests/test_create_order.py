import requests
import allure
from url import URL, CREATE_ORDER


class TestCreateOrder:

    @allure.title("Успешное создание заказа с ингредиентами авторизованным пользователем")
    def test_create_order_after_auth_with_ingredient_success(self, create_user, ingredients):
        token = create_user['token']
        payload = {'ingredients': ingredients}

        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(URL + CREATE_ORDER, headers={"Authorization": token},json=payload)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200
            assert response.json()['success'] is True


    @allure.title("Создание заказа с ингредиентами без авторизации")
    def test_create_order_without_auth_with_ingredient(self, ingredients):
        payload = {'ingredients': ingredients}

        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(URL + CREATE_ORDER, json=payload)
                     
        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 401
            assert response.json()['success'] is False
      

    @allure.title("Создание заказа без ингредиентов")  
    def test_create_order_without_ingredients_error(self, create_user):
        token = create_user['token']
        payload = {'ingredients': []}

        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(URL + CREATE_ORDER, headers={"Authorization": token}, json=payload)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 400
            assert response.json()['success'] is False
            assert response.json()['message'] == 'Ingredient ids must be provided'


    @allure.title("Создание заказа с неверным хэшем ингредиентов")
    def test_create_order_with_wrong_hash_ingredients_error(self, create_user):
        token = create_user['token']
        payload = {'ingredients': ['1111111111']}

        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(URL + CREATE_ORDER, headers={"Authorization": token}, json=payload)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 500
        
