import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def setup():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(setup):
    driver = setup
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//button[text()='7']").click()
    driver.find_element(By.XPATH, "//button[text()=' + ']").click()
    driver.find_element(By.XPATH, "//button[text()='8']").click()
    driver.find_element(By.XPATH, "//button[text()=' = ']").click()

    time.sleep(50)

    result = driver.find_element(By.ID, "result").text
    assert result == "15", f"Ожидалось '15', но получено '{result}'"

if __name__ == "__main__":
    pytest.main()
