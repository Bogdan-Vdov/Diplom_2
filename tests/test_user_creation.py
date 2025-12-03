import pytest
import allure
from test_data_generator import generate_user_data
from api_client.client import ApiClient
from api_client.urls import BASE_URL


class TestUserCreation:
    """Тесты для создания пользователей."""
    
    @allure.title("Создание уникального пользователя")
    @allure.description("Проверка возможности создания нового уникального пользователя")
    def test_create_unique_user(self):
        """Создание уникального пользователя."""
        # Создание клиента API
        api_client = ApiClient(BASE_URL)
        
        # Генерация уникальных данных пользователя
        user_data = generate_user_data()
        
        # Отправка запроса на создание пользователя
        with allure.step("Отправка POST запроса на создание пользователя"):
            response = api_client.post("/api/auth/register", json=user_data)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и данных ответа"):
            assert response.status_code == 200
            response_data = response.json()
            # Проверяем наличие специфичных атрибутов успешного ответа
            assert "accessToken" in response_data
            assert "refreshToken" in response_data
            assert "user" in response_data
            user_info = response_data.get("user")
            assert user_info.get("email") == user_data["email"]
            assert user_info.get("name") == user_data["name"]
    
    @allure.title("Создание уже зарегистрированного пользователя")
    @allure.description("Проверка невозможности создания пользователя с уже существующими данными")
    def test_create_existing_user(self):
        """Создание пользователя, который уже зарегистрирован."""
        # Создание клиента API
        api_client = ApiClient(BASE_URL)
        
        # Генерация данных пользователя
        user_data = generate_user_data()
        
        # Создание пользователя первый раз
        with allure.step("Создание пользователя первый раз"):
            first_response = api_client.post("/api/auth/register", json=user_data)
            assert first_response.status_code == 200
        
        # Попытка создать того же пользователя второй раз
        with allure.step("Попытка создания того же пользователя второй раз"):
            second_response = api_client.post("/api/auth/register", json=user_data)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и сообщения об ошибке"):
            assert second_response.status_code == 403
            response_data = second_response.json()
            # Проверяем наличие специфичных атрибутов ошибочного ответа
            assert "message" in response_data
            assert "User already exists" in response_data.get("message", "")
    
    @allure.title("Создание пользователя без заполнения обязательного поля")
    @allure.description("Проверка невозможности создания пользователя без заполнения обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_without_required_field(self, missing_field):
        """Создание пользователя и не заполнение одного из обязательных полей."""
        # Создание клиента API
        api_client = ApiClient(BASE_URL)
        
        # Генерация данных пользователя
        user_data = generate_user_data()
        
        # Удаление одного из обязательных полей
        user_data.pop(missing_field)
        
        # Отправка запроса на создание пользователя
        with allure.step(f"Отправка POST запроса на создание пользователя без поля {missing_field}"):
            response = api_client.post("/api/auth/register", json=user_data)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и сообщения об ошибке"):
            assert response.status_code == 403
            response_data = response.json()
            # Проверяем наличие специфичных атрибутов ошибочного ответа
            assert "message" in response_data