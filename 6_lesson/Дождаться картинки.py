from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 50)
wait.until(EC.presence_of_element_located((By.ID, "image-container")))

third_image = driver.find_element(By.CSS_SELECTOR, "#image-container img:nth-child(3)")
src_value = third_image.get_attribute("src")

print(src_value)

driver.quit()