from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.customers_tab = (By.CSS_SELECTOR, "button[ng-click='showCust()']")
        self.first_name_header = (By.XPATH, "//a[contains(@ng-click, 'fName')]")
        self.first_name_column = (By.XPATH, "//tr[contains(@ng-repeat, \"cust in Customers\")]/td[1]")

    def click_customers_tab(self) -> None:
        """
        Click on the Customers tab to navigate to the customers listing page.

        Returns:
            None
        """
        self.click_to_element(self.customers_tab)

    def sort_by_first_name(self) -> None:
        """
        Clicks on the first name column header to toggle sorting.

        Returns:
            None
        """
        self.click_to_element(self.first_name_header)

    def get_customers_first_names(self) -> list:
        """
        Get a list of all customer first names currently displayed in the table.

        Returns:
            list: List of strings containing the first names of all displayed customers
        """
        first_names_list = []
        rows = self.find_elements(self.first_name_column)
        for row in rows:
            first_names_list.append(self.get_element_text(row))

        return first_names_list

    def delete_customer_by_name(self, name: str) -> None:
        """
        Delete a customer record by matching the first name.

        Args:
            name (str): First name of the customer to delete

        Returns:
            None
        """
        delete_button_locator = (By.XPATH, f"//table//tr[td[1][text()='{name}']]//button[contains(text(), 'Delete')]")
        self.click_to_element(delete_button_locator)
