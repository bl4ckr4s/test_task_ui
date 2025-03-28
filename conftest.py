import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from helpers.generate_data import generate_first_name, generate_post_code
from pages.customers_page import CustomersPage

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager")

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def prepare_user_data(driver):
    post_code = generate_post_code()
    first_name = generate_first_name(post_code)
    yield post_code, first_name
    customers_page = CustomersPage(driver)
    customers_page.click_customers_tab()
    customers_page.delete_customer_by_name(first_name)
