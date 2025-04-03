import allure
import pytest

from helpers.utils import find_closest_name_by_length
from pages.customers_page import CustomersPage


@allure.feature("Управление пользователями")
@allure.story("Операции со списком пользователей")
class TestCustomers:
    @allure.title("Проверка функциональности сортировки пользователей")
    def test_sort_customers(self, driver):
        with allure.step("Открытие вкладки 'Customers'"):
            customers_page = CustomersPage(driver)
            customers_page.click_customers_tab()

        with allure.step("Получение первоначального списка пользователей"):
            original_names = customers_page.get_customers_first_names()

        with allure.step("Сортировка пользователей по полю 'First Name'"):
            customers_page.sort_by_first_name()

        with allure.step("Проверка порядка сортировки"):
            sorted_names = customers_page.get_customers_first_names()
            assert sorted_names == sorted(original_names, reverse=True), "Неправильная сортировка пользователей"

    @allure.title("Проверка функциональности удаления пользователей")
    def test_delete_customer(self, driver):
        with allure.step("Открытие вкладки 'Customers'"):
            customers_page = CustomersPage(driver)
            customers_page.click_customers_tab()

        with allure.step("Получение списка существующих пользователей"):
            names = customers_page.get_customers_first_names()

            if not names:
                pytest.fail("Нет пользователей, доступных для удаления")

        with allure.step("Поиск подходящего клиента по средней длине имени"):
            closest_name = find_closest_name_by_length(names)

        with allure.step(f"Удаление покупателя - {closest_name}"):
            customers_page.delete_customer_by_name(closest_name)

        with allure.step("Проверка удаления пользователя"):
            remaining_names = customers_page.get_customers_first_names()
            assert closest_name not in remaining_names, f"Пользователь {closest_name} не был удален"
