import allure

from pages.add_customer_page import AddCustomerPage


@allure.feature("Управление пользователями")
@allure.story("Создание пользователя")
class TestAddCustomer:
    @allure.title("Проверка функциональности добавления пользователя")
    def test_add_customer(self, driver, prepare_user_data):
        with allure.step("Открытие вкладки 'Add Customer'"):
            add_customer_page = AddCustomerPage(driver)
            add_customer_page.click_add_customer_tab()

        with allure.step("Заполнение формы и ее отправка"):
            post_code, first_name, last_name = prepare_user_data
            add_customer_page.add_customer(post_code, first_name, last_name)

        with allure.step("Проверка успешного создания пользователя"):
            alert_text = add_customer_page.accept_alert()
            assert "Customer added successfully" in alert_text, f"Неожиданное оповещение: {alert_text}"
