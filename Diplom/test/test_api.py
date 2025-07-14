import pytest
import requests
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


@allure.feature("API Testing")
@allure.story("Поиск на кириллице")
def test_search_kirillitsa(api_client):
    """
    Проверяет возврат корректных результатов при поиске на кириллице.
    Метод: GET
    Входные данные: "Приключения Алисы в Стране Чудес: Льюис Кэрролл"
    """
    params = {'q': TEST_SEARCH_KIRILLIC}
    response = api_client.get(f'{API_BASE_URL}/search', params=params)
    data = response.json()
    assert response.status_code == 200, f'Ошибка поиска на кириллице: {data}'
    assert (
        len(data['results']) > 0
    ), f'Не найдены результаты поиска по запросу: {TEST_SEARCH_KIRILLIC}'


@allure.feature("API Testing")
@allure.story("Поиск по названию с цифрами")
def test_search_with_digits(api_client):
    """
    Проверяет корректность поиска по названию с цифрами.
    Метод: GET
    Входные данные: "1000 животных с наклейками"
    """
    params = {'q': TEST_SEARCH_DIGITS}
    response = api_client.get(f'{API_BASE_URL}/search', params=params)
    data = response.json()
    assert (
        response.status_code == 200
    ), f'Ошибка поиска по названию с цифрами: {data}'

    assert (
        len(data['results']) > 0
    ), f'Не найдены результаты поиска по запросу: {TEST_SEARCH_DIGITS}'


@allure.feature("API Testing")
@allure.story("Поиск на латинице")
def test_search_latinica(api_client):
    """
    Проверяет, что API возвращает корректные результаты при поиске на латинице.
    Метод: GET
    Входные данные: "Harry Potter & the Prisoner of Azkaban: Joanne Rowling"
    """
    params = {'q': TEST_SEARCH_LATIN}
    response = api_client.get(f'{API_BASE_URL}/search', params=params)
    data = response.json()
    assert response.status_code == 200, f'Ошибка поиска на латинице: {data}'
    assert (
        len(data['results']) > 0
    ), f'Не найдены результаты поиска по запросу: {TEST_SEARCH_LATIN}'


@allure.feature("API Testing")
@allure.story("Поиск без названия")
def test_search_without_name(api_client):
    """
    Проверяет, что API корректно обрабатывает пустой поисковый запрос.
    Метод: GET
    Входные данные: ""
    """
    params = {'q': TEST_SEARCH_EMPTY}
    response = api_client.get(f'{API_BASE_URL}/search', params=params)
    data = response.json()
    assert response.status_code == 200, f"Ошибка поиска без названия: {data}"
    assert (
        len(data['results']) == 0
    ), 'При пустом запросе получены некорректные результаты.'


@allure.feature("API Testing")
@allure.story("Стандартный поиск по названию")
def test_standard_search(api_client):
    """
    Проверяет корректность поиска по названию.
    Метод: GET
    Входные данные: "Война и мир"
    """
    params = {'q': TEST_SEARCH_STANDARD}
    response = api_client.get(f'{API_BASE_URL}/search', params=params)
    data = response.json()
    assert response.status_code == 200, f'Ошибка стандартного поиска: {data}'
    assert (
        len(data['results']) > 0
    ), (
        f'Не найдены результаты поиска по стандартному запросу: '
        f'{TEST_SEARCH_STANDARD}'
    )
