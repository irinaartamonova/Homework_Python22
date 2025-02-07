from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, "input")

input_field.send_keys("1000")
input_field.clear()
input_field.send_keys("999")

time.sleep(5)

driver.quit()