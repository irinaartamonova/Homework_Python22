import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser

    browser.quit()

def test_form_submission(browser):

    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


    browser.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    browser.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    browser.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    browser.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    browser.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    browser.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    browser.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    browser.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_field = browser.find_element(By.CSS_SELECTOR, "[name='zip-code']")
    assert zip_code_field.value_of_css_property("background-color") == "rgba(248, 215, 218, 1)"
    "Поле Zip code не подсвечено красным"

    fields_to_check = [
        ("first-name", "rgba(209, 231, 221, 1)"),
        ("last-name", "rgba(209, 231, 221, 1)"),
        ("address", "rgba(209, 231, 221, 1)"),
        ("e-mail", "rgba(209, 231, 221, 1)"),
        ("phone", "rgba(209, 231, 221, 1)"),
        ("city", "rgba(209, 231, 221, 1)"),
        ("country", "rgba(209, 231, 221, 1)"),
        ("job-position", "rgba(209, 231, 221, 1)"),
        ("company", "rgba(209, 231, 221, 1)")
    ]

    for field_name, expected_color in fields_to_check:
        field = browser.find_element(By.CSS_SELECTOR, f"[name='{field_name}']")
        actual_color = field.value_of_css_property("background-color")
        assert actual_color == expected_color, f"Поле {field_name} не подсвечено зеленым"
