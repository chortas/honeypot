from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://0.0.0.0:5000/form")

inputs = driver.find_elements(By.XPATH, "/html/body/form/input")

for input in inputs:
    input.send_keys("bot_input")

form = driver.find_element(By.XPATH, "/html/body/form[1]")

form.submit()

#driver.close()