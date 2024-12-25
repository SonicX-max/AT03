import pytest
import requests
from unittest.mock import patch
from main import get_random_cat_image

def test_successful_request():
    """Тест успешного запроса с TheCatAPI."""
    mock_response = [{"url": "https://example.com/cat.jpg"}]
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_random_cat_image()
        assert result == "https://example.com/cat.jpg"

def test_unsuccessful_request():
    """Тест неуспешного запроса с TheCatAPI."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404

        result = get_random_cat_image()
        assert result is None

def test_request_exception():
    """Тест обработки исключения при запросе."""
    with patch("requests.get", side_effect=Exception("Connection error")):
        result = get_random_cat_image()
        assert result is None