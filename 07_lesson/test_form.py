import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from page_objects import FormPage

class TestForm:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()  
        yield driver
        driver.quit()

    def test_fill_form(self, driver: WebDriver):
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
        assert zip_code_color == 'rgba(255, 0, 0, 1)'  #
        
        other_fields_colors = form_page.get_other_fields_color()
        assert all(color == 'rgba(0, 128, 0, 1)' for color in other_fields_colors)


pytest