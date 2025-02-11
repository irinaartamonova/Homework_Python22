import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from page_objects import FormPage

class TestForm:
    """
    Тестовый класс для проверки заполнения формы.
    """
    @pytest.fixture(scope="function")
    def driver(self) -> WebDriver:
        """
        Фикстура Pytest для создания и уничтожения экземпляра WebDriver.

        Returns:
            WebDriver: Экземпляр WebDriver (Chrome).
        """
        driver = webdriver.Chrome()  
        yield driver
        driver.quit()

    def test_fill_form(self, driver: WebDriver) -> None:
        """
        Тест для заполнения формы и проверки валидации.

        Args:
            driver (WebDriver): Экземпляр WebDriver, предоставляемый фикстурой.

        Returns:
            None
        """
        form_page = FormPage(driver)
        form_page.open()

        form_page.fill_form(
            first_name="Иван",
            last_name="Петров",
            address="Ленина, 55-3",
            email="test@skypro.com",
            phone="+7985899998787",
            zip_code="",  
            city="Москва",
            country="Россия",
            job_position="QA",
            company="SkyPro"
        )

        form_page.submit()


        zip_code_color = form_page.get_zip_code_color()
        assert zip_code_color == 'rgba(255, 0, 0, 1)'

        other_fields_colors = form_page.get_other_fields_color()
        assert all(color == 'rgba(0, 128, 0, 1)' for color in other_fields_colors)

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class FormPage:
    """
    Класс, представляющий страницу с формой.
    """

    def __init__(self, driver: WebDriver):
        """
        Конструктор класса FormPage.

        Args:
            driver (WebDriver): Экземпляр WebDriver.

        Returns:
            None
        """
        self.driver = driver

        self.first_name_field = (By.ID, "firstName")
        self.last_name_field = (By.ID, "lastName")
        self.address_field = (By.ID, "address")
        self.email_field = (By.ID, "email")
        self.phone_field = (By.ID, "phone")
        self.zip_code_field = (By.ID, "zipCode")
        self.city_field = (By.ID, "city")
        self.country_field = (By.ID, "country")
        self.job_position_field = (By.ID, "jobPosition")
        self.company_field = (By.ID, "company")
        self.submit_button = (By.ID, "submit")

    def open(self) -> None:
        """
        Открывает страницу с формой.

        Returns:
            None
        """
        self.driver.get("URL_СТРАНИЦЫ_С_ФОРМОЙ")

    def fill_form(self, first_name: str, last_name: str, address: str, email: str, phone: str, zip_code: str, city: str, country: str, job_position: str, company: str) -> None:
        """
        Заполняет форму данными.

        Args:
            first_name (str): Имя.
            last_name (str): Фамилия.
            address (str): Адрес.
            email (str): Email.
            phone (str): Телефон.
            zip_code (str): Индекс.
            city (str): Город.
            country (str): Страна.
            job_position (str): Должность.
            company (str): Компания.

        Returns:
            None
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.address_field).send_keys(address)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.phone_field).send_keys(phone)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)
        self.driver.find_element(*self.city_field).send_keys(city)
        self.driver.find_element(*self.country_field).send_keys(country)
        self.driver.find_element(*self.job_position_field).send_keys(job_position)
        self.driver.find_element(*self.company_field).send_keys(company)

    def submit(self) -> None:
        """
        Отправляет форму.

        Returns:
            None
        """
        self.driver.find_element(*self.submit_button).click()

    def get_zip_code_color(self) -> str:
        """
        Возвращает цвет поля zip_code.

        Returns:
            str: CSS значение цвета.
        """
        element = self.driver.find_element(*self.zip_code_field)
        return element.value_of_css_property('border-color')

    def get_other_fields_color(self) -> list[str]:
         """
         Возвращает цвета полей first_name, last_name, address, email, phone, city, country, job_position, company.

         Returns:
             list[str]: Список CSS значений цветов.
         """
         colors = []
         fields = [self.first_name_field, self.last_name_field, self.address_field, self.email_field, self.phone_field, self.city_field, self.country_field, self.job_position_field, self.company_field]

         for field in fields:
             element = self.driver.find_element(*field)
             colors.append(element.value_of_css_property('border-color'))
         return colors