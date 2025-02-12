from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FormPage:
    """
    Класс, представляющий страницу с формой на веб-сайте.
    """
    def __init__(self, driver):
        """
        Инициализирует объект FormPage.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        self.first_name_input = (By.NAME, "firstname")
        self.last_name_input = (By.NAME, "lastname")
        self.address_input = (By.NAME, "address")
        self.email_input = (By.NAME, "email")
        self.phone_input = (By.NAME, "phone")
        self.zip_code_input = (By.NAME, "zip")
        self.city_input = (By.NAME, "city")
        self.country_input = (By.NAME, "country")
        self.job_position_input = (By.NAME, "job")
        self.company_input = (By.NAME, "company")
        self.submit_button = (By.XPATH, "//button[@type='submit']")

    def open(self):
        """
        Открывает страницу формы в веб-браузере.

        Returns:
            None
        """
        self.driver.get(self.url)

    def fill_form(self, first_name: str, last_name: str, address: str, email: str, phone: str, zip_code: str, city: str, country: str, job_position: str, company: str):
        """
        Заполняет поля формы предоставленными данными.

        Args:
            first_name (str): Имя.
            last_name (str): Фамилия.
            address (str): Адрес.
            email (str): Электронная почта.
            phone (str): Телефон.
            zip_code (str): Почтовый индекс.
            city (str): Город.
            country (str): Страна.
            job_position (str): Должность.
            company (str): Компания.

        Returns:
            None
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.address_input).send_keys(address)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.city_input).send_keys(city)
        self.driver.find_element(*self.country_input).send_keys(country)
        self.driver.find_element(*self.job_position_input).send_keys(job_position)
        self.driver.find_element(*self.company_input).send_keys(company)

    def submit(self):
        """
        Нажимает кнопку отправки формы.

        Returns:
            None
        """
        self.driver.find_element(*self.submit_button).click()

    def get_zip_code_color(self) -> str:
        """
        Возвращает цвет границы поля почтового индекса.

        Returns:
            str: Цвет границы в формате CSS.
        """
        return self.driver.find_element(*self.zip_code_input).value_of_css_property("border-color")

    def get_other_fields_color(self) -> list:
        """
        Возвращает цвет границы для всех текстовых полей, кроме почтового индекса.

        Returns:
            list: Список цветов границ в формате CSS.
        """
        fields = [self.first_name_input, self.last_name_input, self.address_input, self.email_input,
                  self.phone_input, self.city_input, self.country_input, self.job_position_input, self.company_input]
        return [self.driver.find_element(*field).value_of_css_property("border-color") for field in fields]