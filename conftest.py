import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from data.test_data import TestData
from helpers.generate_data import (generate_first_name, generate_last_name,
                                   generate_post_code)
from pages.customers_page import CustomersPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--window-size={TestData.BROWSER_WINDOW_SIZE}")
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(TestData.BASE_URL)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def prepare_user_data(driver):
    post_code = generate_post_code()
    first_name = generate_first_name(post_code)
    last_name = generate_last_name()

    yield post_code, first_name, last_name

    customers_page = CustomersPage(driver)
    customers_page.click_customers_tab()
    customers_page.delete_customer_by_name(first_name)
