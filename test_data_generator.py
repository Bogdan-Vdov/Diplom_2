import random
import string
from typing import Dict, Any


def generate_random_string(length: int = 10) -> str:
    """Генерация случайной строки заданной длины."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_user_data() -> Dict[str, str]:
    """Генерация уникальных данных пользователя для тестов."""
    return {
        "email": f"test_{generate_random_string(8)}@example.com",
        "password": generate_random_string(12),
        "name": f"TestUser_{generate_random_string(6)}"
    }


def generate_existing_user_data() -> Dict[str, str]:
    """Генерация данных для уже существующего пользователя."""
    return {
        "email": "existing_user@example.com",
        "password": "password123",
        "name": "ExistingUser"
    }