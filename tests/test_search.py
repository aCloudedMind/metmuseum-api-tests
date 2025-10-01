import pytest
import requests
from models.art_objects import SearchResponse, DepartmentsResponse
from utils.logger import log_request, log_response, log_error


class TestSearch:
    """Тесты для поиска произведений искусства"""
    
    def test_search_by_keyword(self, base_url, session, logger, search_keyword):
        """Тест поиска по ключевому слову"""
        try:
            url = f"{base_url}/search"
            params = {"q": search_keyword}
            
            log_request(logger, "GET", url, params)
            response = session.get(url, params=params)
            log_response(logger, response.status_code, response.json())
            
            # Проверка HTTP статуса
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            
            # Валидация структуры ответа
            search_response = SearchResponse(**response.json())
            
            # Проверка наличия результатов
            assert search_response.total >= 0
            if search_response.total > 0:
                assert search_response.objectIDs is not None
                assert len(search_response.objectIDs) > 0
            
            logger.info(f"Search for '{search_keyword}' returned {search_response.total} results")
            
        except Exception as e:
            log_error(logger, e)
            raise
    
    def test_get_departments(self, base_url, session, logger):
        """Тест получения списка отделов музея"""
        try:
            url = f"{base_url}/departments"
            
            log_request(logger, "GET", url)
            response = session.get(url)
            log_response(logger, response.status_code, response.json())
            
            assert response.status_code == 200
            
            # Валидация структуры ответа
            departments_response = DepartmentsResponse(**response.json())
            
            # Проверка наличия отделов
            assert len(departments_response.departments) > 0
            
            logger.info(f"Successfully retrieved {len(departments_response.departments)} departments")
            
        except Exception as e:
            log_error(logger, e)
            raise