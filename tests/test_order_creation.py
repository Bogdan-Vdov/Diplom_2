import pytest
import allure
from api_client.data import TEST_INGREDIENT_IDS, PARTIAL_INGREDIENT_IDS
from api_client.client import ApiClient
from api_client.urls import BASE_URL


class TestOrderCreation:
    """Тесты для создания заказов."""
    
    @allure.title("Создание заказа с авторизацией")
    @allure.description("Проверка возможности создания заказа авторизованным пользователем")
    def test_create_order_with_auth(self, registered_user):
        """Создание заказа с авторизацией."""
        # Создание клиента API
        api_client = ApiClient(BASE_URL)
        
        # Пример ингредиентов из внешнего модуля
        order_data = {
            "ingredients": TEST_INGREDIENT_IDS
        }
        
        # Отправка запроса на создание заказа с авторизацией
        headers = {"Authorization": registered_user["access_token"]}
        with allure.step("Отправка POST запроса на создание заказа с авторизацией"):
            response = api_client.post("/api/orders", json=order_data, headers=headers)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и данных ответа"):
            assert response.status_code == 200
            response_data = response.json()
            # Проверяем наличие специфичных атрибутов успешного ответа
            assert "order" in response_data
            assert "name" in response_data
    
    @allure.title("Создание заказа без авторизации")
    @allure.description("Проверка невозможности создания заказа без авторизации")
    def test_create_order_without_auth(self):
        """Создание заказа без авторизации."""
        # Создание клиента API
        api_client = ApiClient(BASE_URL)
        
        # Пример ингредиентов из внешнего модуля
        order_data = {
            "ingredients": TEST_INGREDIENT_IDS
        }
        
        # Отправка запроса на создание заказа без авторизации
        with allure.step("Отправка POST запроса на создание заказа без авторизации"):
            response = api_client.post("/api/orders", json=order_data)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и данных ответа"):
            # Согласно документации API должен возвращаться статус 401
            assert response.status_code == 401
            response_data = response.json()
            # Проверяем наличие специфичных атрибутов ошибочного ответа
            assert "message" in response_data
    
    @allure.title("Создание заказа с ингредиентами")
    @allure.description("Проверка возможности создания заказа с корректными ингредиентами")
    def test_create_order_with_ingredients(self, registered_user):
        """Создание заказа с ингредиентами."""
        # Создание клиента API
        api_client = ApiClient(BASE_URL)
        
        # Пример корректных ингредиентов из внешнего модуля
        order_data = {
            "ingredients": PARTIAL_INGREDIENT_IDS
        }
        
        # Отправка запроса на создание заказа
        headers = {"Authorization": registered_user["access_token"]}
        with allure.step("Отправка POST запроса на создание заказа с ингредиентами"):
            response = api_client.post("/api/orders", json=order_data, headers=headers)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и данных ответа"):
            assert response.status_code == 200
            response_data = response.json()
            # Проверяем наличие специфичных атрибутов успешного ответа
            assert "order" in response_data
    
    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка невозможности создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self, registered_user):
        """Создание заказа без ингредиентов."""
        # Создание клиента API
        api_client = ApiClient(BASE_URL)
        
        # Данные заказа без ингредиентов
        order_data = {
            "ingredients": []
        }
        
        # Отправка запроса на создание заказа
        headers = {"Authorization": registered_user["access_token"]}
        with allure.step("Отправка POST запроса на создание заказа без ингредиентов"):
            response = api_client.post("/api/orders", json=order_data, headers=headers)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и сообщения об ошибке"):
            assert response.status_code == 400
            response_data = response.json()
            # Проверяем наличие специфичных атрибутов ошибочного ответа
            assert "message" in response_data
    
    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description("Проверка невозможности создания заказа с некорректными ID ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, registered_user):
        """Создание заказа с неверным хешем ингредиентов."""
        # Создание клиента API
        api_client = ApiClient(BASE_URL)
        
        # Некорректные ID ингредиентов
        order_data = {
            "ingredients": [
                "invalid_hash_1",
                "invalid_hash_2"
            ]
        }
        
        # Отправка запроса на создание заказа
        headers = {"Authorization": registered_user["access_token"]}
        with allure.step("Отправка POST запроса на создание заказа с неверным хешем ингредиентов"):
            response = api_client.post("/api/orders", json=order_data, headers=headers)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и сообщения об ошибке"):
            # Согласно документации API должен возвращаться статус 400
            assert response.status_code == 400
            response_data = response.json()
            # Проверяем наличие специфичных атрибутов ошибочного ответа
            assert "message" in response_data