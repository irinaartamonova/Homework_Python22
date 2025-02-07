import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_shop_purchase():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_primary").click()
    driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_primary").click()
    driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(3) .btn_primary").click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    assert total == "Total: $58.29"

    driver.quit()