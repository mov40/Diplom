import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import(
    REQUEST_RETRIES,
    CHROME_DRIVER_PATH,
    API_BASE_URL,
    TEST_SEARCH_DIGITS,
    TEST_SEARCH_LATIN,
    TEST_SEARCH_EMPTY,
    TEST_SEARCH_KIRILLIC,
    TEST_SEARCH_STANDARD
)
import allure


# 🔹 Фикстура для инициализации браузера
@pytest.fixture(scope='session')
def browser():
    """Инициализирует браузер и закрывает окно после завершения."""
    service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


# 🔹 Тест на поиск на кириллице
@allure.feature("HTML Parsing Tests")
@allure.story("Поиск на кириллице")
def test_search_kirillitsa(browser):
    """
    Проверяет корректность результатов поиска на кириллице.
    """
    base_url = API_BASE_URL
    search_query = TEST_SEARCH_KIRILLIC

    # Переходим на главную страницу
    browser.get(base_url)

    # Находим поле поиска и вводим запрос
    wait = WebDriverWait(browser, 10)
    search_field = wait.until(EC.presence_of_element_located((By.ID, 'search-field')))
    search_field.clear()
    search_field.send_keys(search_query)

    # Отправляем запрос
    search_field.submit()

    # Ждём появления элементов с результатами поиска
    wait = WebDriverWait(browser, 10)
    results = wait.until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, 'product-card__top'))
    )

    # Проверяем, что результаты присутствуют
    assert len(results) > 0, f'Не найдены результаты поиска по запросу: {search_query}'


# 🔹 Тест на поиск по названию с цифрами
@allure.feature("HTML Parsing Tests")
@allure.story("Поиск по названию с цифрами")
def test_search_with_digits(browser):
    """
    Проверяет корректность поиска по названию с цифрами.
    """
    base_url = API_BASE_URL
    search_query = TEST_SEARCH_DIGITS

    # Переходим на главную страницу
    browser.get(base_url)

    # Находим поле поиска и вводим запрос
    wait = WebDriverWait(browser, 10)
    search_field = wait.until(EC.presence_of_element_located((By.ID, 'search-field')))
    search_field.clear()
    search_field.send_keys(search_query)

    # Отправляем запрос
    search_field.submit()

    # Ждём появления элементов с результатами поиска
    wait = WebDriverWait(browser, 10)
    results = wait.until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, 'product-card__top'))
    )

    # Проверяем, что результаты присутствуют
    assert len(results) > 0, f'Не найдены результаты поиска по запросу: {search_query}'


# 🔹 Тест на поиск на латинице
@allure.feature("HTML Parsing Tests")
@allure.story("Поиск на латинице")
def test_search_latinica(browser):
    """
    Проверяет, что поиск на латинице возвращает корректные результаты.
    """
    base_url = API_BASE_URL
    search_query = TEST_SEARCH_LATIN

    # Переходим на главную страницу
    browser.get(base_url)

    # Находим поле поиска и вводим запрос
    wait = WebDriverWait(browser, 10)
    search_field = wait.until(EC.presence_of_element_located((By.ID, 'search-field')))
    search_field.clear()
    search_field.send_keys(search_query)

    # Отправляем запрос
    search_field.submit()

    # Ждём появления элементов с результатами поиска
    wait = WebDriverWait(browser, 10)
    results = wait.until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, 'product-card__top'))
    )

    # Проверяем, что результаты присутствуют
    assert len(results) > 0, f'Не найдены результаты поиска по запросу: {search_query}'


# 🔹 Тест на поиск без названия
@allure.feature("HTML Parsing Tests")
@allure.story("Поиск без названия")
def test_search_without_name(browser):
    """
    Проверяет корректность обработки пустых поисковых запросов.
    """
    base_url = API_BASE_URL

    # Переходим на главную страницу
    browser.get(base_url)

    # Находим поле поиска и отправляем пустой запрос
    wait = WebDriverWait(browser, 10)
    search_field = wait.until(EC.presence_of_element_located((By.ID, 'search-field')))
    search_field.clear()
    search_field.submit()

    # Ждём появления элемента, сигнализирующего об отсутствии результатов
    wait = WebDriverWait(browser, 10)
    no_results_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(), "ничего не нашли")]'))
    )

    # Проверяем, что появилась надпись "ничего не нашли"
    assert no_results_message.is_displayed(), 'Не было получено уведомления об отсутствии результатов.'


# 🔹 Тест на стандартный поиск по названию
@allure.feature("HTML Parsing Tests")
@allure.story("Стандартный поиск по названию")
def test_standard_search(browser):
    """
    Проверяет корректность стандартного поиска по названию.
    """
    base_url = API_BASE_URL
    search_query = TEST_SEARCH_STANDARD

    # Переходим на главную страницу
    browser.get(base_url)

    # Находим поле поиска и вводим запрос
    wait = WebDriverWait(browser, 10)
    search_field = wait.until(EC.presence_of_element_located((By.ID, 'search-field')))
    search_field.clear()
    search_field.send_keys(search_query)

    # Отправляем запрос
    search_field.submit()

    # Ждём появления элементов с результатами поиска
    wait = WebDriverWait(browser, 10)
    results = wait.until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, 'product-card__top'))
    )

    # Проверяем, что результаты присутствуют
    assert len(results) > 0, f'Не найдены результаты поиска по запросу: {search_query}'
