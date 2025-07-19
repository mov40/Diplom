import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pages.labirint_pages import HomePage, SearchPage, GenresPage
from config import CHROME_DRIVER_PATH, LABIRINT_URL, SEARCH_KEYWORD, SEARCH_GENRE, SEARCH_CYRILLIC
import allure


@pytest.fixture(scope='session', autouse=True)
def browser_setup(request):
    options = Options()
    options.add_argument("--headless")
    service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    request.addfinalizer(lambda: driver.quit())
    return driver


@allure.feature("UI Testing")
@allure.story("Проверка поиска по ключевому слову")
def test_search_by_keyword(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    search_page = SearchPage(browser_setup)
    found = search_page.perform_search(SEARCH_KEYWORD)
    assert found, f"Не удалось найти результаты поиска по слову '{SEARCH_KEYWORD}'."


@allure.feature("UI Testing")
@allure.story("Проверка поиска по жанру")
def test_search_by_genre(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    genres_page = GenresPage(browser_setup)
    genres_page.go_to_genres_section()
    search_page = genres_page.choose_genre(SEARCH_GENRE)
    found = search_page.check_results_present()
    assert found, f"Не найдены результаты поиска по жанру '{SEARCH_GENRE}'."


@allure.feature("UI Testing")
@allure.story("Проверка поиска на кириллице")
def test_search_by_cyrillic(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    search_page = SearchPage(browser_setup)
    found = search_page.perform_search(SEARCH_CYRILLIC)
    assert found, f"Не найдены результаты поиска по запросу '{SEARCH_CYRILLIC}'."


@allure.feature("UI Testing")
@allure.story("Проверка отображения главной страницы")
def test_return_homepage(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    home_page.return_to_homepage()
    current_url = browser_setup.current_url
    assert current_url == LABIRINT_URL, f"Ошибка возврата на главную страницу: {current_url}"


@allure.feature("UI Testing")
@allure.story("Проверка работоспособности меню поиска")
def test_search_menu_functionality(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    search_page = SearchPage(browser_setup)
    search_page.send_text(" ", search_page.INPUT_SEARCH_FIELD)
    menu_is_visible = search_page.wait_until_visible(search_page.RESULTS_CONTAINER)
    assert menu_is_visible.is_displayed(), "Меню поиска не появилось после ввода символов."
