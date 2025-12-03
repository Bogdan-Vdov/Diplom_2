import pytest
from api_client.urls import BASE_URL
from api_client.client import ApiClient
from test_data_generator import generate_user_data


def pytest_configure(config):
    """Конфигурация pytest."""
    config.option.allure_report_dir = "./allure-results"


@pytest.fixture(scope="function")
def registered_user():
    """Фикстура для создания зарегистрированного пользователя."""
    # Создание тестового пользователя
    test_user = generate_user_data()
    api_client = ApiClient(BASE_URL)
    register_response = api_client.post("/api/auth/register", json=test_user)
    
    # Проверяем, что регистрация успешна
    assert register_response.status_code == 200, f"Ошибка при создании тестового пользователя: {register_response.status_code}"
    
    registered_user_data = register_response.json()
    return {
        "user_data": test_user,
        "registered_data": registered_user_data,
        "access_token": registered_user_data.get("accessToken")
    }


@pytest.fixture(scope="function")
def authorized_headers(registered_user):
    """Фикстура для создания заголовков авторизации."""
    return {"Authorization": registered_user["access_token"]}