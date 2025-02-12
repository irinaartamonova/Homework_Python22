import pytest
from selenium import webdriver
from shop_page import LoginPage, ProductsPage, CheckoutPage

class TestShopping:
    """
    Класс, содержащий тесты для проверки функциональности корзины покупок.
    """
    @pytest.fixture(scope="function")
    def driver(self):
        """
        Фикстура Pytest для инициализации и завершения работы веб-драйвера Chrome.

        Yields:
            webdriver.Chrome: Экземпляр веб-драйвера Chrome.
        """
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_shopping_cart(self, driver):
        """
        Тест для проверки процесса добавления товаров в корзину, перехода к оформлению заказа и проверки итоговой суммы.

        Args:
            driver (webdriver.Chrome): Экземпляр веб-драйвера, предоставленный фикстурой.

        Returns:
            None
        """

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)
        products_page.add_products_to_cart()

        products_page.go_to_cart()
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("Иван", "Петров", "12345")

        total = checkout_page.get_total()

        assert total == "Total: $58.29"
