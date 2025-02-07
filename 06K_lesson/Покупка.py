import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # Убедитесь, что драйвер Chrome установлен
    yield driver
    driver.quit()

def test_shop_purchase(driver):
    driver.get("https://www.saucedemo.com/")

    # Автоматизация авторизации
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Добавление товаров в корзину
    driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_primary").click()
    driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_primary").click()
    driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(3) .btn_primary").click()

    # Переход в корзину и checkout
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Ожидание отображения итоговой суммы
    total = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
    ).text

    # Проверка формата итога
    assert total.strip() == "Total: $58.29"
