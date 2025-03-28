import allure
import pytest
from pages.customers_page import CustomersPage
from helpers.utils import find_closest_name_by_length


@allure.feature("Customer Management")
@allure.story("Customer list operations")
class TestCustomers:
    @allure.title("Verify customer sorting functionality")
    def test_sort_customers(self, driver):
        with allure.step("Open Customers tab"):
            customers_page = CustomersPage(driver)
            customers_page.click_customers_tab()

        with allure.step("Capture initial customer list"):
            original_names = customers_page.get_customers_first_names()

        with allure.step("Sort customers by first name"):
            customers_page.sort_by_first_name()

        with allure.step("Verify sorting order"):
            sorted_names = customers_page.get_customers_first_names()
            assert sorted_names == sorted(original_names, reverse=True), "Customers are not sorted correctly"

    @allure.title("Verify customer deletion functionality")
    def test_delete_customer(self, driver):
        with allure.step("Open Customers tab"):
            customers_page = CustomersPage(driver)
            customers_page.click_customers_tab()

        with allure.step("Retrieve existing customer list"):
            names = customers_page.get_customers_first_names()

            if not names:
                pytest.fail("No customers available for deletion")

        with allure.step("Select customer closest to average name length"):
            closest_name = find_closest_name_by_length(names)

        with allure.step("Delete selected customer"):
            customers_page.delete_customer_by_name(closest_name)

        with allure.step("Verify customer deletion"):
            remaining_names = customers_page.get_customers_first_names()
            assert closest_name not in remaining_names, f"Customer {closest_name} was not deleted"