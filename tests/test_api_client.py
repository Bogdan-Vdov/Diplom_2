import pytest
from api_client.client import ApiClient


class TestApiClient:
    """Тесты для API клиента."""
    
    def test_init(self):
        """Тест инициализации клиента."""
        base_url = "https://jsonplaceholder.typicode.com"
        client = ApiClient(base_url)
        
        assert client.base_url == base_url
        assert client.timeout == 30
    
    def test_init_with_custom_timeout(self):
        """Тест инициализации клиента с кастомным таймаутом."""
        base_url = "https://jsonplaceholder.typicode.com"
        timeout = 60
        client = ApiClient(base_url, timeout=timeout)
        
        assert client.base_url == base_url
        assert client.timeout == timeout
    
    @pytest.mark.skip(reason="Требуется запущенный сервер для тестирования")
    def test_get_request(self):
        """Тест GET запроса."""
        client = ApiClient("https://jsonplaceholder.typicode.com")
        response = client.get("/posts/1")
        
        assert response.status_code == 200
        assert "userId" in response.json()
        assert "id" in response.json()
        assert "title" in response.json()
        assert "body" in response.json()