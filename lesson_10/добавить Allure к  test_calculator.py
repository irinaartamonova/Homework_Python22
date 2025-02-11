import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
import time
import allure
from allure_commons.types import Severity


class TestCalculator:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @allure.title("Calculator Addition Test")
    @allure.description("This test performs addition operation on the calculator and verifies the result.")
    @allure.feature("Calculator Functionality")
    @allure.severity(Severity.NORMAL)
    def test_calculator(self, driver):
        with allure.step("Open Calculator Page"):
            calculator_page = CalculatorPage(driver)
            calculator_page.open()

        with allure.step("Set Delay to 45 seconds"):
            calculator_page.set_delay("45")

        with allure.step("Press Button 7"):
            calculator_page.press_button_7()

        with allure.step("Press Button Plus"):
            calculator_page.press_button_plus()

        with allure.step("Press Button 8"):
            calculator_page.press_button_8()

        with allure.step("Press Button Equals"):
            calculator_page.press_button_equals()

        with allure.step("Wait for 45 seconds"):
            time.sleep(45)

        @allure.step("Get Result")
        def get_result_from_page(calculator_page):
            return calculator_page.get_result()

        result = get_result_from_page(calculator_page)

        @allure.step("Assert Result is 15")
        def assert_result(result):
            assert result == '15'

        assert_result(result)

