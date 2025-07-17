import pytest
import requests
from bs4 import BeautifulSoup
from config import (
    REQUEST_RETRIES,
    API_BASE_URL,
    TEST_SEARCH_DIGITS,
    TEST_SEARCH_LATIN,
    TEST_SEARCH_EMPTY,
    TEST_SEARCH_KIRILLIC,
    TEST_SEARCH_STANDARD
)
import allure


@pytest.fixture(scope='session')
def api_client():
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=REQUEST_RETRIES)
    session.mount(API_BASE_URL, adapter)
    return session


@allure.feature("HTML Parsing Tests")
@allure.story("Поиск на кириллице")
def test_search_kirillitsa():
    """
    Проверяет возврат корректных результатов при поиске на кириллице.
    Метод: GET
    Входные данные: "Приключения Алисы в Стране Чудес: Льюис Кэрролл"
    """
    url = f"{API_BASE_URL}/search/{TEST_SEARCH_KIRILLIC}"
    response = requests.get(url)
    assert response.status_code == 200, f'Ошибка поиска на кириллице: {response.text}'

    soup = BeautifulSoup(response.text, 'html.parser')
    product_cards = soup.find_all('div', class_='product-card__top')
    assert len(product_cards) > 0, f'Не найдены результаты поиска по запросу: {TEST_SEARCH_KIRILLIC}'


@allure.feature("HTML Parsing Tests")
@allure.story("Поиск по названию с цифрами")
def test_search_with_digits():
    """
    Проверяет корректность поиска по названию с цифрами.
    Метод: GET
    Входные данные: "1000 животных с наклейками"
    """
    url = f"{API_BASE_URL}/search/{TEST_SEARCH_DIGITS}"
    response = requests.get(url)
    assert response.status_code == 200, f'Ошибка поиска по названию с цифрами: {response.text}'

    soup = BeautifulSoup(response.text, 'html.parser')
    product_cards = soup.find_all('div', class_='product-card__top')
    assert len(product_cards) > 0, f'Не найдены результаты поиска по запросу: {TEST_SEARCH_DIGITS}'


@allure.feature("HTML Parsing Tests")
@allure.story("Поиск на латинице")
def test_search_latinica():
    """
    Проверяет, что API возвращает корректные результаты при поиске на латинице.
    Метод: GET
    Входные данные: "Harry Potter & the Prisoner of Azkaban: Joanne Rowling"
    """
    url = f"{API_BASE_URL}/search/{TEST_SEARCH_LATIN}"
    response = requests.get(url)
    assert response.status_code == 200, f'Ошибка поиска на латинице: {response.text}'

    soup = BeautifulSoup(response.text, 'html.parser')
    product_cards = soup.find_all('div', class_='product-card__top')
    assert len(product_cards) > 0, f'Не найдены результаты поиска по запросу: {TEST_SEARCH_LATIN}'


@allure.feature("HTML Parsing Tests")
@allure.story("Поиск без названия")
def test_search_without_name():
    """
    Проверяет, что API корректно обрабатывает пустой поисковый запрос.
    Метод: GET
    Входные данные: ""
    """
    url = f"{API_BASE_URL}/search/"
    response = requests.get(url)
    assert response.status_code == 200, f"Ошибка поиска без названия: {response.text}"

    soup = BeautifulSoup(response.text, 'html.parser')
    product_cards = soup.find_all('div', class_='product-card__top')
    assert len(product_cards) == 0, 'При пустом запросе получены некорректные результаты.'


@allure.feature("HTML Parsing Tests")
@allure.story("Стандартный поиск по названию")
def test_standard_search():
    """
    Проверяет корректность поиска по названию.
    Метод: GET
    Входные данные: "Война и мир"
    """
    url = f"{API_BASE_URL}/search/{TEST_SEARCH_STANDARD}"
    response = requests.get(url)
    assert response.status_code == 200, f'Ошибка стандартного поиска: {response.text}'

    soup = BeautifulSoup(response.text, 'html.parser')
    product_cards = soup.find_all('div', class_='product-card__top')
    assert len(product_cards) > 0, f'Не найдены результаты поиска по стандартному запросу: {TEST_SEARCH_STANDARD}'
