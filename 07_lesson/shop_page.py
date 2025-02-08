from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

        # Локаторы
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

        # Локаторы
        self.add_backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_tshirt_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_products_to_cart(self):
        self.driver.find_element(*self.add_backpack_button).click()
        self.driver.find_element(*self.add_tshirt_button).click()
        self.driver.find_element(*self.add_onesie_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Локаторы
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.checkout_button = (By.CSS_SELECTOR, ".btn_action.checkout_button")
        self.total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.checkout_button).click()

    def get_total(self):
        return self.driver.find_element(*self.total_label).text
    
    