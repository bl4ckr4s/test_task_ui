# Тестовое задание на SDET-практикум

Проект содержит набор UI автотестов для страницы [globalsqa.com](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager).

## Инструменты

- Python 3.10
- Selenium WebDriver (Chrome)
- PyTest
- PyTest Xdist
- Allure для формирования отчётов


## Установка и запуск

1. Создайте и активируйте виртуальное окружение (рекомендуется).
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
3. Запустите тесты с формированием Allure-отчёта:
 - стандартный запуск тестов в pytest
         
   ```bash   
   pytest -v --alluredir=allure-results
   
 - параллельный запуск тестов в pytest с использованием pytest-xdist
   ```bash
   pytest -v -n auto --alluredir=allure-results
   
4. Сгенерируйте и откройте отчет:
   ```bash
   allure serve allure-results
---



   


