import pytest
import allure
from api_client.data import TEST_INGREDIENT_IDS, PARTIAL_INGREDIENT_IDS


class TestOrderCreation:
    """Тесты для создания заказов."""
    
    @allure.title("Создание заказа с авторизацией")
    @allure.description("Проверка возможности создания заказа авторизованным пользователем")
    def test_create_order_with_auth(self, api_client, authorized_headers):
        """Создание заказа с авторизацией."""
        # Пример ингредиентов из внешнего модуля
        order_data = {
            "ingredients": TEST_INGREDIENT_IDS
        }
        
        # Отправка запроса на создание заказа с авторизацией
        with allure.step("Отправка POST запроса на создание заказа с авторизацией"):
            response = api_client.post("/api/orders", json=order_data, headers=authorized_headers)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и данных ответа"):
            assert response.status_code == 200
            response_data = response.json()
            assert response_data.get("success") is True
            assert "order" in response_data
            assert response_data.get("name") is not None
    
    @allure.title("Создание заказа без авторизации")
    @allure.description("Проверка невозможности создания заказа без авторизации")
    def test_create_order_without_auth(self, api_client):
        """Создание заказа без авторизации."""
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
            assert response_data.get("success") is False
    
    @allure.title("Создание заказа с ингредиентами")
    @allure.description("Проверка возможности создания заказа с корректными ингредиентами")
    def test_create_order_with_ingredients(self, api_client, authorized_headers):
        """Создание заказа с ингредиентами."""
        # Пример корректных ингредиентов из внешнего модуля
        order_data = {
            "ingredients": PARTIAL_INGREDIENT_IDS
        }
        
        # Отправка запроса на создание заказа
        with allure.step("Отправка POST запроса на создание заказа с ингредиентами"):
            response = api_client.post("/api/orders", json=order_data, headers=authorized_headers)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и данных ответа"):
            assert response.status_code == 200
            response_data = response.json()
            assert response_data.get("success") is True
            assert "order" in response_data
    
    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка невозможности создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self, api_client, authorized_headers):
        """Создание заказа без ингредиентов."""
        # Данные заказа без ингредиентов
        order_data = {
            "ingredients": []
        }
        
        # Отправка запроса на создание заказа
        with allure.step("Отправка POST запроса на создание заказа без ингредиентов"):
            response = api_client.post("/api/orders", json=order_data, headers=authorized_headers)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и сообщения об ошибке"):
            assert response.status_code == 400
            response_data = response.json()
            assert response_data.get("success") is False
    
    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description("Проверка невозможности создания заказа с некорректными ID ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, api_client, authorized_headers):
        """Создание заказа с неверным хешем ингредиентов."""
        # Некорректные ID ингредиентов
        order_data = {
            "ingredients": [
                "invalid_hash_1",
                "invalid_hash_2"
            ]
        }
        
        # Отправка запроса на создание заказа
        with allure.step("Отправка POST запроса на создание заказа с неверным хешем ингредиентов"):
            response = api_client.post("/api/orders", json=order_data, headers=authorized_headers)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и сообщения об ошибке"):
            # Согласно документации API должен возвращаться статус 400
            assert response.status_code == 400
            response_data = response.json()
            assert response_data.get("success") is False