# Комплексный набор автоматизированных тестов для сайта "Лабиринт"- https://www.labirint.ru/
* О проекте
Проект направлен на повышение качества программного обеспечения сайта "Лабиринт" посредством автоматизации тестирования API и UI. Главная цель — обеспечение надежного и эффективного процесса выявления дефектов и регрессий. Набор тестов охватывает ключевые области взаимодействия пользователя с сайтом, такие как поиск товаров, сортировка, просмотр информации о продуктах и многое другое.
Ссылка на финальный проект: 
https://skyproolga.yonote.ru/share/99fe1e21-75a2-4133-952b-f45e69cc1190

# Задачи проекта
- Разработать высококачественный набор автоматизированных тестов для API и UI сайта.
- Демонстрировать знания в области тестирования, анализа требований и разработки качественных тестов.
- Организовать инфраструктуру тестирования с поддержкой создания и интерпретации отчетов.

# Установка и предварительная подготовка
* Минимальные требования:
- Python 3.8+
- Браузер Chrome с установленным драйвером ChromeDriver.
- Интерфейс Allure для просмотра отчетов.

# Установка зависимостей:
Установите необходимые библиотеки с помощью pip:

- pip install -r requirements.txt

# Запуск тестов:
Выполните следующие шаги для запуска тестов:

1. Перейдите в директорию проекта:

- cd path/to/your/project

2. Запустите тесты с сохранением результатов в папку test_reports:

- pytest --alluredir=test_reports

# Генерация отчёта Allure:
Просмотрите отчёт о выполнении тестов:
- allure serve test_reports
Ваш браузер автоматически откроет отчёт с подробной статистикой прохождения тестов.

# Результаты проекта
Реализован набор тестов, позволяющий эффективно выявлять дефекты и повышать общее качество обслуживания сайта "Лабиринт".

