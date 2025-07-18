import os

# Базовая информация о сайте и API
LABIRINT_URL = os.getenv('LABIRINT_URL', 'https://www.labirint.ru/')
API_BASE_URL = os.getenv('LABIRINT_API_URL', 'https://api.labirint.ru/v1/')

# Таймаут ожидания элементов в секундах
EXPLICIT_WAIT_TIME = int(os.getenv('EXPLICIT_WAIT_TIME', 10)) # Используем for explicit waits in Selenium

# Данные для тестов
TEST_SEARCH_KIRILLIC = 'Приключения Алисы в Стране Чудес: Льюис Кэрролл'
TEST_SEARCH_DIGITS = '1000 животных с наклейками'
TEST_SEARCH_LATIN = 'Harry Potter & the Prisoner of Azkaban: Joanne Rowling'
TEST_SEARCH_EMPTY = ''
TEST_SEARCH_STANDARD = 'Война и мир'

# Переменные для UI-тестов
SEARCH_KEYWORD = 'Книга'
SEARCH_GENRE = 'Детективы'
SEARCH_CYRILLIC = 'Колобок'

# Параметры запросов
TIMEOUT_REQUEST = int(os.getenv('TIMEOUT_REQUEST', 10))
REQUEST_RETRIES = int(os.getenv('REQUEST_RETRIES', 3))

# Настройка Selenium (драйвер и опции)
CHROME_DRIVER_PATH = r"C:\Users\OlgaV\.local\bin\chromedriver.exe"
