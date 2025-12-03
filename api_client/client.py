import requests
from typing import Optional, Dict, Any


class ApiClient:
    """Базовый API клиент для выполнения HTTP запросов."""
    
    def __init__(self, base_url: str, timeout: int = 30):
        """
        Инициализация API клиента.
        
        Args:
            base_url: Базовый URL для API
            timeout: Таймаут для запросов в секундах
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> requests.Response:
        """
        Выполнение HTTP запроса.
        
        Args:
            method: HTTP метод (GET, POST, PUT, DELETE и т.д.)
            endpoint: Эндпоинт API
            params: Параметры запроса
            data: Данные формы
            json: JSON данные
            headers: Заголовки запроса
            
        Returns:
            Объект Response от requests
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json,
            headers=headers,
            timeout=self.timeout
        )
        
        return response
    
    def get(
        self,
        endpoint: str,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> requests.Response:
        """Выполнение GET запроса."""
        return self._make_request('GET', endpoint, params=params, headers=headers)
    
    def post(
        self,
        endpoint: str,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> requests.Response:
        """Выполнение POST запроса."""
        return self._make_request('POST', endpoint, data=data, json=json, headers=headers)
    
    def put(
        self,
        endpoint: str,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> requests.Response:
        """Выполнение PUT запроса."""
        return self._make_request('PUT', endpoint, data=data, json=json, headers=headers)
    
    def delete(
        self,
        endpoint: str,
        headers: Optional[Dict] = None
    ) -> requests.Response:
        """Выполнение DELETE запроса."""
        return self._make_request('DELETE', endpoint, headers=headers)