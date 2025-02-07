import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
import time

class TestCalculator:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_calculator(self, driver):
        calculator_page = CalculatorPage(driver)
        calculator_page.open()

        calculator_page.set_delay("45")

        calculator_page.press_button_7()
        calculator_page.press_button_plus()
        calculator_page.press_button_8()
        calculator_page.press_button_equals()

        time.sleep(45)

        result = calculator_page.get_result()
        assert result == '15'

pytest 