import pytest
import allure


class TestUserLogin:
    """Тесты для логина пользователей."""
    
    @allure.title("Вход под существующим пользователем")
    @allure.description("Проверка возможности входа под существующим пользователем")
    def test_login_existing_user(self, api_client, registered_user):
        """Вход под существующим пользователем."""
        # Данные для входа
        login_data = {
            "email": registered_user["user_data"]["email"],
            "password": registered_user["user_data"]["password"]
        }
        
        # Отправка запроса на вход
        with allure.step("Отправка POST запроса на вход пользователя"):
            response = api_client.post("/api/auth/login", json=login_data)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и данных ответа"):
            assert response.status_code == 200
            response_data = response.json()
            assert response_data.get("success") is True
            assert "accessToken" in response_data
            assert "refreshToken" in response_data
            assert response_data.get("user") is not None
            user_info = response_data.get("user")
            assert user_info.get("email") == registered_user["user_data"]["email"]
            assert user_info.get("name") == registered_user["user_data"]["name"]
    
    @allure.title("Вход с неверным логином и паролем")
    @allure.description("Проверка невозможности входа с неверными учетными данными")
    def test_login_with_invalid_credentials(self, api_client):
        """Вход с неверным логином и паролем."""
        # Неверные данные для входа
        invalid_login_data = {
            "email": "invalid@example.com",
            "password": "wrongpassword"
        }
        
        # Отправка запроса на вход
        with allure.step("Отправка POST запроса на вход с неверными данными"):
            response = api_client.post("/api/auth/login", json=invalid_login_data)
        
        # Проверка результата в соответствии с документацией API
        with allure.step("Проверка статус кода и сообщения об ошибке"):
            assert response.status_code == 401
            response_data = response.json()
            assert response_data.get("success") is False