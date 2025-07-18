from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу {url}')
    def open(self, url):
        with allure.step(f'Переход на сайт "{url}"'):
            self.driver.get(url)

    @allure.step('Ожидание появления элемента {locator}')
    def wait_until_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Щёлкнуть по элементу {locator}')
    def click(self, locator):
        element = self.wait_until_visible(locator)
        element.click()

    @allure.step('Набрать текст {text} в поле {locator}')
    def send_text(self, text, locator):
        field = self.wait_until_visible(locator)
        field.clear()
        field.send_keys(text)


class SearchPage(BasePage):
    INPUT_SEARCH_FIELD = (By.ID, 'search-field')                 # Поле поиска
    BUTTON_SUBMIT_SEARCH = (By.CLASS_NAME, 'b-header-b-search-e-btn')  # Кнопка поиска
    RESULTS_CONTAINER = (By.CLASS_NAME, 'products-row')          # Контейнер с результатами

    def perform_search(self, keyword):
        self.send_text(keyword, self.INPUT_SEARCH_FIELD)
        self.click(self.BUTTON_SUBMIT_SEARCH)
        return self.check_results_present()

    def check_results_present(self):
        try:
            self.wait_until_visible(self.RESULTS_CONTAINER)
            return True
        except TimeoutException:
            return False


class GenresPage(BasePage):
    GENRES_SECTION = (By.CLASS_NAME, 'subgenres')                       # Секция жанров
    GENRE_LINK_TEMPLATE = (By.XPATH, "//a[contains(@href,'/genres/') and contains(text(),'{}')]")  # Генерируемая ссылка на жанр

    def go_to_genres_section(self):
        section = self.wait_until_visible(self.GENRES_SECTION)
        return GenresPage(self.driver)

    def choose_genre(self, genre_name):
        link = self.wait_until_visible(self.GENRE_LINK_TEMPLATE.format(genre_name))
        link.click()
        return SearchPage(self.driver)


class HomePage(BasePage):
    HOMEPAGE_LINK = (By.LINK_TEXT, 'Главная')                           # Главная ссылка

    def return_to_homepage(self):
        self.click(self.HOMEPAGE_LINK)
        return HomePage(self.driver)
