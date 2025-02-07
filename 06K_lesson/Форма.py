import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "firstname").send_keys("Иван")
    driver.find_element(By.NAME, "lastname").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_input = driver.find_element(By.NAME, "zip")
    assert "border-color: red;" in zip_code_input.get_attribute("style")

    other_fields = [
        "firstname",
        "lastname",
        "address",
        "email",
        "phone",
        "city",
        "country",
        "job",
        "company"
    ]

    for field in other_fields:
        input_element = driver.find_element(By.NAME, field)
        assert "border-color: green;" in input_element.get_attribute("style")

    driver.quit()