import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from page_objects import FormPage
import allure
from allure_commons.types import Severity


@allure.feature("Form Filling")
class TestForm:
    @pytest.fixture(scope="function")
    def driver(self):
        with allure.step("Initialize Chrome WebDriver"):
            driver = webdriver.Chrome()
        yield driver
        with allure.step("Quit WebDriver"):
            driver.quit()

    @allure.title("Test Filling Form with Validation")
    @allure.description("This test fills the form with valid data except for ZIP code, then checks the validation colors.")
    @allure.severity(Severity.CRITICAL)
    def test_fill_form(self, driver: WebDriver):
        with allure.step("Open Form Page"):
            form_page = FormPage(driver)
            form_page.open()

        with allure.step("Fill the form with data"):
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

        with allure.step("Submit the form"):
            form_page.submit()

        @allure.step("Verify ZIP code field color is red")
        def assert_zip_code_color():
            zip_code_color = form_page.get_zip_code_color()
            assert zip_code_color == 'rgba(255, 0, 0, 1)'

        assert_zip_code_color()

        @allure.step("Verify other fields colors are green")
        def assert_other_fields_colors():
            other_fields_colors = form_page.get_other_fields_color()
            assert all(color == 'rgba(0, 128, 0, 1)' for color in other_fields_colors)

        assert_other_fields_colors()

