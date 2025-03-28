from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.customers_tab = (By.CSS_SELECTOR, "button[ng-click='showCust()']")
        self.customers_table_rows = (By.CSS_SELECTOR, "table tbody tr")
        self.first_name_header = (By.XPATH, "//a[contains(@ng-click, 'fName')]")
        self.delete_button = (By.XPATH, ".//button[contains(text(), 'Delete')]")
        self.first_name_column = (By.XPATH, "./td[1]")

    def click_customers_tab(self) -> None:
        self.click(self.customers_tab)

    def sort_by_first_name(self) -> None:
        self.click(self.first_name_header)

    def get_customers_first_names(self) -> list:
        rows = self.find_elements(self.customers_table_rows)
        return [row.find_element(*self.first_name_column).text for row in rows]

    def delete_customer_by_name(self, name: str) -> None:
        rows = self.find_elements(self.customers_table_rows)
        for row in rows:
            first_name = row.find_element(*self.first_name_column).text
            if first_name == name:
                delete_button = row.find_element(*self.delete_button)
                delete_button.click()
                return
        raise ValueError(f"User '{name}' was not found for deletion")