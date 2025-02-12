import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
import time

class TestCalculator:
    """
    Класс, содержащий тестовые случаи для калькулятора.
    """
    @pytest.fixture(scope="function")
    def driver(self):
        """
        Фикстура pytest, создающая и уничтожающая экземпляр WebDriver для каждого теста.

        :return: webdriver.Chrome: Экземпляр WebDriver.
        """
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_calculator(self, driver):
        """
        Тестовый случай, проверяющий сложение двух чисел в калькуляторе.

        :param driver: webdriver.Chrome: Экземпляр WebDriver, предоставленный фикстурой.
        :return: None
        """
        calculator_page = CalculatorPage(driver)
        calculator_page.open()

        calculator_page.set_delay("45")

        calculator_page.press_button_7()
        calculator_page.press_button_plus()
        calculator_page.press_button_8()
        calculator_page.press_button_equals()

        time.sleep(45)  # Wait for the delay

        result = calculator_page.get_result()
        assert result == '15'

from selenium.webdriver.remote.webdriver import WebDriver

class CalculatorPage:
    """
    Класс, представляющий страницу калькулятора.  Содержит методы для взаимодействия с элементами страницы.
    """

    def __init__(self, driver: WebDriver):
        """
        Конструктор класса CalculatorPage.

        :param driver: webdriver.Chrome: Экземпляр WebDriver, используемый для взаимодействия с браузером.
        :return: None
        """
        self.driver = driver

    def open(self):
        """
        Открывает страницу калькулятора.

        :return: None
        """

    def set_delay(self, delay: str):
        """
        Устанавливает задержку для калькулятора.

        :param delay: str: Значение задержки в секундах.
        :return: None
        """

    def press_button_7(self):
        """
        Нажимает кнопку '7' на калькуляторе.

        :return: None
        """

    def press_button_plus(self):
        """
        Нажимает кнопку '+' на калькуляторе.

        :return: None
        """

    def press_button_8(self):
        """
        Нажимает кнопку '8' на калькуляторе.

        :return: None
        """

    def press_button_equals(self):
        """
        Нажимает кнопку '=' на калькуляторе.

        :return: None
        """

    def get_result(self) -> str:
        """
        Возвращает результат, отображаемый на калькуляторе.

        :return: str: Текстовое значение результата.
        """
        return "result" 
    
    