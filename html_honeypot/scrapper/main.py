from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://0.0.0.0:5000/form")

inputs = driver.find_elements_by_xpath(f"/html/body/form/input")

for input in inputs:
    input.send_keys("bot_input")

form = driver.find_element_by_xpath(f"/html/body/form[1]")

form.submit()

#driver.close()