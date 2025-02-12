import pytest
from selenium import webdriver
from shop_page import LoginPage, ProductsPage, CheckoutPage
import allure
from allure_commons.types import Severity


@allure.feature("Shopping Cart")
class TestShopping:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @allure.title("Successful shopping cart checkout")
    @allure.description("This test verifies the successful checkout process in the shopping cart.")
    @allure.severity(Severity.CRITICAL)
    def test_shopping_cart(self, driver):

        @allure.step("Open login page")
        def open_login_page():
            login_page = LoginPage(driver)
            login_page.open()
            return login_page

        login_page = open_login_page()

        @allure.step("Login with username: {username} and password: {password}")
        def login(username, password):
            login_page.login(username, password)

        login("standard_user", "secret_sauce")

        @allure.step("Add products to cart")
        def add_products():
            products_page = ProductsPage(driver)
            products_page.add_products_to_cart()
            return products_page

        products_page = add_products()


        @allure.step("Go to cart")
        def go_to_cart():
             products_page.go_to_cart()

        go_to_cart()



        @allure.step("Fill checkout information with first name: {first_name}, last name: {last_name}, and postal code: {postal_code}")
        def fill_checkout(first_name, last_name, postal_code):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_info(first_name, last_name, postal_code)
            return checkout_page

        checkout_page = fill_checkout("Иван", "Петров", "12345")

        @allure.step("Get total amount")
        def get_total():
            total = checkout_page.get_total()
            return total

        total = get_total()


        @allure.step("Assert total is equal to expected total: {expected_total}")
        def assert_total(actual_total, expected_total):
            assert actual_total == expected_total

        assert_total(total, "Total: $58.29")