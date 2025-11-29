import pytest


def pytest_configure(config):
    """Конфигурация pytest."""
    config.option.allure_report_dir = "./allure-results"


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL для API."""
    return "https://stellarburgers.education-services.ru"