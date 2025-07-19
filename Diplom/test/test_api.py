import pytest
import requests
import allure
from config import (
    REQUEST_RETRIES,
    CHROME_DRIVER_PATH,
    API_BASE_URL,
    TEST_SEARCH_DIGITS,
    TEST_SEARCH_LATIN,
    TEST_SEARCH_EMPTY,
    TEST_SEARCH_KIRILLIC,
    TEST_SEARCH_STANDARD
)

# Базовый URL для запросов
BASE_URL = API_BASE_URL
HEADERS = {'content-type': 'application/json'}

# 🔹 Позитивные тесты
@pytest.mark.positive
@allure.feature("API тесты")
@allure.story("Поиск названия по кириллице")
def test_search_by_kirillica():
    title = TEST_SEARCH_KIRILLIC
    response = requests.get(f"{BASE_URL}/search/{title}", params={"stype": 0}, headers=HEADERS)
    assert response.status_code == 200
    content_type = response.headers.get('Content-Type', '')
    if content_type.startswith('text/html'):
        print('Ответ в формате HTML')
    else:
        print(f'Ожидали HTML, но получили: {content_type}')

@pytest.mark.positive
@allure.feature("API тесты")
@allure.story("Поиск названия по латинице")
def test_search_by_latinica():
    title = TEST_SEARCH_LATIN
    response = requests.get(f"{BASE_URL}/search/{title}", params={"stype": 0}, headers=HEADERS)
    assert response.status_code == 200
    content_type = response.headers.get('Content-Type', '')
    if content_type.startswith('text/html'):
        print('Ответ в формате HTML')
    else:
        print(f'Ожидали HTML, но получили: {content_type}')

@pytest.mark.positive
@allure.feature("API тесты")
@allure.story("Поиск названия с цифрами")
def test_search_by_digits():
    title = TEST_SEARCH_DIGITS
    response = requests.get(f"{BASE_URL}/search/{title}", params={"stype": 0}, headers=HEADERS)
    assert response.status_code == 200
    content_type = response.headers.get('Content-Type', '')
    if content_type.startswith('text/html'):
        print('Ответ в формате HTML')
    else:
        print(f'Ожидали HTML, но получили: {content_type}')

# 🔹 Негативные тесты
@pytest.mark.negative
@allure.feature("API тесты")
@allure.story("Поиск названия с ошибкой в урле")
def test_search_by_url_defect():
    title = TEST_SEARCH_KIRILLIC
    response = requests.get(f"{BASE_URL}/zearch/{title}", params={"stype": 0}, headers=HEADERS)
    assert response.status_code == 404
    content_type = response.headers.get('Content-Type', '')
    if content_type.startswith('text/html'):
        print('Ответ в формате HTML')
    else:
        print(f'Ожидали HTML, но получили: {content_type}')

@pytest.mark.negative
@allure.feature("API тесты")
@allure.story("Поиск без названия")
def test_search_by_no_name():
    response = requests.get(f"{BASE_URL}/search/", params={"stype": 0}, headers=HEADERS)
    assert response.status_code == 200
    content_type = response.headers.get('Content-Type', '')
    if content_type.startswith('text/html'):
        print('Ответ в формате HTML')
    else:
        print(f'Ожидали HTML, но получили: {content_type}')
        
