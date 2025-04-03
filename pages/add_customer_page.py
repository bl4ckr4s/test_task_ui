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

    def click_add_customer_tab(self) -> None:
        """
        Click on the 'Add Customer' tab in the user interface.

        Returns:
            None
        """
        self.click_to_element(self.add_customer_tab)

    def add_customer(self, post_code: str, first_name: str, last_name: str) -> str:
        """
        Add a new customer with the given information.

        Args:
            post_code (str): Customer's post code
            first_name (str): Customer's firstname
            last_name (str): Customer's lastname

        Returns:
            str: Customer's first name
        """
        self.send_keys(self.first_name_input, first_name)
        self.send_keys(self.last_name_input, last_name)
        self.send_keys(self.post_name_input, post_code)
        self.click_to_element(self.add_customer_button)
        return first_name
