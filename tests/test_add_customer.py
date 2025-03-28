import allure
from pages.add_customer_page import AddCustomerPage


@allure.feature("Customer Management")
@allure.story("Customer creation")
class TestAddCustomer:
    @allure.title("Verify successful customer addition")
    def test_add_customer(self, driver, prepare_user_data):
        with allure.step("Open Customers tab"):
            add_customer_page = AddCustomerPage(driver)
            add_customer_page.click_add_customer_tab()

        with allure.step("Fill customer registration form and submit"):
            post_code, first_name = prepare_user_data
            add_customer_page.add_customer(post_code, first_name)

        with allure.step("Verify successful customer creation"):
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()

            assert "Customer added successfully" in alert_text, f"Unexpected alert message: {alert_text}"