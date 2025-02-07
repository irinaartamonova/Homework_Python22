import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():

    driver = webdriver.Chrome()
    yield driver

    driver.quit()

def test_shop_total_price(browser):

    browser.get("https://www.saucedemo.com/")

    username_field = browser.find_element(By.ID, "user-name")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:

        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"))
        )
        add_to_cart_button.click()

    cart_button = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    checkout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    first_name_field = browser.find_element(By.ID, "first-name")
    last_name_field = browser.find_element(By.ID, "last-name")
    postal_code_field = browser.find_element(By.ID, "postal-code")
    continue_button = browser.find_element(By.ID, "continue")

    first_name_field.send_keys("John")
    last_name_field.send_keys("Doe")
    postal_code_field.send_keys("12345")
    continue_button.click()

    total_price_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_price_text = total_price_element.text
    total_price = float(total_price_text.replace("Total: $", ""))

    assert total_price == 58.29, f"Expected total price to be $58.29, but got {total_price}"
