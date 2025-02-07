from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
 service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_element_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
        add_element_button.click()

delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

sleep(5)