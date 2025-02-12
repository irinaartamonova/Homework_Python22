import allure
from allure_commons.types import Severity
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открываем страницу логина")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Входим в систему с логином: {username} и паролем: {password}")
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

        self.add_backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_tshirt_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавляем товары в корзину")
    def add_products_to_cart(self):
        self.driver.find_element(*self.add_backpack_button).click()
        self.driver.find_element(*self.add_tshirt_button).click()
        self.driver.find_element(*self.add_onesie_button).click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.checkout_button = (By.CSS_SELECTOR, ".btn_action.checkout_button")
        self.total_label = (By.CSS_SELECTOR, ".summary_total_label")

    @allure.step("Заполняем информацию о доставке: Имя: {first_name}, Фамилия: {last_name}, Индекс: {zip_code}")
    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.checkout_button).click()

    @allure.step("Получаем итоговую сумму заказа")
    def get_total(self):
        return self.driver.find_element(*self.total_label).text

import unittest
from selenium import webdriver


@allure.feature("Покупка товара")
class TestPurchase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.title("Успешное оформление заказа")
    @allure.description("Проверяет успешное оформление заказа после добавления товаров в корзину.")
    @allure.severity(Severity.CRITICAL)
    def test_successful_checkout(self):
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")

        self.products_page.add_products_to_cart()
        self.products_page.go_to_cart()

        self.checkout_page.fill_checkout_info("John", "Doe", "12345")

        total = self.checkout_page.get_total()

        with allure.step("Проверка итоговой суммы"):
            self.assertTrue("Item total: $" in total, "Итоговая сумма не отображается")
            print(f"Итоговая сумма: {total}")


if __name__ == '__main__':
    unittest.main()
