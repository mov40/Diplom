import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.labirint_pages import HomePage, SearchPage, GenresPage
from config import LABIRINT_URL, SEARCH_KEYWORD, SEARCH_GENRE, SEARCH_CYRILLIC
import allure


@pytest.fixture(scope='session', autouse=True)
def browser_setup(request):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    request.addfinalizer(lambda: driver.quit())
    return driver


@allure.feature("UI Testing")
@allure.story("Проверка поиска по ключевому слову")
def test_search_by_keyword(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    search_page = SearchPage(browser_setup)
    found = search_page.perform_search(SEARCH_KEYWORD)
    assert (
        found
        ), f"Поиск по слову '{SEARCH_KEYWORD}' не нашёл результатов."


@allure.feature("UI Testing")
@allure.story("Проверка поиска по жанру")
def test_search_by_genre(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    genres_page = GenresPage(browser_setup)
    genres_page.go_to_genres_section()
    search_page = genres_page.choose_genre(SEARCH_GENRE)
    found = search_page.check_results_present()
    assert (
        found
    ), f"Поиск по жанру '{SEARCH_GENRE}' не нашёл результатов."


@allure.feature("UI Testing")
@allure.story("Проверка поиска на киррилице")
def test_search_by_cyrillic(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    search_page = SearchPage(browser_setup)
    found = search_page.perform_search(SEARCH_CYRILLIC)
    assert (
        found
    ), f"Поиск по запросу '{SEARCH_CYRILLIC}' не нашёл результатов."


@allure.feature("UI Testing")
@allure.story("Проверка отображения главной страницы")
def test_return_homepage(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    home_page.return_to_homepage()
    actual_url = browser_setup.current_url
    expected_url = LABIRINT_URL
    assert (
        actual_url == expected_url
    ), f"Ошибка возврата на главную страницу: {actual_url}"


@allure.feature("UI Testing")
@allure.story("Проверка работоспособности меню поиска")
def test_search_menu_functionality(browser_setup):
    home_page = HomePage(browser_setup)
    home_page.open(LABIRINT_URL)
    search_page = SearchPage(browser_setup)
    search_page.send_text(" ", search_page.INPUT_SEARCH_FIELD)
    menu_is_visible = search_page.wait_until_visible(
        search_page.RESULTS_CONTAINER
    )
    assert (
        menu_is_visible.is_displayed()
    ), "Меню поиска не появилось после ввода символов."
