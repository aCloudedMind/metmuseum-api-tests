import pytest
import requests
from models.art_objects import ArtObject
from utils.logger import log_request, log_response, log_error


class TestArtObject:
    """Тесты для работы с объектами искусства"""
    
    def test_get_art_object_by_valid_id(self, base_url, session, logger, valid_object_id):
        """Тест получения информации о произведении искусства по валидному ID"""
        try:
            url = f"{base_url}/objects/{valid_object_id}"
            
            log_request(logger, "GET", url)
            response = session.get(url)
            log_response(logger, response.status_code, response.json())
            
            # Проверка HTTP статуса
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            
            # Валидация структуры данных с помощью Pydantic
            art_object = ArtObject(**response.json())
            
            # Дополнительные проверки полей
            assert art_object.objectID == valid_object_id
            assert art_object.title is not None
            assert art_object.artistDisplayName is not None
            
            logger.info(f"Successfully validated art object: {art_object.title}")
            
        except Exception as e:
            log_error(logger, e)
            raise
    
    def test_get_art_object_by_invalid_id(self, base_url, session, logger, invalid_object_id):
        """Тест получения информации о произведении искусства по невалидному ID"""
        try:
            url = f"{base_url}/objects/{invalid_object_id}"
            
            log_request(logger, "GET", url)
            response = session.get(url)
            log_response(logger, response.status_code, response.text)
            
            # Проверка HTTP статуса для несуществующего объекта
            assert response.status_code == 404, f"Expected 404, got {response.status_code}"
            
            logger.info("Successfully handled invalid object ID request")
            
        except Exception as e:
            log_error(logger, e)
            raise