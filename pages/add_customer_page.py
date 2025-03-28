from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddCustomerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_customer_tab = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
        self.first_name_input = (By.CSS_SELECTOR, "input[ng-model='fName']")
        self.last_name_input = (By.CSS_SELECTOR, "input[ng-model='lName']")
        self.post_name_input = (By.CSS_SELECTOR, "input[ng-model='postCd']")
        self.add_customer_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.last_name = "Doe"

    def click_add_customer_tab(self) -> None:
        self.click(self.add_customer_tab)

    def add_customer(self,post_code: str, first_name: str) -> str:
        self.send_keys(self.first_name_input, first_name)
        self.send_keys(self.last_name_input, self.last_name)
        self.send_keys(self.post_name_input, post_code)
        self.click(self.add_customer_button)
        return first_name

