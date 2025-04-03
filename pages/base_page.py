import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Клик по элементу")
    def click_to_element(self, locator: tuple[str, str]) -> None:
        """
        Click on an element after waiting for it to be clickable.

        Args:
            locator (tuple[str, str]): Element locator in format (By.TYPE, "value")

        Returns:
            None

        Raises:
            TimeoutException: "Элемент с локатором 'locator' не является кликабельным"
        """
        self.wait.until(EC.element_to_be_clickable(locator),
                        message=f"Элемент с локатором '{locator}' не является кликабельным").click()

    @allure.step("Ввод значения")
    def send_keys(self, locator: tuple[str, str], text: str) -> None:
        """
        Enter text into an input field after waiting for it to be visible.

        Args:
            locator (tuple[str, str]): Element locator in format (By.TYPE, "value")
            text (str): Text to enter into the field

        Returns:
            None
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Поиск элементов по локатору")
    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        """
        Find all elements matching the given locator.

        Waits for the elements to be present in the DOM before returning them.
        The action is logged as a step in Allure reports.

        Args:
            locator (tuple[str, str]): Element locator in format (By.TYPE, "value")

        Returns:
            list[WebElement]: List of found WebElement objects

        Raises:
            TimeoutException: "Элементы с локатором 'locator' не найдены."
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Элементы с локатором '{locator}' не найдены.")

    @allure.step("Принять уведомление и вернуть его текст")
    def accept_alert(self) -> str:
        """
        Accept a JavaScript alert and return its text content.

        Returns:
            str: The text content of the alert
        """
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def get_element_text(self, element: WebElement) -> str:
        """
        Get text from the specified element.

        Args:
            element (WebElement): WebElement for text retrieval

        Returns:
            str: Text content of the element
        """
        with allure.step(f"Получить текст из элемента: '{element.tag_name} {element.get_attribute('class')} {element.get_attribute('id')}'"):
            return element.text
