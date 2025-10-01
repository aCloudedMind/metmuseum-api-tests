import logging
import sys
from typing import Dict, Any
import json


def setup_logger():
    """Настройка логгера для тестов"""
    logger = logging.getLogger('metmuseum_api_tests')
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger


def log_request(logger, method: str, url: str, params: Dict[str, Any] = None):
    """Логирование запроса"""
    logger.info(f"REQUEST: {method} {url}")
    if params:
        logger.info(f"PARAMS: {json.dumps(params, indent=2)}")


def log_response(logger, status_code: int, response_data: Any):
    """Логирование ответа"""
    logger.info(f"RESPONSE STATUS: {status_code}")
    if response_data:
        logger.info(f"RESPONSE DATA: {json.dumps(response_data, indent=2)}")


def log_error(logger, error: Exception):
    """Логирование ошибки"""
    logger.error(f"ERROR: {str(error)}")