import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_calculator():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    driver.find_element(By.CSS_SELECTOR, "button[value='7']").click()
    driver.find_element(By.CSS_SELECTOR, "button[value='+']").click()
    driver.find_element(By.CSS_SELECTOR, "button[value='8']").click()
    driver.find_element(By.CSS_SELECTOR, "button[value='='").click()

    result = driver.find_element(By.CSS_SELECTOR, "#result").text
    assert result == "15"

    driver.quit()

