from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        # Локаторы
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.ID, "seven")
        self.button_plus = (By.ID, "plus")
        self.button_8 = (By.ID, "eight")
        self.button_equals = (By.ID, "equals")
        self.result_display = (By.ID, "result")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(delay)

    def press_button_7(self):
        self.driver.find_element(*self.button_7).click()

    def press_button_plus(self):
        self.driver.find_element(*self.button_plus).click()

    def press_button_8(self):
        self.driver.find_element(*self.button_8).click()

    def press_button_equals(self):
        self.driver.find_element(*self.button_equals).click()

    def get_result(self):
        return self.driver.find_element(*self.result_display).text
