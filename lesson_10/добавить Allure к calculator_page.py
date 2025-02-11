from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import allure
from allure_commons.types import Severity


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.ID, "seven")
        self.button_plus = (By.ID, "plus")
        self.button_8 = (By.ID, "eight")
        self.button_equals = (By.ID, "equals")
        self.result_display = (By.ID, "result")

    @allure.step("Открыть страницу калькулятора")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Установить задержку {delay}")
    def set_delay(self, delay):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(delay)

    @allure.step("Нажать кнопку 7")
    def press_button_7(self):
        self.driver.find_element(*self.button_7).click()

    @allure.step("Нажать кнопку +")
    def press_button_plus(self):
        self.driver.find_element(*self.button_plus).click()

    @allure.step("Нажать кнопку 8")
    def press_button_8(self):
        self.driver.find_element(*self.button_8).click()

    @allure.step("Нажать кнопку =")
    def press_button_equals(self):
        self.driver.find_element(*self.button_equals).click()

    @allure.step("Получить результат")
    def get_result(self):
        return self.driver.find_element(*self.result_display).text
