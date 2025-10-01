import pytest
import requests
from utils.logger import setup_logger


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL API Метрополитен музея"""
    return "https://collectionapi.metmuseum.org/public/collection/v1"


@pytest.fixture(scope="session")
def session():
    """Сессия для HTTP запросов"""
    return requests.Session()


@pytest.fixture(scope="session")
def logger():
    """Логгер для тестов"""
    return setup_logger()


@pytest.fixture
def valid_object_id():
    """Валидный ID объекта для тестирования"""
    return 436535  # Van Gogh's "The Starry Night"


@pytest.fixture
def invalid_object_id():
    """Невалидный ID объекта для тестирования"""
    return 999999999


@pytest.fixture
def search_keyword():
    """Ключевое слово для поиска"""
    return "monet"