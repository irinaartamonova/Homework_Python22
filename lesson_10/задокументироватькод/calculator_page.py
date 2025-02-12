from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class CalculatorPage:
    """
    Класс, представляющий страницу калькулятора.

    Содержит методы для взаимодействия с элементами страницы калькулятора,
    такими как ввод задержки, нажатие кнопок и получение результата.
    """
    def __init__(self, driver):
        """
        Инициализирует объект CalculatorPage.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.ID, "seven")
        self.button_plus = (By.ID, "plus")
        self.button_8 = (By.ID, "eight")
        self.button_equals = (By.ID, "equals")
        self.result_display = (By.ID, "result")

    def open(self):
        """
        Открывает страницу калькулятора в браузере.

        Returns:
            None
        """
        self.driver.get(self.url)

    def set_delay(self, delay: str):
        """
        Устанавливает задержку для калькулятора.

        Args:
            delay (str): Задержка в миллисекундах (в виде строки).

        Returns:
            None
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(delay)

    def press_button_7(self):
        """
        Нажимает кнопку '7' на калькуляторе.

        Returns:
            None
        """
        self.driver.find_element(*self.button_7).click()

    def press_button_plus(self):
        """
        Нажимает кнопку '+' на калькуляторе.

        Returns:
            None
        """
        self.driver.find_element(*self.button_plus).click()

    def press_button_8(self):
        """
        Нажимает кнопку '8' на калькуляторе.

        Returns:
            None
        """
        self.driver.find_element(*self.button_8).click()

    def press_button_equals(self):
        """
        Нажимает кнопку '=' на калькуляторе.

        Returns:
            None
        """
        self.driver.find_element(*self.button_equals).click()

    def get_result(self) -> str:
        """
        Возвращает результат, отображаемый на калькуляторе.

        Returns:
            str: Текст, отображаемый в поле результата.
        """
        return self.driver.find_element(*self.result_display).text

