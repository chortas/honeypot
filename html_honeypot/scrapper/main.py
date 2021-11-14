from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://192.168.1.11:5000/form")

inputs = driver.find_elements_by_xpath(f"/html/body/form/input")

for input in inputs:
    input.send_keys("bot_input")

form = driver.find_element_by_xpath(f"/html/body/form[1]")

form.submit()

#driver.close()